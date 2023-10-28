from fastapi import FastAPI

from basic.path_parameters import router as path_parameters
from basic.query_parameters import router as query_parameters
from basic.query_parameters_and_string_validation import \
    router as query_parameters_and_string_validation
from basic.request_body import router as request_body

app = FastAPI()

app = FastAPI()
app.include_router(path_parameters, tags=["path_parameters"])
app.include_router(query_parameters, tags=["query_parameters"])
app.include_router(request_body, tags=["request_body"])
app.include_router(query_parameters_and_string_validation, tags=["query_parameters_and_string_validation"])


@app.get("/")
async def root():
    """
    Returns a JSON object with a message "Hello World".
    """
    return {"message": "Hello World"}
