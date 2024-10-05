import sqlite3

def create_db():
    conn = sqlite3.connect('job_recommendation.db')
    c = conn.cursor()

    # Create table for storing user profiles
    c.execute('''CREATE TABLE IF NOT EXISTS user_profiles
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  skills TEXT,
                  experience_level TEXT,
                  desired_roles TEXT,
                  locations TEXT,
                  job_type TEXT)''')

    # Create table for storing job postings
    c.execute('''CREATE TABLE IF NOT EXISTS job_postings
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  job_title TEXT,
                  company TEXT,
                  required_skills TEXT,
                  location TEXT,
                  job_type TEXT,
                  experience_level TEXT)''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_db()
