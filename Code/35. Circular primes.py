'''
    The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
    How many circular primes are there below one million?
'''

def problem_35(lim):
    primes = {str(num): 1 for num in range(2, lim) if all(num % i for i in range(2, int(round(num**0.5 + 1))))}
    for prime in primes:
        prime_new = prime
        for i in range(len(prime)):
            prime_new = prime_new[1: len(prime_new) + 1] + prime_new[0]
            if prime_new not in primes:
                primes[prime] = 0
                break
    return len([i for i in primes.values() if i != 0])
    
print(problem_35(1000000))