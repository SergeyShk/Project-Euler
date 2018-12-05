'''
	Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
	How many such routes are there through a 20x20 grid?
'''

def problem_15(size):
    routes = {'curr': {(0, 1): 1}}
    for i in range(size + size - 2):
        routes['next'] = {}
        for pos, freq in routes['curr'].items():
            for dx, dy in [(0, 1), (1, 0)]:
                step = pos[0] + dx, pos[1] + dy
                if step[0] <= size and step[1] <= size:
                    if step not in routes['next']:
                        routes['next'][step] = 1 * freq
                    else:
                        routes['next'][step] += 1 * freq
        routes['curr'] = routes['next'] 
    res = sum([freq for freq in routes['next'].values()])
    return res * 2

print(problem_15(20))