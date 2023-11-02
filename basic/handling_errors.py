from fastapi import APIRouter, HTTPException, FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse

router = APIRouter(prefix='/handling_errors')
app = FastAPI()


items = {"foo": "The Foo Wrestlers"}


@router.get("/items/{item_id}")
async def handling_errors(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}


@router.get("/items-header/{item_id}")
async def handling_errors_with_custom_header(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": "There goes my error"},
        )
    return {"item": items[item_id]}

