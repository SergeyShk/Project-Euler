'''
    Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.
    37 36 35 34 33 32 31
    38 17 16 15 14 13 30
    39 18  5  4  3 12 29
    40 19  6  1  2 11 28
    41 20  7  8  9 10 27
    42 21 22 23 24 25 26
    43 44 45 46 47 48 49
    It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.
    If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
'''

def problem_58(lim):
    def is_prime(n):
        return all(n % i for i in range(2, int(round(n**0.5 + 1))))
    def count_prime_corners(s):
        corner_1 = s**2 - 3 * s + 3
        corner_2 = s**2 - 2 * s + 2
        corner_3 = s**2 - 1 * s + 1
        return is_prime(corner_1) + is_prime(corner_2) + is_prime(corner_3)
    
    size = 7
    prime_corners = 8
    ratio = 1
    while True:
        size += 2
        prime_corners += count_prime_corners(size)
        ratio = prime_corners / (size // 2 * 4)
        if ratio <= lim:
            return size
    
print(problem_58(0.1))