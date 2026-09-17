def get_even_squares(numbers):
    result = []
    for i in numbers:
        if i % 2 == 0:
            square = i**2
            result.append(square)
    return result


print(get_even_squares([1, 2, 3, 4, 5, 6]))
