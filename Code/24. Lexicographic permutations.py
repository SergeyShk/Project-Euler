'''
	A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
	012   021   102   120   201   210
	What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

def problem_24(lim):
    digits = [str(i) for i in range(0, 10)]
    
    def permutation(digits):
        if len(digits) <= 1:
            yield digits
        else:
            for permute in permutation(digits[1:]):
                for i in range(len(digits)):
                    yield permute[:i] + digits[0: 1] + permute[i:]
                    
    return int(sorted([''.join(x) for x in permutation(digits)])[lim - 1])

print(problem_24(1000000))