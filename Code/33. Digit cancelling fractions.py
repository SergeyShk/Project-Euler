'''
    The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
    We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
    There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
    If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

def problem_33():
    prod = (1, 1)
    for i in range(10, 100):
        for j in range(10, 100):
            if i < j:
                il, ir = str(i)[0], str(i)[1]
                jl, jr = str(j)[0], str(j)[1]
                if il != ir and jl != jr and ir == jl and int(jr) != 0 and i / j == int(il) / int(jr):
                    prod = (prod[0] * int(il), prod[1] * int(jr))
    for i in range(prod[0], 0, -1):
        if prod[1] % i == 0 and prod[0] % i == 0:
            return int(prod[1] / i)
    
print(problem_33())