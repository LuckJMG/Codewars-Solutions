def to_camel_case(text):
    result = ""
    cap_mode = False

    for char in text:
        if char in "-_":
            cap_mode = True
            continue

        if cap_mode:
            char = char.capitalize()
            cap_mode = False

        result += char

    return result
