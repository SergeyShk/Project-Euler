'''
    In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:
    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    The cards are valued in the order:
    2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
    If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.
    Consider the following five hands dealt to two players:
    Hand 1:
    Player 1 - 5H 5C 6S 7S KD (Pair of Fives)
    Player 2 - 2C 3S 8S 8D TD (Pair of Eights)
    Winner - Player 2
    Hand 2:
    Player 1 - 5D 8C 9S JS AC (Highest card Ace)
    Player 2 - 2C 5C 7D 8S QH (Highest card Queen)
    Winner - Player 1
    Hand 3:
    Player 1 - 2D 9C AS AH AC (Three Aces)
    Player 2 - 3D 6D 7D TD QD (Flush with Diamonds)
    Winner - Player 2
    Hand 4:
    Player 1 - 4D 6S 9H QH QC (Pair of Queens, Highest card Nine)
    Player 2 - 3D 6D 7H QD QS (Pair of Queens, Highest card Seven)
    Winner - Player 1
    Hand 5:
    Player 1 - 2H 2D 4C 4D 4S (Full House, With Three Fours)
    Player 2 - 3C 3D 3S 9S 9D (Full House, With Three Threes)
    Winner - Player 1    
    The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.
    How many hands does Player 1 win?
'''

def problem_54(file):
    def check_hand(hand):
        result, highest, highest_ext = '', 0, 0
        cards, values, suits = [], [], []
        freqs = {}
        for card in hand:
            cards.append(card[0])
            values.append(cards_value[card[0]])
            suits.append(card[1])
            if card[0] in freqs:
                freqs[card[0]] += 1
            else:
                freqs[card[0]] = 1
        if len(set(suits)) == 1 and sum(values) == 60:
            result = 'Royal Flush'
        elif len(set(suits)) == 1 and len(set(cards)) == 5 and max(values) - min(values) == 4:
            result = 'Straight Flush'
            highest = max(values)
        elif len(set(cards)) == 2 and 4 in freqs.values():
            result = 'Four of a Kind'
            highest = cards_value[sorted(freqs, key=lambda x: freqs[x])[1]]
        elif len(set(cards)) == 2 and 3 in freqs.values():
            result = 'Full House'
            highest = cards_value[sorted(freqs, key=lambda x: freqs[x])[1]]
        elif len(set(suits)) == 1:
            result = 'Flush'
            highest = max(values)
        elif len(set(cards)) == 5 and max(values) - min(values) == 4:
            result = 'Straight'
            highest = max(values)
        elif 3 in freqs.values():
            result = 'Three of a Kind'
            highest = cards_value[sorted(freqs, key=lambda x: freqs[x])[-1]]
        elif len(set(cards)) == 3 and 1 in freqs.values():
            result = 'Two Pairs'
            highest = max([cards_value[x] for x in sorted(freqs, key=lambda x: freqs[x])[-1: -3: -1]])
            highest_ext = cards_value[sorted(freqs, key=lambda x: freqs[x])[0]]
        elif len(set(cards)) == 4:
            result = 'One Pair'
            highest = cards_value[sorted(freqs, key=lambda x: freqs[x])[-1]]
            highest_ext = max([cards_value[x] for x in sorted(freqs, key=lambda x: freqs[x])[: 3]])
        else:
            result = 'High Card'
            highest = max(values)
        return combinations_value[result], highest, highest_ext
        
    cards_value = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                   '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    combinations_value = {'High Card': 1, 'One Pair': 2, 'Two Pairs': 3,
                          'Three of a Kind': 4, 'Straight': 5, 'Flush': 6,
                          'Full House': 7, 'Four of a Kind': 8,
                          'Straight Flush': 9, 'Royal Flush': 10}
    with open(file, 'r') as file:
        hands = [cards.split(' ') for cards in file.read().split('\n')][:-1]
        player_1 = [hand[: 5] for i, hand in enumerate(hands)]
        player_2 = [hand[5: 10] for i, hand in enumerate(hands)]
    player_1_wins = 0
    for i in range(len(player_1)):
        result_1, highest_1, highest_ext_1 = check_hand(player_1[i])
        result_2, highest_2, highest_ext_2 = check_hand(player_2[i])
        total_1 = result_1 * 10000 + highest_1 * 100 + highest_ext_1
        total_2 = result_2 * 10000 + highest_2 * 100 + highest_ext_2
        if total_1 > total_2:
            player_1_wins += 1
    return player_1_wins

print(problem_54('../Resources/p054_poker.txt'))