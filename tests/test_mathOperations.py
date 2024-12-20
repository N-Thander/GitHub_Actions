
from src.math_operations import add, subtract


def test_add():
    assert add(2, 3) == 5
    assert add(-5, 0) == -5
    
def test_subtract():
    assert subtract(2, 3) == -1
    assert subtract(-5, 0) == -5
    