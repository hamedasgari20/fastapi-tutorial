import time

from fastapi import Request

from main import app


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """
    Adds an X-Process-Time header to the response containing the time it took to process the request.

    Args:
        request (Request): The request object.
        call_next (function): The next function in the middleware chain.

    Returns:
        Response: The response object.
    """
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
