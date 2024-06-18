import random


def game():
    print("Welcome to Rock-Paper-Scissors\n")
    print("'r' for Rock, 'p' for paper, 's' for scissors")

    user = input("\nPlease enter your choice\n-->\t").lower()
    computer = random.choice(('r', 'p', 's'))

    print("You VS Computer")
    print(f"\t{user} : {computer}")

    #   r>s, s>p, p>r
    if user == computer:
        print("It is a draw!!")

    elif winning(user, computer):
        print("You win!!")
    else:
        print("You lost!!")


def winning(player1, player2):
    if (player1 == 'r' and player2 == 's') or (player1 == 's' and player2 == 'p') or (player1 == 'p' and player2 == 'r'):
        return True


game()
