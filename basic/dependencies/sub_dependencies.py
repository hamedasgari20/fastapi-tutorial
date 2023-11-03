from typing import Annotated

from fastapi import APIRouter, Depends, Cookie

router = APIRouter(prefix='/sub_dependencies')


def query_extractor(q: str | None = None):
    """
    Extracts the query string from the request.

    Args:
        q (str | None): The query string.

    Returns:
        str | None: The query string.
    """
    return q


def query_or_cookie_extractor(
        q: Annotated[str, Depends(query_extractor)],
        last_query: Annotated[str | None, Cookie()] = None,
):
    """
    Extracts the query string from the request or the last query string from the cookie.

    Args:
        q (str): The query string.
        last_query (str | None): The last query string from the cookie.

    Returns:
        str | None: The query string.
    """
    if not q:
        return last_query
    return q


@router.get("/items/")
async def read_query(
        query_or_default: Annotated[str, Depends(query_or_cookie_extractor)]
):
    """
    Reads the query string from the request or the last query string from the cookie.

    Args:
        query_or_default (str): The query string.

    Returns:
        dict: A dictionary containing the query string.
    """
    return {"q_or_cookie": query_or_default}
