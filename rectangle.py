from pydantic import BaseModel
from pydantic import PositiveInt


class Rectangle(BaseModel):
    name: str | None
    calculate_area: bool
    width: PositiveInt
    height: PositiveInt
    area: PositiveInt | None
