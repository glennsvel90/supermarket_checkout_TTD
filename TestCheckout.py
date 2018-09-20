import pytest
from Checkout import Checkout

@pytest.fixture()
def checkout():
    checkout = Checkout()
    return checkout

def test_CanAddItemPrice(checkout):
    checkout.addItemPrice("a",1)

def test_CanAddItem(checkout):
    checkout.addItem("a")

def test_CanFindTheCurrentTotal(checkout):
    checkout.addItemPrice("a", 1)
    checkout.addItem("a")
    assert checkout.CalculateTotal() == 1