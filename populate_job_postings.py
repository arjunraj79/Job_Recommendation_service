from models import insert_job_posting

# Sample job postings data (you can expand this list with more job postings)
job_postings = [
  {
    "job_title": "Software Engineer",
    "company": "Tech Solutions Inc.",
    "required_skills": ["JavaScript", "React", "Node.js"],
    "location": "San Francisco",
    "job_type": "Full-Time",
    "experience_level": "Intermediate"
  },
  {
    "job_title": "Data Scientist",
    "company": "Data Analytics Corp.",
    "required_skills": ["Python", "Data Analysis", "Machine Learning"],
    "location": "Remote",
    "job_type": "Full-Time",
    "experience_level": "Intermediate"
  },
  {
    "job_title": "Frontend Developer",
    "company": "Creative Designs LLC",
    "required_skills": ["HTML", "CSS", "JavaScript", "Vue.js"],
    "location": "New York",
    "job_type": "Part-Time",
    "experience_level": "Junior"
  },
  # Add other job postings here from the provided mock data...
]

# Insert job postings into the database
for job in job_postings:
    insert_job_posting(job)

print("Job postings have been successfully added to the database.")
