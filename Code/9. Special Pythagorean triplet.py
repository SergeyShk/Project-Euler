'''
	A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
	a**2 + b**2 = c**2
	For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
	There exists exactly one Pythagorean triplet for which a + b + c = 1000.
	Find the product abc.
'''

def problem_9(lim):
    product = 6
    for a in range(1, lim // 3):
        for b in range(a + 1, lim // 2):
            for c in range(b + 1, lim - 2):
                if (a + b + c) != lim or (a**2 + b**2) != c**2:
                    continue
                product = max(a * b * c, product)
    return product

print(problem_9(1000))