def narcissistic(value):
    num = str(value)
    sum = 0

    for digit in num:
        sum += int(digit) ** len(num)

    return value == sum
