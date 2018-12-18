'''
    In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
    It is possible to make £2 in the following way:
    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
    How many different ways can £2 be made using any number of coins?
'''

def problem_31():
    ways = 2
    for po_1 in range(2):
        total_po_1 = po_1 * 100
        for pe_50 in range((200 - total_po_1) // 50 + 1):
            total_pe_50 = total_po_1 + pe_50 * 50
            for pe_20 in range((200 - total_pe_50) // 20 + 1):
                total_pe_20 = total_pe_50 + pe_20 * 20
                for pe_10 in range((200 - total_pe_20) // 10 + 1):
                    total_pe_10 = total_pe_20 + pe_10 * 10
                    for pe_5 in range((200 - total_pe_10) // 5 + 1):
                        total_pe_5 = total_pe_10 + pe_5 * 5
                        for pe_2 in range((200 - total_pe_5) // 2 + 1):
                            total_pe_2 = total_pe_5 + pe_2 * 2
                            for pe_1 in range(200 - total_pe_2 + 1):
                                total_pe_1 = total_pe_2 + pe_1
                                if total_pe_1 == 200:
                                    ways += 1
    return ways
    
print(problem_31())