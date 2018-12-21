'''
    The n^th term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
    By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t_10. If the word value is a triangle number then we shall call the word a triangle word.
    Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''

def problem_42(file):
    with open(file, 'r') as file:
        words = file.read().replace('"', '').lower().split(',')
    triang_nums = [n * (n + 1) // 2 for n in range(1, max(list(map(len, words))) * 30)]
    triang_words = 0
    for word in words:
        value = 0
        for char in word:
            value += ord(char) - 96
        if value in triang_nums:
            triang_words += 1
    return triang_words

print(problem_42('../Resources/p042_words.txt'))