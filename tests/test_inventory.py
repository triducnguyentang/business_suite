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
    # TODO: Implement this test.
    assert False, "Test not implemented"

def test_add_existing_product_fails(empty_inventory, sample_product):
    # TODO: Implement this test.
    assert False, "Test not implemented"

def test_remove_product_successfully(empty_inventory, sample_product):
    # TODO: Implement this test.
    assert False, "Test not implemented"