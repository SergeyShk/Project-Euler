'''
    If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
    {20,48,52}, {24,45,51}, {30,40,50}
    For which value of p ≤ 1000, is the number of solutions maximised?
'''

def problem_39(lim):
    max_solutions = 0
    max_p = 0
    for p in range(12, lim + 1, 2):
        solutions = 0
        for a in range(1, p // 2):
            for b in range(p // 2 - a, p // 2):
                if a**2 + b**2 == (p - a - b)**2:
                    solutions += 1
        if solutions > max_solutions:
            max_solutions, max_p = solutions, p
    return max_p

print(problem_39(1000))