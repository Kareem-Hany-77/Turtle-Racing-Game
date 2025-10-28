import turtle
import time
import random

WIDTH, HEIGHT = 800, 600
COLORS = ["red", "green", "blue", "yellow", "magenta", "cyan", "brown", "black", "orange", "gray"]

def get_number():
    while True:
        print("===============================================")
        print("==========WELCOME TO TURTLES GAME==============")
        print("===============================================")
        number = (input("Enter Numbers of Turtles (2-10) : "))
        print("===============================================")

        if number.isdigit():
            number = int(number)
        else:
            print("Invalid Input")
            continue

        if 2 <= number <= 10:
            return number
        else:
            print("Invalid Input")

def race(colors):
    turtles = create_turtle(colors)

    while True:
        for number in turtles:
            distance = random.randrange(1, 20)
            number.forward(distance)
            x, y = number.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(number)]

def create_turtle(colors):
    turtles = []
    spacing = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        number = turtle.Turtle()
        number.color(color)
        number.shape("turtle")
        number.left(90)
        number.penup()
        number.setpos( -WIDTH // 2+ (i+1) *spacing, -HEIGHT//2 + 20)
        number.pendown()
        turtles.append(number)

    return turtles

def init_turtle():
    turtle.clearscreen()
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing")

def get_color(colors):
    while True:
        print("Bet on which color?")
        for color in colors:
            print(color)
        bet_color = input("Enter your color : ").lower()

        if bet_color in colors:
            return bet_color
        else:
            print("Invalid color, please choose from the list.")

def get_bet(balance):
    while True:
        bet_money = (input("Enter your bet : "))

        if bet_money.isdigit():
            bet_money = int(bet_money)
        else:
            print("Invalid Input")
            continue

        if bet_money <= balance:
            return bet_money
        else:
            print("Invalid bet.")

def check_bet(number, winner, balance, choose_color, choose_money):
    if choose_color == winner:
        return balance + (choose_money * number)
    else:
        return balance - choose_money

def main():
    balance = 100
    is_racing = True

    while is_racing:
        colors = COLORS
        print("===============================================")
        print(f"UR balance is = ${balance}")
        number = get_number()
        init_turtle()
        random.shuffle(COLORS)
        colors = COLORS[:number]
        choose_color = get_color(colors)
        choose_money = get_bet(balance)
        winner = race(colors)
        print("===============================================")
        print(F"THE WINNER IS.... : {winner}")
        print("===============================================")
        balance = check_bet(number, winner, balance, choose_color, choose_money)
        print(f"UR balance is = ${balance:}")
        time.sleep(3)
        if balance == 0:
            print("Sorry.UR out of $$$")
            print("===============================================")
            is_racing = False
            break

        while True:
            again = input("Do you want to play again? (y/n) : ")
            if again.lower() == "y":
                break
            elif again.lower() == "n":
                is_racing = False
                break
            else:
                print("Invalid Input")

if __name__ == "__main__":
    main()