'''
    Euler discovered the remarkable quadratic formula:
    n^2+n+41
    It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,40^2+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,41^2+41+41 is clearly divisible by 41.
    The incredible formula n^2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.
    Considering quadratics of the form:
    n^2+an+b, where |a|<1000 and |b|≤1000
    where |n| is the modulus/absolute value of n
    e.g. |11|=11 and |−4|=4
    Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
'''

def problem_27(a, b):
    max_primes = {'a': 0, 'b': 0, 'n': 0}
    for a in range(-1 * a, a + 1):
        for b in range(-1 * b, b + 1):
            n = 0
            while True:
                num = n**2 + a * n + b
                if len([i for i in range(2, round(abs(num)**0.5) + 1) if num % i == 0]) == 0:
                    n += 1
                else:
                    break
                if n > max_primes['n']:
                    max_primes['a'] = a
                    max_primes['b'] = b
                    max_primes['n'] = n
    return max_primes['a'] * max_primes['b']

print(problem_27(1000, 1000))