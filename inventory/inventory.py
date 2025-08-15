from typing import Dict, Optional
from .product import Product

class Inventory:
    """Manages a collection of products in the inventory."""

    def __init__(self):
        """Initializes the inventory with an empty dictionary to store products."""
        self._products: Dict[str, Product] = {}

    def add_product(self, product: Product) -> bool:
        """
        Adds a new product to the inventory.
        - A product should not be added if a product with the same ID already exists.
        - Returns True if the product was added successfully, False otherwise.
        """
        # TODO: Implement this method.
        pass

    def remove_product(self, product_id: str) -> bool:
        """
        Removes a product from the inventory by its ID.
        - Returns True if the product was removed successfully, False if the product_id was not found.
        """
        # TODO: Implement this method.
        pass

    def update_quantity(self, product_id: str, new_quantity: int) -> bool:
        """
        Updates the quantity of an existing product.
        - The new quantity must be zero or positive.
        - Returns True if the quantity was updated, False if the product_id was not found
          or the new_quantity is negative.
        """
        # TODO: Implement this method.
        pass

    def get_product_details(self, product_id: str) -> Optional[Product]:
        """
        Retrieves a product's details by its ID.
        - Returns the Product object if found, otherwise returns None.
        """
        # TODO: Implement this method.
        pass

    def get_inventory_summary(self) -> str:
        """
        Returns a string summary of the inventory.
        - The summary should list each product's ID, name, and quantity.
        - If the inventory is empty, it should return "Inventory is empty."
        - Example format for one item: "ID: 101, Name: Laptop, Quantity: 10"
        """
        # TODO: Implement this method.
        pass