from enum import Enum

from fastapi import APIRouter

router = APIRouter(prefix='/path_parameters')


@router.get("/items/{item_id}")
async def read_item(item_id: int):
    """
    Returns a JSON object with the item_id.
    :param item_id: An integer representing the item ID.
    """
    return {"item_id": item_id}


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@router.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    """
    Get information about a machine learning model.

    Parameters:
    - model_name (ModelName): The name of the model to retrieve information for.

    Returns:
    - A dictionary containing information about the model, including its name and a message.

    Raises:
    - None
    """
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
