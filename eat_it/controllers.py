from dataclasses import dataclass
from eat_it.repositories import UserRepository

@dataclass
class GetUserRequest:
    pass

@dataclass
class AddUserRequest:
    user: dict
@dataclass
class PutUserRequest:
    user: dict

@dataclass
class DeleteUserRequest:
    user_id: int

@dataclass 
class PatchUserRequest:
    user: dict

class GetUserController:
    def get(self, request: GetUserRequest) -> None:
        raise NotImplementedError()


class AddUserController:
    def __init__(self, repository: UserRepository):
        pass

    def add(self, request: AddUserRequest) -> None:
        raise NotImplementedError()


class PutUserController:
    def __init__(self, repository: UserRepository):
        pass

    def put(self, request: PutUserRequest) -> None:
        print(request)


class DeleteUserController:
    def delete(self, request: DeleteUserRequest) -> None:
        raise NotImplementedError()


class PatchUserController:
    def __init__(self, repository: UserRepository):
        pass

    def patch(self, request: PatchUserRequest) -> None:
        raise NotImplementedError()