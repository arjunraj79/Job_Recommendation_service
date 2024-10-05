import sqlite3

def insert_user_profile(user_data):
    conn = sqlite3.connect('job_recommendation.db')
    c = conn.cursor()

    # Insert user data into the database
    c.execute('''INSERT INTO user_profiles (name, skills, experience_level, desired_roles, locations, job_type)
                 VALUES (?, ?, ?, ?, ?, ?)''',
              (user_data['name'], ",".join(user_data['skills']), user_data['experience_level'],
               ",".join(user_data['preferences']['desired_roles']),
               ",".join(user_data['preferences']['locations']), user_data['preferences']['job_type']))

    conn.commit()
    conn.close()

def insert_job_posting(job_data):
    conn = sqlite3.connect('job_recommendation.db')
    c = conn.cursor()

    # Insert job posting into the database
    c.execute('''INSERT INTO job_postings (job_title, company, required_skills, location, job_type, experience_level)
                 VALUES (?, ?, ?, ?, ?, ?)''',
              (job_data['job_title'], job_data['company'], ",".join(job_data['required_skills']),
               job_data['location'], job_data['job_type'], job_data['experience_level']))

    conn.commit()
    conn.close()
