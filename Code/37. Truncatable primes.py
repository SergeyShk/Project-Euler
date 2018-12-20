'''
    The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
    Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

def problem_37(primes):
    def is_prime(n):
        return n != 1 and all(n % i for i in range(2, int(round(n**0.5 + 1))))
    
    n = 8
    primes_sum = 0
    while primes > 0:
        n += 1
        all_primes = True
        if is_prime(n):
            for i in range(1, len(str(n))):
                left = int(str(n)[i: len(str(n))])
                right = int(str(n)[0: len(str(n)) - i])
                if not is_prime(left) or not is_prime(right):
                    all_primes = False
                    break
            if all_primes:
                primes -= 1
                primes_sum += n
    return primes_sum
    
print(problem_37(11))