'''
    The square root of 2 can be written as an infinite continued fraction.
    The infinite continued fraction can be written, 2–√=[1;(2)], (2) indicates that 2 repeats ad infinitum. In a similar way, 23−−√=[4;(1,3,1,8)].
    It turns out that the sequence of partial values of continued fractions for square roots provide the best rational approximations. Let us consider the convergents for 2–√.
    What is most surprising is that the important mathematical constant,
    e=[2;1,2,1,1,4,1,1,6,1,...,1,2k,1,...].
    The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.
    Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.
'''

def problem_65(lim):
    n0 = 1
    n1 = 2
    for i in range(2, lim + 1): 
        n0, n1 = n1, n0 + n1 * (1 if i % 3 else 2 * i // 3)
    return sum(map(int, str(n1)))

print(problem_65(100))