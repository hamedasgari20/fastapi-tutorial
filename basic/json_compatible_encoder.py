from datetime import datetime

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

router = APIRouter(prefix='/json_compatible_encoder')


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str | None = None


@router.get("/items/")
def return_json_compatible_of_pydantic_model(item: Item):
    """
    Convert a Pydantic model to a JSON-compatible dictionary.

    :param item: The Pydantic model to convert.
    :return: A dictionary containing the JSON-compatible data.
    """
    json_compatible_item_data = jsonable_encoder(item)
    return json_compatible_item_data
