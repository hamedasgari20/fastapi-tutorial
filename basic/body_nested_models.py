from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix='/body_nested_models')


class Image(BaseModel):
    url: str
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    image: Image | None = None


@router.put("/items_a/{item_id}")
async def body_nested_models(item_id: int, item: Item):
    """
    Update an item with the given ID.

    Parameters:
    - `item_id`: The ID of the item to update.
    - `item`: The updated item data.

    Returns:
    - A dictionary containing the updated item ID and data.
    """
    results = {"item_id": item_id, "item": item}
    return results


@router.post("/index-weights/")
async def body_of_arbitrary_dict(weights: dict[int, float]):
    """
    Create a new index with the given weights.

    Parameters:
    - `weights`: A dictionary containing the weights for each index.

    Returns:
    - The weights dictionary.
    """
    return weights
