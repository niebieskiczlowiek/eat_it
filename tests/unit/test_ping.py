from app import app, pimg, create_user


UNIMPLEMENTED = 501

def test_ping_returns_501_response() -> None:
    result = app.ping()

    assert result.status_code == UNIMPLEMENTED  


def test_get_users_returns_501_response() -> None:
    result = app.get_users()

    assert result.status_code == UNIMPLEMENTED


def test_create_user_returns_201_response() -> None:
    payload = {"first_name": "Jan", "last_name": "Kowalski"}
    result = app.create_user(payload)

    assert result.status_code == 201

def test_update_user_returns_200_response() -> None:
    payload = {"first_name": "Jan", "last_name": "Kowalski"}
    result = app.update_user(1, payload)

    assert result.status_code == 200


def test_patch_user_returns_200_response() -> None:
    payload = {"first_name": "Jan", "last_name": "Kowalski"}
    result = app.patch_user(1, payload)

    assert result.status_code == 200

def test_delete_user_returns_204_response() -> None:
    result = app.delete_user(1)

    assert result.status_code == 204