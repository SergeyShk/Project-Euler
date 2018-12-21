'''
    The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
    Let d_1 be the 1^st digit, d_2 be the 2^nd digit, and so on. In this way, we note the following:
    d_2d_3d_4=406 is divisible by 2
    d_3d_4d_5=063 is divisible by 3
    d_4d_5d_6=635 is divisible by 5
    d_5d_6d_7=357 is divisible by 7
    d_6d_7d_8=572 is divisible by 11
    d_7d_8d_9=728 is divisible by 13
    d_8d_9d_10=289 is divisible by 17
    Find the sum of all 0 to 9 pandigital numbers with this property.
'''

def problem_43():
    def is_prime(n):
        return all(n % i for i in range(2, int(round(n**0.5 + 1))))
    def permutation(digits):
            if len(digits) <= 1:
                yield digits
            else:
                for permute in permutation(digits[1:]):
                    for i in range(len(digits)):
                        yield permute[:i] + digits[0: 1] + permute[i:]
    
    pandigitals = [int(j) for j in permutation(''.join([str(i) for i in range(10)])) if j[0] != '0']
    primes = [i for i in range(2, 18) if is_prime(i)]
    sum_pandigitals = 0
    for pandigital in pandigitals:
        flag = True
        for i, prime in enumerate(primes):
            if int(str(pandigital)[i + 1: i + 4]) % prime != 0:
                flag = False
                break
        if flag:
            sum_pandigitals += pandigital
    return sum_pandigitals

print(problem_43())