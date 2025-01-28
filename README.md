# CRUD_Flask_MongoDB
Microservice Architecture for User CRUD in Flask and MongoDB
In this project, we are implementing a Microservice Architecture for managing User CRUD (Create, Read, Update, Delete) operations using Flask (Python framework) and MongoDB (NoSQL database). The application allows the creation, management, and retrieval of user data, all while adhering to microservice principles.

Key Components:
Microservice Architecture:

Microservices are independent, loosely coupled services that can communicate over the network (usually through HTTP or messaging protocols). Each service in the microservice architecture focuses on a single responsibility and can be developed, deployed, and scaled independently.
In this context, the User CRUD service is a standalone microservice responsible for managing user data. It handles tasks such as creating new users, retrieving user data, updating user information, and deleting users.
Flask as the Web Framework:

Flask is a lightweight and flexible Python web framework used for building APIs. It's chosen here due to its simplicity and speed for prototyping web services.
Flask allows the definition of routes and the management of HTTP requests (GET, POST, PUT, DELETE), which is ideal for implementing a RESTful API.
MongoDB as the Database:

MongoDB is a NoSQL database used for storing user data in a document-oriented format. It allows flexible and scalable storage, making it an excellent choice for microservices where the data model might evolve over time.
MongoEngine is used as the ODM (Object-Document Mapper) for MongoDB in Flask, which provides a simple interface to interact with MongoDB from Python code.
CRUD Operations:

Create: A service endpoint to add new users to the system.
Read: A service endpoint to fetch users based on certain parameters (e.g., username, user ID).
Update: A service endpoint to modify user details such as their username, email, or role.
Delete: A service endpoint to remove a user from the system.
