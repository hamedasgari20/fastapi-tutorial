from fastapi import FastAPI

from apps.path_parameters.path_parameters import router as path_parameters
from apps.query_parameters.query_parameters import router as query_parameters
from apps.request_body.request_body import router as request_body

app = FastAPI()

app = FastAPI()
app.include_router(path_parameters, tags=["path_parameters"])
app.include_router(query_parameters, tags=["query_parameters"])
app.include_router(request_body, tags=["request_body"])


@app.get("/")
async def root():
    """
    Returns a JSON object with a message "Hello World".
    """
    return {"message": "Hello World"}
