
# 🧠 Smart Resume Screener

An intelligent, full-stack AI-powered application that automates resume screening by comparing resumes against job descriptions using Google Gemini API. It extracts relevant skills, generates a match score, and provides clear justifications—all within a clean, responsive dashboard.

---

## 🚀 Features

- 🤖 **AI-Powered Screening:** Uses Google Gemini API for contextual resume-to-JD matching.  
- 📄 **Resume Parsing:** Extracts text from PDF/TXT resumes via PyMuPDF.  
- 🧩 **Skill Extraction:** Identifies relevant technical and soft skills.  
- 📊 **Score & Justification:** Provides match score (1.0–10.0) and 2–3 sentence reasoning.  
- 🗃️ **Job Description Management:** Add, delete, and view job roles dynamically.  
- 👤 **Candidate Management:** Upload, view, filter, and delete candidates.  
- 🖥️ **Responsive Frontend:** Built with Tailwind CSS + Vanilla JavaScript.  
- 💾 **Persistent Storage:** SQLite database using SQLAlchemy ORM.  

---

## 🧰 Tech Stack

| Layer | Technologies |
|-------|---------------|
| **Frontend** | HTML, Tailwind CSS, Vanilla JavaScript (Fetch API) |
| **Backend** | Python (Flask, Flask-SQLAlchemy, Flask-CORS) |
| **Database** | SQLite |
| **AI Model** | Google Gemini API |
| **File Parsing** | PyMuPDF |

---

## 🏗️ System Architecture

**Frontend** → Fetch API → **Flask Backend** → Gemini API → **SQLite Database**

1. The user uploads a resume (PDF/TXT) and selects a job description.  
2. The backend parses the resume and sends both the resume and job description to Gemini API.  
3. The model returns a JSON with:  
   - `match_score`  
   - `justification`  
   - `extracted_skills`  
4. Results are stored in SQLite and displayed on the dashboard.  

---

## 📦 Installation Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Dev-art-stack/Smart-Resume-Screener.git
cd Smart-Resume-Screener
````

### 2️⃣ Backend Setup

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure API Key

Create a `.env` file in the root directory and add:

```bash
GEMINI_API_KEY=your_google_gemini_api_key
```

### 4️⃣ Run Flask Server

```bash
python app.py
```

Then open the app in your browser:

```
http://127.0.0.1:5000
```

---

## 🎥 Demo

📸 https://drive.google.com/file/d/17sPqnIoDSOzsJ7MNU9puDVDPM4EYyvat/view?usp=drive_link
