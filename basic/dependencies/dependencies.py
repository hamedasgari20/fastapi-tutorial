from typing import Annotated

from fastapi import APIRouter, Depends

router = APIRouter(prefix='/dependencies')


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    """
    Define common query parameters for multiple endpoints.

    :param q: A search query string.
    :param skip: The number of items to skip.
    :param limit: The maximum number of items to return.
    :return: A dictionary containing the common query parameters.
    """
    return {"q": q, "skip": skip, "limit": limit}


@router.get("/items/")
async def read_items_with_depends(commons: Annotated[dict, Depends(common_parameters)]):
    """
    Get a list of items with common query parameters.

    :param commons: The common query parameters.
    :return: A dictionary containing the common query parameters.
    """
    return commons


@router.get("/users/")
async def read_users_with_depends(commons: Annotated[dict, Depends(common_parameters)]):
    """
    Get a list of users with common query parameters.

    :param commons: The common query parameters.
    :return: A dictionary containing the common query parameters.
    """
    return commons
