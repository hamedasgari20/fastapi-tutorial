from fastapi import FastAPI

app = FastAPI()

from fastapi import FastAPI
from apps.path_parameters.path_parameters import router as path_parameters

app = FastAPI()
app.include_router(path_parameters, tags=["path_parameters"])


@app.get("/")
async def root():
    """
    Returns a JSON object with a message "Hello World".
    """
    return {"message": "Hello World"}
