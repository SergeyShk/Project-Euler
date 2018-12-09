'''
	n! means n × (n − 1) × ... × 3 × 2 × 1
	For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
	and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
	Find the sum of the digits in the number 100!
'''

def problem_20(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return sum(list(map(int, [num for num in str(fact)])))

print(problem_20(100))