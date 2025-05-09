import unittest

from flask import Flask, request, jsonify #Import necessary modules

from app.models import User # Assuming you have a User model

class TestAuthRoutes(unittest.TestCase):

    #Setup method to create a test app instance

    def setUp(self):

        self.app = Flask(__name__)

        #Register your auth routes here (replace with your actual routes)

        #Example:

        #@self.app.route('/login', methods=['POST'])

        #def login():

        #    pass

        self.client = self.app.test_client()

    def test_login(self):

        # Add your test logic here.  Example using the test client:

        response = self.client.post('/login', json={'username': 'testuser', 'password': 'password'}) #Replace with your login endpoint and data

        self.assertEqual(response.status_code, 200) # Or the expected status code

    # Add more tests for other auth routes

    def tearDown(self):

        pass #Clean up if needed

if __name__ == '__main__':

    unittest.main()

from flask import Blueprint, request, jsonify
from app.models import User
from app import db
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"error": "Username already exists"}), 400

    user = User(username=data["username"])
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data["username"]).first()
    if user and user.check_password(data["password"]):
        access_token = create_access_token(identity=user.id)
        return jsonify({"access_token": access_token}), 200
    return jsonify({"error": "Invalid username or password"}), 401