def array_diff(a, b):
    result = []
    for element in a:
        if not element in b:
            result.append(element)

    return result
