import os
import pyautogui
def clear():
    os.system('cls') #on Windows System


bids = {}
bidding_finished = False
winner = ""
def find_highest_bidders(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid} ")

while not bidding_finished:
    name = input("\nWhat's your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidders(bids)
    elif should_continue == "yes":
        # clear()
        pyautogui.hotkey('ctrl', 'l')
