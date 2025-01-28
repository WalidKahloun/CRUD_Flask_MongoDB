# User CRUD Microservice

## Overview

This project is a Microservice built using Flask and MongoDB to provide CRUD (Create, Read, Update, Delete) operations for managing users. It is designed to handle user management tasks in a microservice-oriented environment, using MongoDB as the data store for user data. This microservice is lightweight, scalable, and can be easily integrated with other services in a larger application.

## Features

* Create a User: Add a new user with a unique username, email, and role.
* Read User: Fetch a user’s details by username.
* Update User: Update an existing user’s details such as email, role, etc.
* Delete User: Remove a user by username.
* MongoDB Integration: Data is stored in MongoDB, a NoSQL database.

## Technologies Used

* Flask: A Python micro web framework for building web APIs.
* MongoDB: A NoSQL database for flexible data storage.
* MongoEngine: An ODM (Object-Document Mapper) for MongoDB, allowing Flask to interact with MongoDB in an object-oriented way.

## Getting Started

### Prerequisites

* Python 3.x
* MongoDB instance running locally or on a cloud provider like MongoDB Atlas
* Postman (or any API testing tool)

### Installation

1. Clone the repository:

git clone https://github.com/yourusername/CRUD_Flask_MongoDB.git
cd CRUD_Flask_MongoDB

2. Install dependencies:

pip install -r requirements.txt

3. Ensure that MongoDB is running on your local machine or you have connected to a cloud instance (e.g., MongoDB Atlas).

### Run the Flask application:

python app.py

This will start the service, and it will be available at http://127.0.0.1:5000.

## API Endpoints

1. Create User

* URL: /create

* Method: POST

* Request Body:

{
  "username": "john_doe",
  "email": "john.doe@example.com",
  "role": "user"
}

* Response: Returns the newly created user object with a success status.

2. Read User

* URL: /read/{username}
* Method: GET
* URL Params:
  * username: The username of the user to retrieve.
* Response: Returns user data if found or a 404 error if the user is not found.

4. Update User

* URL: /update/{username}
* Method: PUT
* Request Body:

{
  "email": "new.email@example.com",
  "role": "admin"
}

* URL Params:
  * username: The username of the user to update.
* Response: Returns the updated user object.

6. Delete User

* URL: /delete/{username}
* Method: DELETE
* URL Params:
  * username: The username of the user to delete.
* Response: Returns a success message or an error if the user is not found.

## File Structure

Here's the updated file structure for your project without the models directory:

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

## Running the Application

1. Make sure MongoDB is up and running either locally or on a cloud provider (e.g., MongoDB Atlas).

2. Run the Flask app:

python app.py

The app should now be running at http://127.0.0.1:5000.

3. Use Postman or any API testing tool to make requests to the endpoints mentioned above.

## Contributing

Contributions are welcome! If you encounter any issues or would like to suggest improvements, feel free to create an issue or submit a pull request.
