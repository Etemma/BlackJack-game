def operation():
    import random
    import os
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    print("Welcome to my game of BlackJack, all rules apply!!!")
    print()
    user = []
    x = 2
    while x > 0:
        user.append(random.choice(cards))
        x -= 1

    computer = []
    x = 2
    while x > 0:
        computer.append(random.choice(cards))
        x -= 1

    def sum(y):
        i = 0
        for x in (y):
            i += x
        return i
    i = sum(user)

    if i < 14:
        user.append(random.choice(cards))
    x = sum(user)

    print(f'Your cards: {user}, current score: {x}, dealers first card {computer[0]}')
    print()
    option= input("Type 'y' to get another card, 'n' to pass:  ")
    print()
    if option == 'y':
        user.append(random.choice(cards))
        x = sum(user)
    d = sum(computer)
    if d < 14:
        computer.append(random.choice(cards))
    d = sum(computer)

    print(f'Your final hand: {user}, final score: {x}')
    print()
    print(f'computer\'s final hand: {computer}, final score: {d}')
    print()

    def result(x, d):
        if x > 21:
            return ("You went over, you losee :(")
        elif x == d:
            return ("Game is a draw")
        elif x < d:
            return ("You scored less, you lose :(")
        else:
            return ('You win :)')
    print(result(x,d))
    print()
    game = input("Do you want to play a game of Blackjack? 'y' or 'n':  ")
    if game == 'y':
        #Clear Console screen
        cls = lambda: os.system('cls')
        cls()
        operation()
    else:
        return
operation()