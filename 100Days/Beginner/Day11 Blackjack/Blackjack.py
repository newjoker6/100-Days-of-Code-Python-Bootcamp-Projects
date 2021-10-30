import random, sys

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []


dealer_cards = []



def deal_cards():
    user_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))
    user_cards.append(random.choice(cards))
    dealer_cards.append("?")

def total_user(hand):
    total = 0
    for card in hand:
        total += card
    return total

def hit(hand):
    hand.append(random.choice(cards))


deal_cards()
user_total = total_user(user_cards)

while True:
    print(f"Dealer has: {dealer_cards}\n")
    print(f"You have: {user_cards}")
    print(f"Your total is {user_total}\n")
    answer = input("Would you like another card? 'y' or 'n'\n")
    if answer == 'y':
        hit(user_cards)
        user_total = total_user(user_cards)
        if user_total > 21:
            print(f"You have: {user_cards}")
            print(f"Your total is {user_total}\n")
            dealer_cards.remove("?")
            hit(dealer_cards)
            dealer_total = total_user(dealer_cards)
            print(f"Dealer has: {dealer_cards}")
            print(f"Dealer total is {dealer_total}\n")
            print("Bust")
            sys.exit(0)

    if answer == 'n':
        dealer_cards.remove("?")
        hit(dealer_cards)
        dealer_total = total_user(dealer_cards)
        while dealer_total < 17:
            dealer_total = total_user(dealer_cards)
            if dealer_total > 21:
                print(f"Dealer has: {dealer_cards}")
                print(f"Dealer total is {dealer_total}\n")


            if dealer_total < 21:
                hit(dealer_cards)
                print(f"Dealer total is {dealer_total}")
                print(f"Dealer has: {dealer_cards}")


        break


if dealer_total == user_total:
    print("Draw")

elif dealer_total > user_total:
    if dealer_total > 21:
        print("Dealer Bust")
    else:
        print("Dealer Wins")

elif user_total > dealer_total:
    print("User Wins")