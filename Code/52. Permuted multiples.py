'''
    It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
    Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''

def problem_52():
    def is_permuted(x, y):
        return sorted(str(x)) == sorted(str(y))

    x = 1
    while True:
        x += 1
        if is_permuted(x, x * 2) and is_permuted(x, x * 3) \
        and is_permuted(x, x * 4) and is_permuted(x, x * 5) \
        and is_permuted(x, x * 6):
            return x

print(problem_52())