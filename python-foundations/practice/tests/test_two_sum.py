from two_sum import two_sum

def test_two_sum():
    assert two_sum(
        [2,9,10,11],13
    )== [[0,3]]
    assert two_sum(
        [],0
    ) == []

    assert two_sum(
        [-1,-2,1,2],0
    )== [[0,2],[1,3]]