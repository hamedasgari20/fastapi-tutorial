from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix='/request_body')


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@router.post("/items/")
async def request_body(item: Item):
    """
    Create a new item with the given data.

    Parameters:
    - item (Item): The data for the new item.

    Returns:
    - The data for the new item.

    Raises:
    - None
    """
    return item


@router.post("/items/{item_id}")
async def request_body_and_path_parameter(item_id: int, item: Item):
    """
    Create a new item with the given ID and data.

    Parameters:
    - item_id (int): The ID for the new item.
    - item (Item): The data for the new item.

    Returns:
    - A dictionary containing the ID and data for the new item.

    Raises:
    - None
    """
    return {"item_id": item_id, **item.model_dump()}
