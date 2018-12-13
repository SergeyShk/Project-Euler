'''
    Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13
    It can be verified that the sum of the numbers on the diagonals is 101.
    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

def problem_28(size):
    grid = [[0 for i in range(size)] for j in range(size)]
    x, y = size // 2, size // 2
    dx, dy = 0, 1
    squares = [n**2 for n in range(1, size + 1) if n % 2 != 0]
    dist = 0
    for i in range(1, size**2 + 1):
        grid[x][y] = i
        if i in squares:
            dist += 1
        new_x, new_y = x + dx, y + dy
        if max(abs(new_x - size // 2), abs(new_y - size // 2)) <= dist:
            x, y = new_x, new_y
        else:
            dx, dy = dy, -1 * dx
            x, y = x + dx, y + dy
    sums_diag = 1
    for i in range(size):
        if i != size // 2:
            sums_diag += grid[i][i] + grid[i][size - i - 1]
    return sums_diag
    
print(problem_28(1001))