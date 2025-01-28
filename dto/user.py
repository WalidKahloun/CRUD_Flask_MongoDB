from mongoengine import Document, StringField, BooleanField

class User(Document):
    username = StringField(required=True)
    email = StringField(required=True)
    password = StringField(required=True)
    role = StringField(default="user")  # Add role field
    is_active = BooleanField(default=True)  # Add is_active field
    
    def to_json(self):
        return {
            "username": self.username,
            "email": self.email,
            "role": self.role,
            "is_active": self.is_active
        }