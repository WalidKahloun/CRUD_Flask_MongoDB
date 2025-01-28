from flask import request, jsonify
from dto.user import User

class CrudUserService:

    @staticmethod
    def create_user_service():
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400

        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        if not username or not email or not password:
            return jsonify({"error": "Missing required fields"}), 400

        if User.objects(username=username).first():
            return jsonify({"error": "Username already exists"}), 409

        user = User(username=username, email=email, password=password)
        user.save()
        return jsonify({"message": "User created successfully"}), 201

    @staticmethod
    def delete_user_service(username):
        user = User.objects(username=username).first()
        if not user:
            return jsonify({"error": "User not found"}), 404

        user.delete()
        return jsonify({"message": "User deleted successfully"}), 200

    @staticmethod
    def fetch_read_users():
        users = list(User.objects().only("username", "email", "role"))
        return jsonify(users), 200

    @staticmethod
    def fetch_read_user(username):
        user = User.objects(username=username).only("username", "email", "role").first()
        if not user:
            return jsonify({"error": "User not found"}), 404
        return jsonify(user), 200

    @staticmethod
    def update_user_service(username):
        user = User.objects(username=username).first()
        if not user:
            return jsonify({"error": "User not found"}), 404

        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400

        user.update(**data)
        return jsonify({"message": "User updated successfully"}), 200

crud_user_service = CrudUserService()
