import random

name = "kajihara"

while True:
    random_letter = random.choice("abcdefghijklmnopqrstuvwxyz")
    print(random_letter)

    if random_letter.lower() == name[0].lower():
        print("Found the initial letter of your name!")
        break
