import pytest
from app.calculator import add, subtract, multiply, divide


# Caso exitoso: suma correcta
def test_add_success():
    assert add(2, 3) == 5


# Caso borde: resta con resultado negativo
def test_subtract_edge_case_negative_result():
    assert subtract(5, 8) == -3


# Caso borde: multiplicación por cero
def test_multiply_edge_case_zero():
    assert multiply(7, 0) == 0


# Caso exitoso: división correcta
def test_divide_success():
    assert divide(10, 2) == 5


# Caso de error: división por cero
def test_divide_by_zero_error():
    with pytest.raises(ValueError):
        divide(10, 0)