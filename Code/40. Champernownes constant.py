'''
    An irrational decimal fraction is created by concatenating the positive integers:
    
    0.123456789101112131415161718192021...
    
    It can be seen that the 12th digit of the fractional part is 1.
    
    If d_n represents the n^th digit of the fractional part, find the value of the following expression.
    
    d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
'''

def problem_40(n):
    num = ''
    res = 1
    for i in range(10**n + 1):
        num += str(i)
    for i in range(n + 1):
        res *= int(num[10**i])
    return res

print(problem_40(6))