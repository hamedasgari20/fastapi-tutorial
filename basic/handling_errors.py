from fastapi import APIRouter, HTTPException, FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse

router = APIRouter(prefix='/handling_errors')
app = FastAPI()


items = {"foo": "The Foo Wrestlers"}


@router.get("/items/{item_id}")
async def handling_errors(item_id: str):
    """
    Get an item with the given ID.

    :param item_id: The ID of the item to get.
    :return: A dictionary containing the item data.
    :raises HTTPException: If the item with the given ID is not found.
    """
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}


@router.get("/items-header/{item_id}")
async def handling_errors_with_custom_header(item_id: str):
    """
    Get an item with the given ID, including a custom error header.

    :param item_id: The ID of the item to get.
    :return: A dictionary containing the item data.
    :raises HTTPException with custom header: If the item with the given ID is not found.
    """
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": "There goes my error"},
        )
    return {"item": items[item_id]}

