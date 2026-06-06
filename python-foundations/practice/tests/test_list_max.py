import pytest
from list_max import list_max
def test_list_max():
    result = list_max([1,2,3,4,5])
    assert result == 5

    assert list_max(
        [-1,-2,-3,-4,-5]
    ) == -1

    assert list_max(
        [0,0,0,0,0]
    ) == 0

def empty_list():
    with pytest.raises(ValueError):
        list_max([])