import os

clear = lambda: os.system('cls')

bidding = True

bids = {}

def find_highest_bidder(bid_record):
    highest_bid = 0
    winner = ""

    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while bidding:
    print("Welcome to the Silent Auction Program.")

    username = input("What is your name?: ")
    userbid = input("What is your bid?: $")
    morebids = input("Are there any more bidders? Type 'yes' or 'no'.\n")

    bids[username] = int(userbid)

    if morebids == "yes":
        print(bids)
        clear()


    elif morebids == "no":
        find_highest_bidder(bids)
        bidding = False
