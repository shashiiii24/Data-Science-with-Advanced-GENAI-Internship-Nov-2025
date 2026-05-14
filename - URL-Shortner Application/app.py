
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import string
import random
import validators

app = Flask(__name__)
app.secret_key = "supersecretkey"  # needed for flash messages

# Database Config (SQLite)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///urls.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Database Model
class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.Text, nullable=False)
    short_code = db.Column(db.String(10), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# Create DB tables
with app.app_context():
    db.create_all()


def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    while True:
        short_code = "".join(random.choices(characters, k=length))
        existing = URL.query.filter_by(short_code=short_code).first()
        if not existing:
            return short_code


@app.route("/", methods=["GET", "POST"])
def home():
    short_url = None

    if request.method == "POST":
        original_url = request.form.get("original_url", "").strip()

        # Validate URL
        if not validators.url(original_url):
            flash("Invalid URL. Please enter a valid link (example: https://google.com).", "danger")
            return render_template("index.html", short_url=None)

        # Check if URL already exists in DB
        existing_url = URL.query.filter_by(original_url=original_url).first()
        if existing_url:
            short_url = request.host_url + existing_url.short_code
            flash("This URL already exists. Returning the saved short link.", "info")
            return render_template("index.html", short_url=short_url)

        # Create new short code + store
        short_code = generate_short_code()
        new_url = URL(original_url=original_url, short_code=short_code)
        db.session.add(new_url)
        db.session.commit()

        short_url = request.host_url + short_code
        flash("URL shortened successfully!", "success")

    return render_template("index.html", short_url=short_url)


@app.route("/history")
def history():
    urls = URL.query.order_by(URL.created_at.desc()).all()
    return render_template("history.html", urls=urls)


@app.route("/<short_code>")
def redirect_to_original(short_code):
    url_entry = URL.query.filter_by(short_code=short_code).first()
    if url_entry:
        return redirect(url_entry.original_url)

    flash("Short URL not found!", "danger")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
