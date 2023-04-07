from flask import Response
from flask.views import MethodView

from eat_it.controllers import GetUserController, AddUserController, PutUserController, PatchUserController, DeleteUserController

class UserView(MethodView):
    def __init__(self, controller) -> None:
        self._get_user_controller = controller

    def get(self, id: str) -> Response:
        return Response(status=501)
    
    def post(self, id: str) -> Response:
        return Response(status=501)
    
    def put(self, id: str) -> Response:
        return Response(status=501)
    
    def patch(self, id: str) -> Response:
        return Response(status=501)
    
    def delete(self, id: str) -> Response:
        return Response(status=501)