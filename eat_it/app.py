from flask import Flask, Response, request, jsonify

from eat_it.controllers import AddUserController, AddUserRequest, GetUserRequest, GetUserController, PutUserRequest, PutUserController
from eat_it.repositories import UserRepository

app = Flask(__name__)


@app.get("/ping")
def ping():
    return Response(status=501)

# @app.get('/users/<id>')
# def get_users(id) -> Response:
#     return Response(status=501)


# Z pracy domowej:
@app.get('/users')
def get_users():
    repository = UserRepository()
    controller = GetUserController(repository=repository)
    get_user_request = GetUserRequest()
    controller.get(request=get_user_request)
    return Response(status=501)


@app.post('/users')
def create_user() -> Response:
    user = request.json
    repository = UserRepository()
    controller = AddUserController(repository=repository)
    add_user_request = AddUserRequest(user=user)
    controller.add(request=add_user_request)
    return jsonify(user)

@app.put('/users/<user_id>')
def update_user(user_id) -> Response:
    user = request.json
    repository = UserRepository()
    controller = PutUserController(repository=repository)
    put_user_request = PutUserRequest(user=user)
    controller.put(request=put_user_request)
    return jsonify(user)


@app.patch('/users/<user_id>')
def patch_user(user_id) -> Response:
    user = request.json
    return Response(status=200), jsonify(user)


@app.delete('/users/<user_id>')
def delete_user(user_id) -> Response:
    return Response(status=204)