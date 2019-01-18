'''
    The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
    Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
'''

def problem_60():
    def is_pair_prime(primes):
        pairs = [(a, b) for i, a in enumerate(primes) for b in primes[i + 1:]]
        for pair in pairs:
            a, b = int(str(pair[0]) + str(pair[1])), int(str(pair[1]) + str(pair[0]))
            if not all(a % i for i in range(2, int(round(a**0.5 + 1)))) or not all(b % i for i in range(2, int(round(b**0.5 + 1)))):
                return False
        return True
    
    primes = [num for num in range(3, 10000) if all(num % i for i in range(2, int(round(num**0.5 + 1))))]
    for a in range(len(primes)):
        for b in range(a + 1, len(primes)):
            if not is_pair_prime([primes[a], primes[b]]):
                continue
            for c in range(b + 1, len(primes)):
                if not is_pair_prime([primes[a], primes[b], primes[c]]):
                    continue
                for d in range(c + 1, len(primes)):
                    if not is_pair_prime([primes[a], primes[b], primes[c], primes[d]]):
                        continue
                    for e in range(d + 1, len(primes)):
                        if not is_pair_prime([primes[a], primes[b], primes[c], primes[d], primes[e]]):
                            continue
                        return primes[a] + primes[b] + primes[c] + primes[d] + primes[e]

print(problem_60())