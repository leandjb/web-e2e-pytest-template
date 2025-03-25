import pytest
from src.calc import Calculator


@pytest.fixture
def calculator():
    return Calculator()


def test_add_positives(calculator):
    assert calculator.add(0, 0) == 0
    assert calculator.add(0, 32767) == 32767
    assert calculator.add(-32767, 32767) == 0
    assert calculator.add(1, 65535) == 65536
    assert calculator.add(0.00003, 2147483647.00001) == 2147483647.00004


def test_add_negatives(calculator):
    assert calculator.add(32768, -0.000001) == 32767.999999
    assert calculator.add(-65535, 0) == -65535
    assert calculator.add(-0.0002, 65535) == 65534.9998
    assert calculator.add(-0.00003, 2147483648.00006) == 2147483648.00003


def test_subtract(calculator):
    assert calculator.subtract(2, 1) == 1
    assert calculator.subtract(2, 2) == 0
    assert calculator.subtract(2, 3) == -1


def test_multiply(calculator):
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(-1, 1) == -1
    assert calculator.multiply(-1, -1) == 1

@pytest.mark.skip(reason='Falta despliegue version 2.0.1 pendiente')
def test_divide(calculator):
    assert calculator.divide(6, 3) == 2
    assert calculator.divide(5, 2) == 2.5
    with pytest.raises(ValueError):
        calculator.divide(1, 0)
