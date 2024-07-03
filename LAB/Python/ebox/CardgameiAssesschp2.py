card1 = input()
card2 = input()
card3 = input()

card1_type = card1[0]
card1_number = int(card1[1:])
card2_type = card2[0]
card2_number = int(card2[1:])
card3_type = card3[0]
card3_number = int(card3[1:])

if card1_type == card2_type == card3_type and card1_number == card2_number == card3_number:
    print("Double Bonanza")
elif card1_type == card2_type == card3_type or card1_number == card2_number == card3_number:
    print("Bonanza")
else:
    print("No Bonanza")
