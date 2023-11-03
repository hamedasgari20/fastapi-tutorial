from typing import Annotated

from fastapi import APIRouter, Header, HTTPException, Depends

router = APIRouter(prefix='/dependencies_as_decorator')


async def verify_token(x_token: Annotated[str, Header()]):
    """
    Verifies the X-Token header.

    Args:
        x_token (str): The X-Token header.

    Raises:
        HTTPException: If the X-Token header is invalid.
    """
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: Annotated[str, Header()]):
    """
    Verifies the X-Key header.

    Args:
        x_key (str): The X-Key header.

    Raises:
        HTTPException: If the X-Key header is invalid.

    Returns:
        str: The X-Key header.
    """
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


@router.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items_with_some_decorator():
    """
    Reads items with some decorator it first checks two headers in request.

    Returns:
        list: A list of items if headers are provided correctly.
    """
    return [{"item": "Foo"}, {"item": "Bar"}]
