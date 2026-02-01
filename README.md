# Customer Churn Prediction System

An **end-to-end machine learning system** that predicts customer churn probability and explains *why* a customer is likely to leave.
Built with **production-style architecture**, separating model inference, explainability, and UI.

---

## 🚀 What This Project Does

* Predicts **churn probability** for a telecom customer
* Converts probability into **business-friendly risk levels**
* Generates **human-readable churn drivers**
* Provides an **interactive Streamlit dashboard**
* Exposes a **FastAPI inference service**
* Supports **Docker-based deployment**

This mirrors how real ML systems are built and deployed in industry.

---

## 🧠 Why This Project Matters

Customer churn directly impacts revenue.
Instead of just predicting *yes/no*, this system:

* Outputs **likelihood**, not certainty
* Explains **drivers behind the prediction**
* Enables **actionable retention strategies**

This makes it suitable for **business decision-making**, not just model evaluation.

---

## 🧱 Tech Stack

* **Python**
* **FastAPI** – backend inference API
* **Streamlit** – frontend UI
* **Scikit-learn** – ML model
* **Pydantic** – input validation
* **Docker** – containerization
* **Render / Streamlit Cloud** – deployment

---

## 🧩 Architecture Overview

```
Streamlit UI  →  FastAPI API  →  Feature Engineering  →  ML Model
                               ↓
                        Explainability + Risk Logic
```

* Frontend and backend are **fully decoupled**
* Feature engineering is reused during **training & inference**
* Logging is handled centrally

---

## 📊 Model Details

* Trained on **Telco Customer Churn Dataset**
* Outputs:

  * `churn_probability`
  * `risk_level` (Low / Medium / High)
  * `top_reasons` for churn

---

## ▶️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/ShaiviSri04/customer-churn.git
cd customer-churn
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start Backend (FastAPI)

```bash
uvicorn api.app:app --reload --port 8000
```

Check:

```
http://127.0.0.1:8000/health
```

### 5. Start Frontend (Streamlit)

```bash
streamlit run streamlit_app/app.py
```

---

## 🔗 API Endpoints

| Endpoint   | Method | Description          |
| ---------- | ------ | -------------------- |
| `/health`  | GET    | Service health check |
| `/predict` | POST   | Churn prediction     |

---

## 🐳 Docker (Backend)

```bash
docker build -t churn-api .
docker run -p 8000:8000 churn-api
```

---

## 🌐 Deployment

* **Backend**: Render (Dockerized FastAPI)
* **Frontend**: Streamlit Cloud
* Cold start may cause slight delay on first request

Just say the word 💙
