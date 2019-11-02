'''
	The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.
	How many n-digit positive integers exist which are also an nth power?
'''

def problem_63():
    result = []
    for i in range(1, 10):
        j = 1
        while True:
            n = i**j
            if len(str(n)) == j:
                result.append((i, j, i**j))
            elif len(str(n)) < j:
                break
            j += 1
    return len(result)

print(problem_63())
