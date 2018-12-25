'''
    The prime 41, can be written as the sum of six consecutive primes:
    41 = 2 + 3 + 5 + 7 + 11 + 13
    This is the longest sum of consecutive primes that adds to a prime below one-hundred.
    The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
    Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

def problem_50(lim):
    def is_prime(n):
        return all(n % i for i in range(2, int(round(n**0.5 + 1))))
    
    primes = [num for num in range(2, lim // 4) if all(num % i for i in range(2, int(round(num**0.5 + 1))))]
    max_sums = 0
    max_length = 0
    for i in range(len(primes)):
        if sum(primes[i: i + max_length]) > lim:
            return max_sums
        for j in range(len(primes) - i - 1, max_length, -1):
            sum_primes = sum(primes[i: i + j])
            if sum_primes > lim or not is_prime(sum_primes):
                continue
            if j > max_length:
                max_length = max(max_length, len(primes[i: i + j]))
                max_sums = max(max_sums, sum_primes)
                break

print(problem_50(1000000))