from str_reverse import str_reverse

def test_str_reverse():
    result = str_reverse("abcdef")
    assert result == "fedcba"
    
    assert str_reverse(
        ""
    )==""

    assert str_reverse(
        "a"
    )=="a"