from typing import Annotated

from fastapi import APIRouter, Header

router = APIRouter(prefix='/header_parameter')


@router.get("/items_a/")
async def header_parameter(user_agent: Annotated[str | None, Header()] = None):
    """
    Get items with an optional User-Agent header.

    :param user_agent: The User-Agent header value.
    :return: A dictionary containing the User-Agent header value.
    """
    return {"User-Agent": user_agent}


@router.get("/items_b/")
async def duplicate_header_parameters(x_token: Annotated[list[str] | None, Header()] = None):
    """
    Get items with an optional list of X-Token headers.

    :param x_token: A list of X-Token header values.
    :return: A dictionary containing the X-Token header values.
    """
    return {"X-Token values": x_token}
