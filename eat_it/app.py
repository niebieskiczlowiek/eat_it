from flask import Flask, Response, request, jsonify

from eat_it.views import UserView

from eat_it.controllers import AddUserRequest, PutUserRequest, DeleteUserRequest, PatchUserRequest, GetUserRequest
from eat_it.controllers import AddUserController, GetUserController, PutUserController, DeleteUserController, PatchUserController
from eat_it.repositories import UserRepository

app = Flask(__name__)


@app.get("/ping")
def ping():
    return Response(status=501)

# @app.get('/users/<id>')
# def get_users(id) -> Response:
#     return Response(status=501)


# Z pracy domowej:
# @app.get('/users')
# def get_users():
#     repository = UserRepository()
#     controller = GetUserController(repository=repository)
#     try:
#         get_user_request = GetUserRequest()
#         controller.get(request=get_user_request)
#     except NotImplementedError:
#         return Response(status=501)
#     return Response(status=200)

user_view_get = UserView.as_view('user_view_get')
app.add_url_rule('/users', view_func=user_view_get, methods=['GET'])


# @app.post('/users')
# def create_user() -> Response:
#     user = request.json
#     repository = UserRepository()
#     controller = AddUserController(repository=repository)
#     try:
#         add_user_request = AddUserRequest(user=user)
#         controller.add(request=add_user_request)
#     except NotImplementedError:
#         pass
#     return jsonify(user)

user_view_post = UserView.as_view('user_view_post')
app.add_url_rule('/users', view_func=user_view_post, methods=['POST'])
    

# @app.put('/users/<user_id>')
# def update_user(user_id) -> Response:
#     user = request.json
#     repository = UserRepository()
#     controller = PutUserController(repository=repository)
#     try:
#         put_user_request = PutUserRequest(user=user)
#         controller.put(request=put_user_request)
#     except NotImplementedError:
#         pass
#     return jsonify(user)

user_view_put = UserView.as_view('user_view_put')
app.add_url_rule('/users', view_func=user_view_put, methods=['PUT'])

# @app.patch('/users/<user_id>')
# def patch_user(user_id) -> Response:
#     user = request.json
#     repository = UserRepository()
#     controller = PatchUserController(repository=repository)
#     try:
#         patch_user_request = PatchUserRequest(user=user)
#         controller.patch(request=patch_user_request)
#     except NotImplementedError:
#         pass
#     return jsonify(user)

user_view_patch = UserView.as_view('user_view_patch')
app.add_url_rule('/users', view_func=user_view_patch, methods=['PATCH'])

# @app.delete('/users/<user_id>')
# def delete_user(user_id) -> Response:
#     repository = UserRepository()
#     controller = DeleteUserController(repository=repository)
#     try:
#         delete_user_request = DeleteUserRequest(user_id=user_id)
#         controller.delete(request=delete_user_request)
#     except NotImplementedError:
#         return Response(status=501)
#     return Response(status=200)

user_view_delete = UserView.as_view('user_view_delete')
app.add_url_rule('/users', view_func=user_view_delete, methods=['DELETE'])


# @app.get('/users/<id>')
# def get_user(id) -> Response:
#     controller = GetUserController()
#     try:
#         controller.get(id=id)
#     except NotImplementedError:
#         pass
#     return Response(status=501)


# user_view = UserView.as_view('user_view')
# app.add_url_rule('/users', view_func=user_view)