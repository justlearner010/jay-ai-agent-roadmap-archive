import pytest
from sort_records import sort_students


def test_sort_students_by_score_ascending():
    students = [
        {"name": "Tom", "score": 90},
        {"name": "Alice", "score": 95},
        {"name": "Bob", "score": 80}
    ]

    result = sort_students(students, "score")

    assert result == [
        {"name": "Bob", "score": 80},
        {"name": "Tom", "score": 90},
        {"name": "Alice", "score": 95}
    ]


def test_sort_students_by_score_descending():
    students = [
        {"name": "Tom", "score": 90},
        {"name": "Alice", "score": 95},
        {"name": "Bob", "score": 80}
    ]

    result = sort_students(students, "score", reverse=True)

    assert result == [
        {"name": "Alice", "score": 95},
        {"name": "Tom", "score": 90},
        {"name": "Bob", "score": 80}
    ]


def test_sort_students_by_name():
    students = [
        {"name": "Tom", "score": 90},
        {"name": "Alice", "score": 95},
        {"name": "Bob", "score": 80}
    ]

    result = sort_students(students, "name")

    assert result == [
        {"name": "Alice", "score": 95},
        {"name": "Bob", "score": 80},
        {"name": "Tom", "score": 90}
    ]


def test_sort_students_empty_list():
    result = sort_students([], "score")

    assert result == []


def test_sort_students_missing_field():
    students = [
        {"name": "Tom", "score": 90},
        {"name": "Alice"}
    ]

    with pytest.raises(KeyError):
        sort_students(students, "score")