from dataclasses import dataclass

@dataclass
class Product:
    """A class to represent a single product in the inventory."""
    product_id: str
    name: str
    price: float
    quantity: int