from app import create_app, db
from app.models import User, Company, Candidate, HotTopic, Course, JobPosting, Assessment, CandidateMetric

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db, 
        'User': User, 
        'Company': Company, 
        'Candidate': Candidate,
        'HotTopic': HotTopic,
        'Course': Course,
        'JobPosting': JobPosting,
        'Assessment': Assessment,
        'CandidateMetric': CandidateMetric
    }

if __name__ == '__main__':
    app.run(debug=True, port=5000)
