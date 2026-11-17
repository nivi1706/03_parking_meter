import pytest
from parking_permit import is_permit_valid


# PARK-TCS-007
def test_active_permit_120_minutes():
    assert is_permit_valid(True, 120) is True


# PARK-TCS-008
def test_active_permit_121_minutes():
    assert is_permit_valid(True, 121) is False


# PARK-TCS-009
def test_inactive_permit():
    assert is_permit_valid(False, 120) is False


# PARK-TCS-010
def test_negative_parked_minutes():
    with pytest.raises(ValueError):
        is_permit_valid(True, -1)


# PARK-TCS-011
def test_invalid_permit_type():
    with pytest.raises(TypeError):
        is_permit_valid(1, 60)


# PARK-TCS-012
def test_invalid_parked_minutes_type():
    with pytest.raises(TypeError):
        is_permit_valid(True, "120")


# PARK-TCS-017
def test_active_permit_zero_minutes():
    assert is_permit_valid(True, 0) is True


# PARK-TCS-018
def test_inactive_permit_zero_minutes():
    assert is_permit_valid(False, 0) is False


# PARK-TCS-019
def test_float_parked_minutes():
    with pytest.raises(TypeError):
        is_permit_valid(True, 60.5)