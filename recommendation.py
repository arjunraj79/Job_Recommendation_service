import sqlite3

def get_job_recommendations(user_data):
    conn = sqlite3.connect('job_recommendation.db')
    c = conn.cursor()

    # Extract user preferences
    user_skills = set(user_data['skills'])
    experience_level = user_data['experience_level']
    desired_roles = set(user_data['preferences']['desired_roles'])
    locations = set(user_data['preferences']['locations'])
    job_type = user_data['preferences']['job_type']

    # Query job postings that match the user's profile
    c.execute('''SELECT job_title, company, required_skills, location, job_type, experience_level
                 FROM job_postings
                 WHERE experience_level = ?
                 AND job_type = ?''', (experience_level, job_type))

    job_postings = c.fetchall()
    recommended_jobs = []

    # Match jobs based on user skills, desired roles, and location
    for job in job_postings:
        job_skills = set(job[2].split(','))
        job_location = job[3]
        job_title = job[0]

        # Check if user's skills and desired roles match the job posting
        if user_skills.intersection(job_skills) and job_title in desired_roles and job_location in locations:
            recommended_jobs.append({
                "job_title": job[0],
                "company": job[1],
                "location": job[3],
                "job_type": job[4],
                "required_skills": job[2],
                "experience_level": job[5]
            })

    conn.close()
    return recommended_jobs
