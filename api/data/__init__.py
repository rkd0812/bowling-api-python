from ..models.user import User

users = {'users': [
    User('001', 'John', 'password', 'test1@email.com').to_dictionary(),
    User('002', 'marry', 'password', 'test1@email.com').to_dictionary(),
    User('003', 'Tom', 'password', 'test1@email.com').to_dictionary(),
    User('004', 'Jane', 'password', 'test1@email.com').to_dictionary()
]}
