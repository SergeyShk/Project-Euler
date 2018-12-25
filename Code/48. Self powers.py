'''
    The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
    Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
'''

def problem_48(power, digits):
    return sum([i**i for i in range(1, power + 1)]) % (10**digits)

print(problem_48(1000, 10))