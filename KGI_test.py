import pytest
from KGI import KGI


serial_number_group = [("1234567890", "36212345678908"), ("1111111111", "36211111111111")]    
    
@pytest.mark.parametrize("test_input,expected",serial_number_group)
def test_eval(test_input, expected):
    assert KGI(test_input) == expected