'''
    Take the number 192 and multiply it by each of 1, 2, and 3:
    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576
    By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
    The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
    What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

def problem_38(n):
    pandigitals = set([str(i) for i in range(1, n + 1)])
    max_pandigital = 0
    i = 1
    while True:
        num = str(i)
        j = 2
        while True:
            product = i * j
            if len(num + str(product)) > n:
                break
            num += str(product)
            if set(num + str(product)) == pandigitals:
                max_pandigital = max(max_pandigital, int(num))
            j += 1
        if len(str(max_pandigital)) > n or len(str(i)) > n // 2:
            break
        i += 1
    return max_pandigital

print(problem_38(9))