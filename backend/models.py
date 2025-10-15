import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class JobDescription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, unique=True)
    description_text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    # This relationship ensures that when a job description is deleted,
    # all candidates associated with it are also deleted automatically.
    candidates = db.relationship('Candidate', backref='job_description', lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description_text': self.description_text,
            'created_at': self.created_at.isoformat()
        }

class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(255), nullable=False)
    job_description_id = db.Column(db.Integer, db.ForeignKey('job_description.id'), nullable=False)
    # Changed from Integer to Float to allow for decimal scores (e.g., 8.5)
    match_score = db.Column(db.Float, nullable=False)
    justification = db.Column(db.Text, nullable=False)
    extracted_skills = db.Column(db.Text, nullable=True)
    resume_text = db.Column(db.Text, nullable=True) # To store the parsed resume
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'file_name': self.file_name,
            'match_score': self.match_score,
            'justification': self.justification,
            'extracted_skills': self.extracted_skills.split(',') if self.extracted_skills else [],
            'created_at': self.created_at.isoformat(),
            'job_title': self.job_description.title if self.job_description else 'N/A'
        }

