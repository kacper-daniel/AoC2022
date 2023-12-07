data = open('inputs/day7_input.txt', 'r').read().split('\n')
cards_and_bids = dict()
strengths = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
for line in data:
    helper = [x for x in line.split(" ")]    
    cards_and_bids[helper[0]] = int(helper[1])

def hand_to_dict(hand):
    helper = dict()
    for char in hand:
        if char not in helper:
            helper[char] = 1
        else:
            helper[char] += 1
    return helper

def map_to_category(hand):
    counted_chars = sorted(hand_to_dict(hand).values())
    if counted_chars == [5]:
        return 7
    if counted_chars == [1, 4]:
        return 6
    if counted_chars == [2, 3]:
        return 5
    if counted_chars == [1, 1, 3]:
        return 4
    if counted_chars == [1, 2, 2]:
        return 3
    if counted_chars == [1, 1, 1]:
        return 2
    else:
        return 1
    
# TODO: implement binary sort

print(cards_and_bids)
sorted_hands = []
for hand in cards_and_bids.keys():
    if sorted_hands ==[]:
        sorted_hands.append(hand)
    else:
        actual = map_to_category(hand)
        for i in range(len(sorted_hands)):
            curr = map_to_category(sorted_hands[i])
            if actual < curr:
                sorted_hands.insert(i, hand)
                break
            elif actual == curr:
                for j in range(len(hand)):
                    if strengths.index(hand[j])<strengths.index(sorted_hands[i][j]):
                        sorted_hands.insert(i,hand)
                        break
                else:
                    sorted_hands.append(hand)
            else:
                sorted_hands.append(hand)
print(sorted_hands)
output_one = 0
for i in range(1, len(sorted_hands) + 1):
    output_one += cards_and_bids[sorted_hands[i-1]] * i
print(output_one)