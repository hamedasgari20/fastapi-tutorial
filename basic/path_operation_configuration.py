from fastapi import APIRouter
from pydantic import BaseModel
from starlette import status

router = APIRouter(prefix='/path_operation_configuration')


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


@router.post("/items_a/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def add_status_code_to_response(item: Item):
    """
    Create a new item with the given data and return it with a 201 status code.

    :param item: The data for the new item.
    :return: The created item.
    """
    return item


@router.post("/items_b/", response_model=Item, summary="Add description and summary",
             description="Create an item with all the information, name, description, price, tax and a set of unique tags")
async def add_description_and_summary(item: Item):
    """
    Create a new item with the given data and return it.

    :param item: The data for the new item.
    :return: The created item.
    """
    return item


@router.post("/items_c/", response_model=Item, response_description="Custom description to response")
async def add_description_to_response(item: Item):
    """
    Create a new item with the given data and return it with a custom response description.

    :param item: The data for the new item.
    :return: The created item.
    """
    return item


@router.get("/items_d/", deprecated=True)
async def mark_as_deprecated():
    """
    Get a list of items, marking the endpoint as deprecated.

    :return: A list of items.
    """
    return [{"item_id": "Foo"}]
