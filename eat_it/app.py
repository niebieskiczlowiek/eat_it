from flask import Flask, Response, request, jsonify

app = Flask(__name__)


@app.get("/ping")
def ping():
    return Response(status=501)


@app.post('/users')
def create_user() -> Response:
    user = request.json
    return jsonify(user)

@app.get('/users')
def get_users() -> Response:
    return Response(status=501)

@app.post('/users')
def create_user() -> Response:
    user = request.json
    return Response(status=201), jsonify(user)

@app.put('/users/<user_id>')
def update_user(user_id) -> Response:
    user = request.json
    return Response(status=200), jsonify(user)

@app.patch('/users/<user_id>')
def patch_user(user_id) -> Response:
    user = request.json
    return Response(status=200), jsonify(user)

@app.delete('/users/<user_id>')
def delete_user(user_id) -> Response:
    return Response(status=204)