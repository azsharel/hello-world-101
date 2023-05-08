import random


def main():
    balance = get_balance()
    bet = get_bet()
    balance = check_win_or_loss(balance, bet)
    print("Your new balance is: ${}".format(balance))


def get_balance():
    balance = float(input("Enter your current balance: $"))
    return balance


def get_bet():
    bet = float(input("Enter your bet amount: $"))
    return bet


def check_win_or_loss(balance, bet):
    outcome = random.randint(1, 2)

    if outcome == 1:
        print("Congratulations! You won!")
        balance += bet
    else:
        print("Sorry, you lost.")
        balance -= bet

    return balance


main()
