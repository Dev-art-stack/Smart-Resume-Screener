🤖 Smart Resume Screener
An intelligent, full-stack application designed to streamline the recruitment process by automatically parsing resumes, scoring them against job descriptions using a Large Language Model (LLM), and displaying the results on a clean, modern dashboard.

🎯 Objective
The primary goal of this project is to intelligently parse resumes, extract key skills, and compute a precise match score against a given job description. This automates the initial screening phase, allowing recruiters to focus on the most qualified candidates.

✨ Features
AI-Powered Analysis: Leverages the Google Gemini API to semantically analyze resume content and provide a match score with one decimal place for higher accuracy.

Full Frontend Dashboard: A responsive, single-page application to manage the entire screening process.

Job Description Management:

✅ Add and save new job descriptions.

✅ Filter the candidate list by a specific job.

✅ Delete job descriptions (which also removes associated candidates).

Candidate Management:

✅ Upload resumes in PDF or TXT format.

✅ View justification and extracted skills for each candidate.

✅ Download the original uploaded resume file.

✅ Delete individual candidate profiles.

Persistent Storage: Uses an SQLite database to store all job descriptions and parsed candidate data.

⚙️ Tech Stack
Component

Technology

Backend

Python, Flask, Flask-SQLAlchemy, Flask-CORS, PyMuPDF

Frontend

HTML, Tailwind CSS, Vanilla JavaScript (Fetch API)

LLM API

Google Gemini API

Database

SQLite

🏛️ Architecture
The application is built on a classic client-server model:

Backend: A Python Flask server acts as a REST API. It handles business logic, file processing, database interactions (via SQLAlchemy), and communication with the Google Gemini API.

Frontend: A single index.html file serves as a dynamic, client-side application. It communicates with the backend via asynchronous fetch requests to create, retrieve, and delete data without needing to reload the page.

🧠 LLM Prompt
The core of the analysis is driven by a carefully crafted prompt sent to the Google Gemini API (gemini-pro-latest model). The model is instructed to return a structured JSON object.

You are an expert HR recruitment assistant. Your task is to analyze a candidate's resume against a job description.
Provide a single, valid JSON object as your response, without any markdown formatting like ```json.

**Job Description:**
---
{job_description}
---

**Resume Text:**
---
{resume_text}
---

Based on the comparison, your JSON output must contain these keys:
- "match_score": A floating-point number from 1.0 to 10.0 (1.0=poor fit, 10.0=excellent fit).
- "justification": A 2-3 sentence explanation for the score, highlighting strengths and weaknesses.
- "extracted_skills": A list of key skills (as strings) from the resume relevant to the job.


🚀 Setup and Installation
Follow these steps to run the project locally.

📋 Prerequisites
Python 3.8+

A Google Gemini API Key

VS Code with the Live Server extension

1. Clone the Repository
git clone <your-repo-url>
cd Smart-Resume-Screener


2. Backend Setup 🖥️
Navigate to the backend directory:

cd backend


Create and activate a virtual environment:

# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Set up environment variables:
Create a file named .env in the backend directory and add your Google Gemini API key:

GEMINI_API_KEY="your_google_api_key_here"


Run the Flask Server:

flask run --port=5001


The backend API will now be running at http://127.0.0.1:5001. Keep this terminal open.

3. Frontend Setup 🌐
Open the project's root folder (Smart-Resume-Screener) in VS Code.

Right-click on the index.html file.

Select "Open with Live Server" (or click the "Go Live" button in the status bar).

Your browser will automatically open the dashboard, and the application will be fully functional.

🔗 API Endpoints
Method

Endpoint

Description

POST

/job-descriptions

Adds a new job description.

GET

/job-descriptions

Retrieves all saved job descriptions.

DELETE

/job-descriptions/<job_id>

Deletes a job description and all its candidates.

POST

/screen

Screens a new resume against a job description.

GET

/candidates

Retrieves all candidates (optionally filtered by job).

DELETE

/candidates/<candidate_id>

Deletes a single candidate.

GET

/uploads/<filename>

Downloads the specified resume file.

🎥 Video Demonstration

https://drive.google.com/file/d/17sPqnIoDSOzsJ7MNU9puDVDPM4EYyvat/view?usp=drive_link
