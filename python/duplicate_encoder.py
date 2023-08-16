def duplicate_encode(word: str):
    word = word.lower()
    result = ""

    for char in word:
        if word.count(char) > 1:
            result += ")"
            continue
        result += "("

    return result
