from typing import Annotated

from fastapi import APIRouter, Form

router = APIRouter(prefix='/form_data')


@router.post("/login/")
async def form_data_required(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    """
    Authenticate a user with the given username and password as a FROM data.

    :param username: The username of the user to authenticate (required).
    :param password: The password of the user to authenticate (required).
    :return: A dictionary containing the username of the authenticated user.
    """
    return {"username": username}
