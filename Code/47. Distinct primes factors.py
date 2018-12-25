'''
    The first two consecutive numbers to have two distinct prime factors are:
    14 = 2 × 7
    15 = 3 × 5
    The first three consecutive numbers to have three distinct prime factors are:
    644 = 2² × 7 × 23
    645 = 3 × 5 × 43
    646 = 2 × 17 × 19.
    Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
'''

def problem_47(lim):
    def prime_factors(n):
        factors = []
        if n % 2 == 0:
            factors.append(2)
            n /= 2
        for i in range(3, int(n + 1), 2):
            if n % i == 0 and all(i % j for j in range(2, int(round(i**0.5 + 1)))):
                factors.append(i)
        return factors
    
    consec = lim
    num = 10**(lim - 1)
    while consec != 0:
        num += 1
        if len(prime_factors(num)) != lim:
            consec = lim
        else:
            consec -= 1
    return num - lim + 1

print(problem_47(4))