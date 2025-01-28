from flask import Flask
from mongoengine import connect
from controllers.user_controller import user_blueprint

app = Flask(__name__)

# Connect to MongoDB manually
connect(db="mydatabase", host="localhost", port=27017)

# Register blueprints
app.register_blueprint(user_blueprint, url_prefix="/user")

if __name__ == "__main__":
    app.run(debug=True)
