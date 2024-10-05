from flask import Flask, request, jsonify
from models import insert_user_profile, insert_job_posting
from recommendation import get_job_recommendations

app = Flask(__name__)

# API to accept user profile data
@app.route('/api/user_profile', methods=['POST'])
def add_user_profile():
    user_data = request.get_json()
    insert_user_profile(user_data)
    return jsonify({"message": "User profile added successfully"}), 201

# API to get job recommendations for a user
@app.route('/api/recommendations', methods=['POST'])
def recommend_jobs():
    user_data = request.get_json()
    recommendations = get_job_recommendations(user_data)
    return jsonify(recommendations), 200

if __name__ == '__main__':
    app.run(debug=True)
