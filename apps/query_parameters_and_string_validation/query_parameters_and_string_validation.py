from fastapi import APIRouter, Query

router = APIRouter(prefix='/query_parameters_and_string_validation')


@router.get("/items_a/")
async def query_parameter(q: str | None = None):
    """
    This function returns a dictionary of items with an optional query parameter.

    Parameters:
    q (str | None): An optional query parameter.

    Returns:
    dict: A dictionary of items with an optional query parameter.
    """
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@router.get("/items_b/")
async def query_parameter_with_string_validation(q: str = Query(default=None, max_length=10)):
    """
    This function returns a dictionary of items with a string query parameter that is validated for maximum length.

    Parameters:
    q (str): A string query parameter with a maximum length of 10 characters.

    Returns:
    dict: A dictionary of items with a validated string query parameter.
    """
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@router.get("/items_c/")
async def query_parameter_with_regular_expression_validation(q: str = Query(default=None, pattern="^fixedquery$")):
    """
    This function returns a dictionary of items with a string query parameter that is validated using a regular expression pattern.

    Parameters:
    q (str): A string query parameter that matches the regular expression pattern "^fixedquery$".

    Returns:
    dict: A dictionary of items with a validated string query parameter.
    """
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@router.get("/items_d/")
async def query_parameter_with_string_validation_which_is_required(q: str = Query(max_length=10)):
    """
    This function returns a dictionary of items with a required string query parameter that is validated for maximum length.

    Parameters:
    q (str): A required string query parameter with a maximum length of 10 characters.

    Returns:
    dict: A dictionary of items with a validated required string query parameter.
    """
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
