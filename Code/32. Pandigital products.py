'''
    We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
    The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
    Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
    HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

def problem_32(n):
    pandigitals = set([str(i) for i in range(1, n + 1)])
    products = {}
    for i in range(2000):
        for j in range(2000):
            s = str(i) + str(j) + str(i * j)
            if len(s) > n:
                break
            ident = set(s)
            if len(s) == n and ident == pandigitals and i * j not in products:
                products[i * j] = 1
    return sum(products.keys())
    
print(problem_32(9))