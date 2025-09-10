import pytest
from inventory.inventory import Inventory
from inventory.product import Product

@pytest.fixture
def empty_inventory():
    return Inventory()

@pytest.fixture
def sample_product():
    return Product(product_id="P001", name="Laptop", price=1200.00, quantity=10)

def test_add_product_successfully(empty_inventory, sample_product):
    empty_inventory.add_product(sample_product)
    # Check if the product is in the inventory  
    assert sample_product.product_id in empty_inventory.products
    # Optionally, check if the stored product matches the added product
    assert empty_inventory.products[sample_product.product_id] == sample_product
    assert False, "Test not implemented"

def test_add_existing_product_fails(empty_inventory, sample_product):
    empty_inventory.add_product(sample_product)
    with pytest.raises(ValueError):
        empty_inventory.add_product(sample_product) # Adding the same product again should raise an error
    assert False, "Test not implemented"

def test_remove_product_successfully(empty_inventory, sample_product):
    empty_inventory.add_product(sample_product)
    empty_inventory.remove_product(sample_product.product_id)
    assert sample_product.product_id not in empty_inventory.products
    assert False, "Test not implemented"