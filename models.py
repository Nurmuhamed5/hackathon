
from dataclasses import dataclass

from dataclasses import dataclass


class BaseModel:
    id: int
    FILE: str

    def to_json():
        raise NotImplementedError

    @classmethod
    def from_json(cls, json: dict):
        raise NotImplementedError


@dataclass
class Car(BaseModel):
    brand: str
    model: str
    release_year: int
    engine_volume: float
    body_type: str
    color: str
    miliage: float
    price: float

    id: int = 0

    FILE = "data/json/car.json"

    def to_json(self):
        return {
            "id": self.id,
            "brand": self.brand,
            "model": self.model,
            "release_year": self.release_year,
            "engine_volume": self.engine_volume,
            "body_type": self.body_type,
            "color": self.color,
            "miliage": self.miliage,
            "price": self.price,
        }

    @classmethod
    def from_json(cls, json: dict):
        return cls(**json)