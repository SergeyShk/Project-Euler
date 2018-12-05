'''
    The sum of the squares of the first ten natural numbers is,
    1**2 + 2**2 + ... + 10*2 = 385
    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)**2 = 552 = 3025
    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def problem_6(lim):
    sum_squares = square_sums = diff = 0
    for i in range(1, lim + 1):
        sum_squares += i**2
        square_sums += i
    square_sums = square_sums**2
    diff = square_sums - sum_squares
    return diff

print(problem_6(100))