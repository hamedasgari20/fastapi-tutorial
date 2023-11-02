from typing import Any

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix='/response_model')


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@router.post("/items_a/", response_model=Item)
async def response_model_item(item: Item) -> Any:
    """
    Create a new item with the given data.

    :param item: The data for the new item.
    :return: The created item.
    """
    return item


@router.get("/items_b/", response_model=list[Item])
async def response_model_list() -> Any:
    """
    Get a list of items.

    :return: A list of items.
    """
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}


@router.get("/items_c/{item_id}/name", response_model=Item, response_model_include=["name", "description"])
async def response_model_with_include(item_id: str):
    """
    Get the name and description of an item.

    :param item_id: The ID of the item to get.
    :return: A dictionary containing the name and description of the item.
    """
    return items[item_id]


@router.get("/items_d/{item_id}/public", response_model=Item, response_model_exclude=["tax"])
async def response_model_with_exclude(item_id: str):
    """
    Get a public view of an item, excluding the tax field.

    :param item_id: The ID of the item to get.
    :return: A dictionary containing the public view of the item.
    """
    return items[item_id]
