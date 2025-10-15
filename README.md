# Smart Resume Screener

This project is a backend application that intelligently parses resumes, extracts key information like skills and experience, and matches them against a job description using a Large Language Model (LLM).

## [cite_start]Objective [cite: 2, 3]
To streamline the initial recruitment process by automatically screening and scoring candidates based on their resume's relevance to a specific job opening.

## Architecture

The application is built with a simple, robust architecture:

-   [cite_start]**Backend API**: A Python Flask server that exposes endpoints to upload resumes and retrieve shortlisted candidates.
-   [cite_start]**Resume Parser**: A utility module (`PyMuPDF`) that extracts raw text from `.pdf` and `.txt` files[cite: 6].
-   [cite_start]**LLM Integration**: A handler that communicates with an external LLM (e.g., OpenAI's GPT) to perform the semantic analysis, scoring, and justification.
-   [cite_start]**Database**: An SQLite database managed by Flask-SQLAlchemy to store the results of each screening, including the score, justification, and extracted skills.

## [cite_start]LLM Prompt 

[cite_start]The core of the analysis is driven by the following prompt structure sent to the LLM[cite: 16]: