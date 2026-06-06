import pytest
from void_input import inp

def test_inp():

    assert inp(
        0
    ) == 0

    assert inp(
        -1
    )== -1


def test_inp_empty():
    with pytest.raises(ValueError):
        inp("")
    