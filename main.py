from fastapi import FastAPI

from basic.body_nested_models import router as body_nested_models
from basic.extera_data_types import router as extra_data_types
from basic.path_parameters import router as path_parameters
from basic.path_parameters_and_numeric_validations import router as path_parameters_and_numeric_validations
from basic.query_parameters import router as query_parameters
from basic.query_parameters_and_string_validation import \
    router as query_parameters_and_string_validation
from basic.request_body import router as request_body
from basic.header_parameter import router as header_parameter

app = FastAPI()

app = FastAPI()
app.include_router(path_parameters, tags=["path_parameters"])
app.include_router(query_parameters, tags=["query_parameters"])
app.include_router(request_body, tags=["request_body"])
app.include_router(query_parameters_and_string_validation, tags=["query_parameters_and_string_validation"])
app.include_router(path_parameters_and_numeric_validations, tags=["path_parameters_and_numeric_validation"])
app.include_router(body_nested_models, tags=["body_nested_models"])
app.include_router(extra_data_types, tags=["extera_data_types"])
app.include_router(header_parameter, tags=["header_parameter"])




@app.get("/")
async def root():
    """
    Returns a JSON object with a message "Hello World".
    """
    return {"message": "Hello World"}
