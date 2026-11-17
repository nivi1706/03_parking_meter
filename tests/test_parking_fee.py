import os
import sys
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from parking_fee import calculate_parking_fee


# PARK-TCS-001
def test_zero_minutes():
    assert calculate_parking_fee(0) == 0


# PARK-TCS-002
def test_one_minute():
    assert calculate_parking_fee(1) == 200


# PARK-TCS-003
def test_sixty_minutes():
    assert calculate_parking_fee(60) == 200


# PARK-TCS-004
def test_sixty_one_minutes():
    assert calculate_parking_fee(61) == 400


# PARK-TCS-005
def test_negative_minutes():
    with pytest.raises(ValueError):
        calculate_parking_fee(-1)


# PARK-TCS-006
def test_invalid_minutes_type():
    with pytest.raises(TypeError):
        calculate_parking_fee("60")


# PARK-TCS-013
def test_one_hundred_twenty_minutes():
    assert calculate_parking_fee(120) == 400


# PARK-TCS-014
def test_one_hundred_twenty_one_minutes():
    assert calculate_parking_fee(121) == 600


# PARK-TCS-015
def test_float_minutes():
    with pytest.raises(TypeError):
        calculate_parking_fee(1.5)


# PARK-TCS-016
def test_boolean_minutes():
    with pytest.raises(TypeError):
        calculate_parking_fee(True)