'''
    All square roots are periodic when written as continued fractions
    For conciseness, we use the notation √23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats indefinitely.
    The first ten continued fraction representations of (irrational) square roots are:

    √2=[1;(2)], period=1
    √3=[1;(1,2)], period=2
    √5=[2;(4)], period=1
    √6=[2;(2,4)], period=2
    √7=[2;(1,1,1,4)], period=4
    √8=[2;(1,4)], period=2
    √10=[3;(6)], period=1
    √11=[3;(3,6)], period=2
    √12= [3;(2,6)], period=2
    √13=[3;(1,1,1,1,6)], period=5

    Exactly four continued fractions, for N ≤ 13, have an odd period.

    How many continued fractions for N ≤ 10000 have an odd period?
'''

def problem_64(lim):
    result = 0
    for N in range(2, lim + 1):
        r = limit = int(N**0.5)
        if limit**2 == N: 
            continue
        k = 1
        period = 0
        while k != 1 or period == 0:
            k = (N - r * r) // k
            r = (limit + r) // k * k - r
            period += 1
        if period % 2 == 1: 
            result += 1
    return result

print(problem_64(10000))