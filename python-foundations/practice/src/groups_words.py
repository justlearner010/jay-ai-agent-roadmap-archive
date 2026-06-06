
def words_group(words):
    groups = {}

    for word in words:
        if not word:
            continue
        first  = word[0]

        if first not in groups:
            groups[first] = []

        groups[first].append(word)

    return groups