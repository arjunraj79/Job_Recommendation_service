# Job Recommendation Backend Service

## Objective
This project is a backend service designed to recommend job postings to users based on their profiles. It accepts user profiles as input and returns relevant job recommendations based on skills, experience level, and job preferences. The system uses an SQLite database to store job postings and user profiles.

---

## Features
- **RESTful API**: The backend service exposes an API to input user data and return job recommendations.
- **Recommendation Algorithm**: A simple rule-based algorithm matches job postings with user profiles based on skills, location, job type, and experience level.
- **Database**: Uses an SQLite database to store user profiles and job postings.
- **Error Handling**: Robust error handling for API requests and database operations.

---

## Technologies Used
- **Programming Language**: Python
- **Framework**: Flask (or FastAPI, Django, etc.)
- **Database**: SQLite
- **API Testing**: Postman / cURL
- **Development Environment**: Visual Studio Code

---

## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/job-recommendation-service.git
cd job-recommendation-service
```
### 2. Install Dependencies
```bash
Copy code
pip install -r requirements.txt
```
### 3. Initialize the Database
Run the script to set up the database:

```bash
Copy code
python init_db.py
```
### 4. Populate the Database
Add the job postings to the database:

```bash
Copy code
python populate_job_postings.py
```
### 5. Start the API Server
Run the server using:

```bash
Copy code
python app.py
```
The API will now be running at http://127.0.0.1:5000/.

## API Endpoints
### 1. Get Job Recommendations
Endpoint: /recommendations

Method: POST

Request Body (Example):

json
Copy code
{
  "name": "John Doe",
  "skills": ["Python", "Django", "REST APIs"],
  "experience_level": "Intermediate",
  "preferences": {
    "desired_roles": ["Backend Developer", "Software Engineer"],
    "locations": ["Remote", "New York"],
    "job_type": "Full-Time"
  }
}
Response (Example):

json
Copy code
[
  {
    "job_title": "Backend Developer",
    "company": "Tech Solutions Inc.",
    "location": "Remote",
    "job_type": "Full-Time",
    "required_skills": ["Python", "Django", "REST APIs"],
    "experience_level": "Intermediate"
  },
  {
    "job_title": "Software Engineer",
    "company": "Innovative Tech Corp.",
    "location": "New York",
    "job_type": "Full-Time",
    "required_skills": ["Python", "Microservices", "SQL"],
    "experience_level": "Intermediate"
  }
]

## Challenges Faced
### Matching Logic: 
Fine-tuning the recommendation algorithm to balance between skills, experience level, and location preferences.
## Error Handling: 
Ensuring all API inputs are validated and handling missing or incorrect data appropriately.
