from flask import Blueprint, jsonify
from services.crud_user_service import crud_user_service
from dto.user import User

user_blueprint = Blueprint('user', __name__)

# Create a new user
@user_blueprint.post('/create')
def create_user():
    user_created = crud_user_service.create_user_service()
    return user_created

# Delete a user by username
@user_blueprint.delete('/delete/<username>')
def delete_user(username):
    delete_result = crud_user_service.delete_user_service(username)
    return delete_result

# Fetch all users
@user_blueprint.get('/read')
def get_users():
    users = User.objects()  # Fetch all users
    # Convert the User objects to a list of JSON serializable dictionaries
    users_json = [user.to_json() for user in users]
    return jsonify(users_json)

# Fetch a user by username
@user_blueprint.get('/read/<username>')
def get_user(username):
    user = User.objects(username=username).first()
    
    if user:
        return jsonify(user.to_json())  # Convert to JSON-serializable dictionary
    else:
        return jsonify({'error': 'User not found'}), 404

# Update a user by username
@user_blueprint.put('/update/<username>')
def update_user(username):
    update_result = crud_user_service.update_user_service(username)
    return update_result
