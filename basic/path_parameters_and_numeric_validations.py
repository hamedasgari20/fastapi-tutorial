from typing import Annotated

from fastapi import APIRouter

router = APIRouter(prefix='/path_parameters_and_numeric_validations')

from fastapi import Path


@router.get("/items_a/{item_id}")
async def path_parameter(q: str, item_id: int = Path(title="The ID of the item to get")):
    """
    Get the item with the given ID.

    Args:
        q (str): The query string.
        item_id (int): The ID of the item to get.

    Returns:
        dict: A dictionary containing the item ID and the query string (if provided).
    """
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@router.get("/items_b/{item_id}")
async def path_parameter_with_numeric_validation(
        item_id: Annotated[int, Path(title="The ID of the item to get", ge=5)], q: str
):
    """
    Get the item with the given ID, with numeric validation.

    Args:
        item_id (int): The ID of the item to get, must be greater than or equal to 5.
        q (str): The query string.

    Returns:
        dict: A dictionary containing the item ID and the query string (if provided).
    """
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@router.get("/items_c/{item_id}")
async def path_parameter_with_multi_numeric_validation(
        *,
        item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
        q: str,
):
    """
    Get the item with the given ID, with multiple numeric validations.

    Args:
        item_id (int): The ID of the item to get, must be between 0 and 1000 (inclusive).
        q (str): The query string.

    Returns:
        dict: A dictionary containing the item ID and the query string (if provided).
    """
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

