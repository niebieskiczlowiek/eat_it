import pytest
from flask.views import MethodView
from flask.wrappers import Response

from eat_it.views import UserView

from eat_it.repositories import UserRepository
from eat_it.controllers import GetUserController

@pytest.fixture
def view() -> UserView:
    return UserView( 
        controller=GetUserController(
            repository=UserRepository()
            ) 
        )

def test_user_view_returns_501_on_get_method(view: UserView) -> None:
    actual = view.get(
        id='1'
    )
    assert actual.status_code == 501
    
def test_user_view_returns_response_on_get_method(view: UserView) -> None:
    actual = view.get(
        id='1'
    )
    assert isinstance(actual, Response)

def test_user_view_is_subclass_method_view(view: UserView) -> None:
    assert isinstance(view, MethodView)


def test_user_view_returns_501_on_post_method(view: UserView) -> None:
    actual = view.post(
        id='1'
    )
    assert actual.status_code == 501

def test_user_view_returns_response_on_put_method(view: UserView) -> None:
    actual = view.put(
        id='1'
    )
    assert isinstance(actual, Response)

def test_user_view_returns_501_on_patch_method(view: UserView) -> None:
    actual = view.patch(
        id='1'
    )
    assert actual.status_code == 501

def test_user_view_returns_response_on_delete_method(view: UserView) -> None:
    actual = view.delete(
        id='1'
    )
    assert isinstance(actual, Response)

