from fastapi import APIRouter

router = APIRouter(prefix='/query_parameters')

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@router.get("/query-parameters/")
async def query_parameters(skip: int = 0, limit: int = 10):
    """
    Get a list of items from the fake database.

    Parameters:
    # - skip (int): The number of items to skip.
    - limit (int): The maximum number of items to return.

    Returns:
    - A list of items from the fake database.

    Raises:
    - None
    """
    return fake_items_db[skip: skip + limit]


@router.get("/query-parameters-and-path-parameters/{user_id}/items/{item_id}")
async def query_and_path_parameters(
        user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    """
    Get information about an item with a given ID and owner ID.

    Parameters:
    - user_id (int): The ID of the item's owner.
    - item_id (str): The ID of the item.
    - q (str | None): An optional query string.
    - short (bool): Whether to return a short description.

    Returns:
    - A dictionary containing information about the item, including its ID, owner ID, and description.

    Raises:
    - None
    """
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@router.get("/required-query-parameters/")
async def required_query_parameters(item_id: str, needy: str):
    """
    Get information about an item with a given ID and a needy parameter.

    Parameters:
    - item_id (str): The ID of the item.
    - needy (str): A needy parameter.

    Returns:
    - A dictionary containing information about the item, including its ID and the needy parameter.

    Raises:
    - None
    """
    item = {"item_id": item_id, "needy": needy}
    return item
