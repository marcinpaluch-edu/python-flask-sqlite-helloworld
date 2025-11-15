from flask import Blueprint, request, jsonify
from app.services.auth_service import create_user
from app.models.user import User

user_bp = Blueprint("user_bp", __name__)

# Root route for quick testing
@user_bp.route("/hello", methods=["GET"])
def hello_world():
    return jsonify({"message": "Hello from Flask! Your app is running 🚀"})

@user_bp.route("/", methods=["POST"])
def add_user():
    data = request.get_json()
    user = create_user(data["username"], data["email"])
    return jsonify({"id": user.id, "username": user.username, "email": user.email})

@user_bp.route("/", methods=["GET"])
def list_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "username": u.username, "email": u.email} for u in users])