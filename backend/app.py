import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
from models import db, Candidate, JobDescription
from parser import extract_text_from_file
from llm_handler import get_llm_analysis

# --- Configuration ---
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'uploads')
ALLOWED_EXTENSIONS = {'txt', 'pdf'}

# --- Create Flask App ---
app = Flask(__name__)

# --- Absolute Path Database Configuration (THE FIX) ---
# Get the absolute path of the directory where app.py is located
basedir = os.path.abspath(os.path.dirname(__file__))
# Configure the app to use an absolute path for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'resumes.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# --- Initialize Extensions ---
CORS(app)  # Enable Cross-Origin Resource Sharing
db.init_app(app)

with app.app_context():
    db.create_all()

# --- Helper Function ---
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# --- API Endpoints ---

# == Job Description Endpoints ==
@app.route('/job-descriptions', methods=['POST'])
def add_job_description():
    data = request.get_json()
    if not data or 'title' not in data or 'description_text' not in data:
        return jsonify({"error": "Missing title or description_text"}), 400
    
    if JobDescription.query.filter_by(title=data['title']).first():
        return jsonify({"error": "A job description with this title already exists."}), 409

    new_job = JobDescription(title=data['title'], description_text=data['description_text'])
    db.session.add(new_job)
    db.session.commit()
    return jsonify(new_job.to_dict()), 201

@app.route('/job-descriptions', methods=['GET'])
def get_job_descriptions():
    jobs = JobDescription.query.order_by(JobDescription.created_at.desc()).all()
    return jsonify([job.to_dict() for job in jobs]), 200

@app.route('/job-descriptions/<int:job_id>', methods=['DELETE'])
def delete_job_description(job_id):
    job_to_delete = JobDescription.query.get(job_id)
    if not job_to_delete:
        return jsonify({"error": "Job description not found"}), 404
    
    db.session.delete(job_to_delete)
    db.session.commit()
    return jsonify({"message": "Job description and associated candidates deleted successfully"}), 200

# == Candidate Endpoints ==
@app.route('/screen', methods=['POST'])
def screen_resume():
    if 'resume' not in request.files:
        return jsonify({"error": "No resume file part"}), 400
    
    file = request.files['resume']
    job_description_id = request.form.get('job_description_id')

    if file.filename == '' or not job_description_id:
        return jsonify({"error": "Missing resume file or job description ID"}), 400

    job_description = JobDescription.query.get(job_description_id)
    if not job_description:
        return jsonify({"error": "Job description not found"}), 404

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        file.save(filepath)

        resume_text = extract_text_from_file(filepath, filename)
        if not resume_text:
            return jsonify({"error": "Could not extract text from file"}), 500

        analysis = get_llm_analysis(resume_text, job_description.description_text)
        if not analysis:
            return jsonify({"error": "Failed to get analysis from LLM"}), 500

        try:
            candidate = Candidate(
                file_name=filename,
                job_description_id=job_description.id,
                match_score=analysis.get('match_score'),
                justification=analysis.get('justification'),
                extracted_skills=",".join(analysis.get('extracted_skills', [])),
                resume_text=resume_text
            )
            db.session.add(candidate)
            db.session.commit()
            return jsonify(candidate.to_dict()), 201
        
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": f"Database error: {e}"}), 500
    else:
        return jsonify({"error": "File type not allowed"}), 400

@app.route('/candidates', methods=['GET'])
def get_shortlisted_candidates():
    job_id = request.args.get('job_id')
    query = Candidate.query

    if job_id:
        query = query.filter_by(job_description_id=job_id)
    
    # Sort by creation date descending to show the newest first
    candidates = query.order_by(Candidate.created_at.desc()).all()
    
    return jsonify([c.to_dict() for c in candidates]), 200

@app.route('/candidates/<int:candidate_id>', methods=['DELETE'])
def delete_candidate(candidate_id):
    candidate_to_delete = Candidate.query.get(candidate_id)
    if not candidate_to_delete:
        return jsonify({"error": "Candidate not found"}), 404
    
    db.session.delete(candidate_to_delete)
    db.session.commit()
    return jsonify({"message": "Candidate deleted successfully"}), 200

# == File Download Endpoint ==
@app.route('/uploads/<path:filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True, port=5001)

