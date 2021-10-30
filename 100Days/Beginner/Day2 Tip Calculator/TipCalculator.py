import sys


def tip_calculate():
    print("Welcome to the tip calculator.")
    bill_total = input("What was the total bill? $")
    people = input("How many people to split the bill? ")
    select_percent = input("What percentage tip would you like to give? ")
    percent = float(select_percent)/float(100)
    tip_amount = float(bill_total) * percent
    portion = (float(bill_total) + float(tip_amount)) / float(people)
    print(f"Each person should pay: ${portion}")
    answer = input("\n\nCalculate another tip? ")

    if answer == "yes":
        print("\n")
        tip_calculate()
    else:
        sys.exit(0)

while True:
    tip_calculate()