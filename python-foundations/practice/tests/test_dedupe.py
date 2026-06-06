from dedupe import remove_duplicates

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 3, 3]) == [1, 2, 3]


def test_no_duplicates():
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]


def test_string_duplicates():
    assert remove_duplicates(["a", "b", "a"]) == ["a", "b"]


def test_empty_list():
    try:
        remove_duplicates([])
        assert False  # 没抛异常就失败
    except ValueError:
        pass

