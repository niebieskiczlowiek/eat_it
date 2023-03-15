from dataclasses import dataclass
from eat_it.repositories import UserRepository

@dataclass
class AddUserRequest:
    user: dict

class AddUserController:
    def __init__(self, repository: UserRepository):
        pass

    def add(self, request: AddUserRequest) -> None:
        print(request.user)


@dataclass
class GetUserRequest:
    pass


class GetUserController:
    def __init__(self, repository: UserRepository):
        pass

    def get(self, request: GetUserRequest) -> None:
        print(request)


@dataclass
class PutUserRequest:
    user: dict


class PutUserController:
    def __init__(self, repository: UserRepository):
        pass

    def put(self, request: PutUserRequest) -> None:
        print(request)