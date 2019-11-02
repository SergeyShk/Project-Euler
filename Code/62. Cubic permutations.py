'''
    The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
    Find the smallest cube for which exactly five permutations of its digits are cube.
'''

def problem_62(p):
    cubes = {}
    n = 100

    while True:
        cube = n**3
        digits = ''.join(sorted(str(cube)))
        if digits in cubes:
            cubes[digits] += [cube]
            if len(cubes[digits]) == p:
                return cubes[digits][0]
        else:
            cubes[digits] = [cube]
        n += 1    

print(problem_62(5))