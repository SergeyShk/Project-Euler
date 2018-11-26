'''
	A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
	Find the largest palindrome made from the product of two 3-digit numbers.
'''

def problem_4(digit):
    palindrome = 0
    for i in range(1, 10 ** digit):
        for j in range(1, 10 ** digit):
            n = i * j
            if str(n) == str(n)[::-1]:
                palindrome = max(n, palindrome)
    return palindrome

print(problem_4(1))