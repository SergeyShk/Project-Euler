'''
	2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
	What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def problem_5(lim):
    num = 0
    not_div = True
    while not_div:
        num += 1 
        for i in range(2, lim + 1):
            not_div = num % i != 0
            if not_div:
                break
    return num

print(problem_5(20))