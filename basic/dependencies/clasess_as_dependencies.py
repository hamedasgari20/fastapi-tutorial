from typing import Annotated

from fastapi import APIRouter, Depends

router = APIRouter(prefix='/clasess_as_dependencies')


class CommonQueryParams:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@router.get("/items/")
async def read_items_with_class_depends(commons: Annotated[CommonQueryParams, Depends()]):
    """
    Returns the common query parameters for items.

    Parameters:
    commons (Annotated[CommonQueryParams, Depends()]): The common query parameters for items.

    Returns:
    The common query parameters for items.
    """
    return commons


@router.get("/users/")
async def read_users_with_class_depends(commons: Annotated[CommonQueryParams, Depends()]):
    """
    Returns the common query parameters for users.

    Parameters:
    commons (Annotated[CommonQueryParams, Depends()]): The common query parameters for users.

    Returns:
    The common query parameters for users.
    """
    return commons
