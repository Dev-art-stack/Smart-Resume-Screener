import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure the Gemini API client
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_llm_analysis(resume_text, job_description):
    """
    Compares resume and job description using Gemini and returns a structured analysis.
    """
    # This is the high-quality prompt for the LLM, updated for decimal scores
    prompt = f"""
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
    - "match_score": A float from 1.0 to 10.0, allowing for one decimal place for more accuracy.
    - "justification": A 2-3 sentence explanation for the score, highlighting strengths and weaknesses.
    - "extracted_skills": A list of key skills (as strings) from the resume relevant to the job.
    """

    try:
        # Use a stable and capable model
        model = genai.GenerativeModel('models/gemini-pro-latest')

        # Configure the model to output JSON
        generation_config = genai.GenerationConfig(response_mime_type="application/json")

        # Get the response from the API
        response = model.generate_content(prompt, generation_config=generation_config)

        # The API returns a string, so we parse it into a Python dictionary
        analysis_json = json.loads(response.text)
        return analysis_json

    except Exception as e:
        print(f"Error communicating with LLM: {e}")
        return None

