"""
This module contains the endpoints of the API.
"""

from typing import Any
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.status import HTTP_200_OK

from src.model import LLM

app = FastAPI()
service = LLM()


class Request(BaseModel):
    """
    A Pydantic model representing a request to the endpoint.

    Attributes:

    """

    instructions: str


@app.get("/", status_code=HTTP_200_OK)
async def root() -> Any:
    """
    Get the root endpoint of the API.

    Returns:
        dict: A dictionary containing a response message.
    """
    return {"message": "API service"}


@app.post("/answer", status_code=HTTP_200_OK)
async def answer(request: Request) -> Any:
    """
    Endpoint to retrieve user input and post answer.

    Args:
        instructions (str): The user input

    Returns:
        str: The answer
    """

    print("Inputs received")
    result = service.answer(request.instructions)

    return {"text": result}
