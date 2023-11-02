from datetime import datetime, time, timedelta
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Body

router = APIRouter(prefix='/extra_data_types')


@router.put("/items/{item_id}")
async def extra_data_types(
        item_id: UUID,
        start_datetime: Annotated[datetime | None, Body()] = None,
        end_datetime: Annotated[datetime | None, Body()] = None,
        repeat_at: Annotated[time | None, Body()] = None,
        process_after: Annotated[timedelta | None, Body()] = None,
):
    """
    Update an item with extra data types.

    :param item_id: The ID of the item to update.
    :param start_datetime: The start datetime of the item.
    :param end_datetime: The end datetime of the item.
    :param repeat_at: The time at which the item should repeat.
    :param process_after: The amount of time to wait after the start datetime before processing the item.
    :return: A dictionary containing the updated item data.
    """
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }
