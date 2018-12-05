'''
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.
'''

def problem_10(lim):
    n = 1
    add = 0
    while True:   
        if n == lim:
            break
        n += 1
        if all(n % i for i in range(2, int(round(n**0.5 + 1)))):
            add += n
    return add

print(problem_10(2000000))