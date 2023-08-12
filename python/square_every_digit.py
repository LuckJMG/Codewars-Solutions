def square_digits(num):
    num = str(num)
    result = ""

    for char in num:
        result += str(int(char) * int(char))

    return int(result)
