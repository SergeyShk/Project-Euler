'''
	By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
	What is the 10 001st prime number?
'''

def problem_7(lim):
    n = 1
    while lim > 0:   
        n += 1
        if all(n % i for i in range(2, int(round(n**0.5 + 1)))):
            lim -= 1
    return n

print(problem_7(10001))