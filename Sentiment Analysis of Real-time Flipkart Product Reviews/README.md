<div align="center">

# Sentiment Analysis of Flipkart Reviews

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=F7B42C&center=true&vCenter=true&width=435&lines=Flipkart+Reviews+Analysis;Sentiment+Classification;Pain+Point+Extraction;Powered+by+AI" alt="Typing SVG" />
</a>
<br/>

---

## 📌 Project Overview
An end-to-end, production-ready Sentiment Analysis system designed to classify Flipkart product reviews (specifically for the YONEX MAVIS 350 Nylon Shuttle) into **Positive** or **Negative** sentiment. It also extracts key **pain points** from negative reviews to identify customer dissatisfaction themes.

This project demonstrates a full-stack AI application, featuring a custom-trained Machine Learning model, a fast Python API, and a modern, interactive Next.js frontend.

## 🚀 Features

### Core AI Capabilities
-   **Sentiment Classification**: Classifies reviews with high accuracy (F1-Score ~92%) using a Logistic Regression model trained on TF-IDF embeddings.
-   **Pain Point Extraction**: Automatically identifies specific complaints (e.g., "bad quality", "waste of money") from negative reviews.
-   **Real-time Inference**: Low-latency predictions via a FastAPI backend.

### Modern Web Interface
-   **Interactive UI**: Built with Next.js 15 and TailwindCSS.
-   **Dynamic Animations**: Smooth fade-ins, glassmorphism effects, and animated gradients.
-   **User Preferences**: Toggleable settings for animations and high-contrast mode.
-   **Responsive Design**: Fully optimized for desktop and mobile devices.

---

## 🛠️ Tech Stack

-   **Frontend**: Next.js 15 (React), TailwindCSS, Lucide Icons
-   **Backend**: FastAPI, Uvicorn, Python 3.10+
-   **Machine Learning**: Scikit-Learn, NLTK, Pandas, Numpy, Joblib
-   **Deployment**: Vercel (Frontend), Vercel/Render (Backend)

---

## 📂 Project Structure

```bash
Sentiment Analysis/
├── api/                # FastAPI Backend
│   ├── main.py         # API Endpoints
│   └── index.py        # Vercel Entry Point
├── app/                # Next.js App Router & Pages
├── public/             # Static Assets
├── models/             # Trained ML Models
│   └── sentiment_model.joblib
│   └── model_params.json
├── src/                # Machine Learning Source Code
│   ├── preprocessing.py# Text Cleaning & Normalization
│   └── train_model.py  # Model Training Script
├── data/               # Dataset
│   └── raw/            # Raw CSV data
├── requirements.txt    # Python Dependencies
├── package.json        # Frontend Dependencies
└── README.md           # Documentation
```

---

## ⚡ Quick Start (Local)

### 1. Backend Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Train the model (if not already trained)
python -m src.train_model

# Run the API
uvicorn api.main:app --reload
```
*API runs at `http://localhost:8000`*

### 2. Frontend Setup
```bash
# Install dependencies
npm install

# Run the app
npm run dev
```
*App runs at `http://localhost:3000`*

---

## 📊 Model Performance

| Model | F1-Score | Accuracy |
|-------|----------|----------|
| **Logistic Regression** | **0.92** | **92%** |
| Random Forest | 0.90 | 90% |
| Naive Bayes | 0.89 | 89% |

*The Logistic Regression model was selected for its balance of high accuracy and extremely low inference latency.*

---

## 🔮 Future Improvements
-   Implement Deep Learning models (BERT/RoBERTa) for potentially higher nuance detection.
-   Add a dashboard for visualization of bulk review uploads.
-   Deploy as a containerized microservice using Docker.

---
<div align="center">

## 👨‍💻 Created By

### SHASHI KIRAN T

## 💼 Open to Data Science & ML opportunities

**Made with ❤️ and Python**

⭐ *Star this repository if you found it helpful!* ⭐

*Last Updated: December 2025*
<div></div>
