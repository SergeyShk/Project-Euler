'''
    There are exactly ten ways of selecting three from five, 12345:
    123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
    In combinatorics, we use the notation, 5C_3 = 10.
    In general,
    nCr =	n!/r!(n−r)!, where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
    It is not until n = 23, that a value exceeds one-million: 23C_10 = 1144066.
    
    How many, not necessarily distinct, values of  nC_r, for 1 ≤ n ≤ 100, are greater than one-million?
'''

def problem_53(nmin, nmax, lim):
    def factorial(n):
        fact = 1
        for i in range(1, n + 1):
            fact *= i        
        return fact
    
    values = 0
    for n in range(nmin, nmax + 1):
        for r in range(1, n):
            c = factorial(n) / (factorial(r) * factorial(n - r))
            if c > lim:
                values += 1
    return values

print(problem_53(1, 100, 1000000))
