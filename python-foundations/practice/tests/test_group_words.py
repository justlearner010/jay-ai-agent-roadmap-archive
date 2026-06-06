from groups_words import words_group

def test_words_group():
    assert words_group(
    ["apple","banana","air","bake"]
    ) == {'a':['apple','air'],'b':['banana','bake']}

    assert words_group(
        []
    )== {}
    