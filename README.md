#User CRUD Microservice
Overview
This project is a Microservice built using Flask and MongoDB to provide CRUD (Create, Read, Update, Delete) operations for managing users. It is designed to handle user management tasks in a microservice-oriented environment, using MongoDB as the data store for user data. This microservice is lightweight, scalable, and can be easily integrated with other services in a larger application.

Features
Create a User: Add a new user with a unique username, email, and role.
Read User: Fetch a user’s details by username.
Update User: Update an existing user’s details such as email, role, etc.
Delete User: Remove a user by username.
MongoDB Integration: Data is stored in MongoDB, a NoSQL database.
Technologies Used
Flask: A Python micro web framework for building web APIs.
MongoDB: A NoSQL database for flexible data storage.
MongoEngine: An ODM (Object-Document Mapper) for MongoDB, allowing Flask to interact with MongoDB in an object-oriented way.
Getting Started
Prerequisites
Python 3.x
MongoDB instance running locally or on a cloud provider like MongoDB Atlas
Postman (or any API testing tool)
Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/CRUD_Flask_MongoDB.git
cd CRUD_Flask_MongoDB
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Ensure that MongoDB is running on your local machine or you have connected to a cloud instance (e.g., MongoDB Atlas).

Run the Flask application:

bash
Copy
Edit
python app.py
This will start the service, and it will be available at http://127.0.0.1:5000.

API Endpoints
1. Create User
URL: /create
Method: POST
Request Body:
json
Copy
Edit
{
  "username": "john_doe",
  "email": "john.doe@example.com",
  "role": "user"
}
Response: Returns the newly created user object with a success status.
2. Read User
URL: /read/{username}
Method: GET
URL Params:
username: The username of the user to retrieve.
Response: Returns user data if found or a 404 error if the user is not found.
3. Update User
URL: /update/{username}
Method: PUT
Request Body:
json
Copy
Edit
{
  "email": "new.email@example.com",
  "role": "admin"
}
URL Params:
username: The username of the user to update.
Response: Returns the updated user object.
4. Delete User
URL: /delete/{username}
Method: DELETE
URL Params:
username: The username of the user to delete.
Response: Returns a success message or an error if the user is not found.
File Structure
Here's the updated file structure for your project without the models directory:

bash
Copy
Edit
├── app.py                 # Main application entry point, defines the User model and routes
├── controllers/           # Contains route handlers for User CRUD operations
│   └── user_controller.py
├── services/              # Contains business logic for User CRUD
│   └── crud_user_service.py
├── dto/                   # Contains Data Transfer Objects (DTOs)
│   └── user.py
├── requirements.txt       # List of required Python dependencies
├── README.md              # This README file
└── .gitignore             # Git ignore file
Model Definition in app.py:
Since you don’t have a models/ folder, you can define your User model directly in app.py. Here’s an example:

python
Copy
Edit
from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'userdb',
    'host': 'localhost',
    'port': 27017
}

db = MongoEngine(app)

# Define the User model
class User(db.Document):
    username = db.StringField(required=True, unique=True)
    email = db.StringField(required=True, unique=True)
    role = db.StringField(default="user")
    is_active = db.BooleanField(default=True)

    def to_json(self):
        return {
            "username": self.username,
            "email": self.email,
            "role": self.role,
            "is_active": self.is_active
        }
In the above code, User is the model used to represent user data. This model includes fields like username, email, role, and is_active.

Running the Application
Make sure MongoDB is up and running either locally or on a cloud provider (e.g., MongoDB Atlas).

Run the Flask app:

bash
Copy
Edit
python app.py
The app should now be running at http://127.0.0.1:5000.

Use Postman or any API testing tool to make requests to the endpoints mentioned above.

Contributing
Contributions are welcome! If you encounter any issues or would like to suggest improvements, feel free to create an issue or submit a pull request.
