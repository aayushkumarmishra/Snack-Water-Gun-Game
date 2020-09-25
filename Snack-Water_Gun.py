import random
lst = ['s','W','g']

chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0

print("\t \t \t \t Snack,Water,Gun Game\n \n")
print("s for snack \nw for water \ng for gun \n")

# making the game in while
while no_of_chance < chance:
    _input = input('Snack,Water,Gun: ')
    _random = random.choice(lst)

    if _input == _random:
        print("Tie Both 0 point to each \n ")

        # if user enter (s) for snack
    elif _input == "s" and _random == "g":
        computer_point = computer_point +1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    elif _input == "s" and _random == "w":
        human_point = human_point + 1
        print(f"your guess  {_input}  and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer-point is {computer_point} and your point is {human_point} \n")

        # if user enter (w) for water
    elif _input == "w" and _random == "s":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your points is {human_point} \n")

    elif _input == "w" and _random == "g":
        human_point = human_point +1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

        # if user enter (g) for gun

    elif _input == "g" and _random == "s":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your points is {human_point} \n")

    elif _input == "g" and _random == "w":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your points is {human_point} \n")

    else:
        print("you have input wrong \n")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")

print("GAME OVER")

if computer_point == human_point:
    print("Tie")

elif computer_point > human_point:
    print("computer wins and you loose")

else:
    print("you win and computer loose")

    print(f"your point is {human_point} and computer points is {computer_point}")