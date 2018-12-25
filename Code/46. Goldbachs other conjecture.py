'''
    It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
    9 = 7 + 2x1^2
    15 = 7 + 2x2^2
    21 = 3 + 2x3^2
    25 = 7 + 2x3^2
    27 = 19 + 2x2^2
    33 = 31 + 2x1^2
    It turns out that the conjecture was false.
    What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''

def problem_46():
    def is_prime(n):
        return all(n % i for i in range(2, int(round(n**0.5 + 1))))

    n = 33
    while True:
        n += 1
        if n % 2 != 0 and not is_prime(n):
            flag = True
            primes = [i for i in range(1, n) if is_prime(i)]
            for prime in primes[::-1]:
                if ((n - prime) / 2)**0.5 % 1 == 0:
                    flag = False
                    break
            if flag:
                return n

print(problem_46())