from dataclasses import dataclass


@dataclass
class Product:
    id: str
    name: str
    desc: str
    price: float

    def __str__(self):
        return f"{self.name},{self.desc} - {self.price}"