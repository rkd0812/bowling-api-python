# initial routes
from .user import UsersApi, UserApi, UserAddApi


def init_routes(api):
    api.add_resource(UsersApi, '/users')
    api.add_resource(UserApi, '/user/<int:user_id>')
    api.add_resource(UserAddApi, '/user')
