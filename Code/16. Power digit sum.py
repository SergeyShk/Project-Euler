'''
	2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
	What is the sum of the digits of the number 2^1000?
'''

def problem_16(n):
    return sum(list(map(int, [num for num in str(2**n)])))

print(problem_16(1000))