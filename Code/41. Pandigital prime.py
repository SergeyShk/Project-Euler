'''
    We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
    What is the largest n-digit pandigital prime that exists?
'''

def problem_41():
    def is_prime(n):
        return all(n % i for i in range(2, int(round(n**0.5 + 1))))
    def permutation(digits):
            if len(digits) <= 1:
                yield digits
            else:
                for permute in permutation(digits[1:]):
                    for i in range(len(digits)):
                        yield permute[:i] + digits[0: 1] + permute[i:]
    
    n = 9
    while n > 1:
        pandigitals = [int(j) for j in sorted(permutation(''.join([str(i) for i in range(n, 0, -1)])), reverse=True) if is_prime(int(j))]
        if len(pandigitals) != 0:
            return pandigitals[0]
        n -= 1

print(problem_41())