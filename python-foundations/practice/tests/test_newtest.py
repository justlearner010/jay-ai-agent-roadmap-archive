from newtest import remove_duplicates

def test_remove_duplicates():
    assert remove_duplicates(
        [1,2,2,3]
    )==[1,2,3]

    assert remove_duplicates(
        [1,1,1]
    ) == [1]

    assert remove_duplicates(
        []
    ) == []

