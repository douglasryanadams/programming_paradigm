from typing import List

from pydantic import BaseModel


class Shape(BaseModel):
    name: str
    sides: int
    side_lengths: List[int]
    corner_angles: List[float]
