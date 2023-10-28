from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    """
    A Pydantic model representing a user.

    Attributes:
    -----------
    id : int
        The user's ID.
    name : str, optional
        The user's name. Defaults to "John Doe".
    signup_ts : datetime.datetime, optional
        The timestamp of when the user signed up. Defaults to None.
    friends : List[int], optional
        A list of the user's friend IDs. Defaults to an empty list.
    """
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)
print(user)
