'''
	The prime factors of 13195 are 5, 7, 13 and 29.
	What is the largest prime factor of the number 600851475143 ?
'''

def problem_3(num):
    max_prime = 1
    if num % 2 == 0:
        max_prime = 2
        num /= 2
    for i in range(3, round(num ** 0.5) + 1, 2):
        if num % i == 0:
            max_prime = max(max_prime, i)
            num /= i
    return max_prime

print(problem_3(600851475143))