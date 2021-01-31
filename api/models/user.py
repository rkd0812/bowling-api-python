# User Class

class User:
    def __init__(self, user_id, name, password, email):
        self.user_id = user_id
        self.name = name
        self.password = password
        self.email = email

    def to_dictionary(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email
        }
