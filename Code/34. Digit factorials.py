'''
    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
    Find the sum of all numbers which are equal to the sum of the factorial of their digits.
    Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

def problem_34():
    numbers = 0
    for i in range(3, 100000):
        facts = []
        for num in str(i):
            fact = 1
            for j in range(1, int(num) + 1):
                fact *= j
            facts.append(fact)
        if sum(facts) == i:
            numbers += sum(facts)
    return numbers
    
print(problem_34())