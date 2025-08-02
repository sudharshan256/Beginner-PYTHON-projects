import random

number=random.randint(1,100)
print("This is number game")

while True:
    turn=int(input("Enter your number:"))

    if turn < number:
        print("Need more")
    elif turn > number:
        print("Need less")
    else:
        print("mission passed, you found the number")
        break
