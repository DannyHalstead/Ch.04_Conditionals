# Sign your name: Danny H

  #1. Make the following program work.

midichlorians = float(input("Enter midichlorian count: "))
if midichlorians > 10000:
    print("You have serious Jedi potential")
else:
    print("Jedi, you will never be.")

    # 2. Make the following program work.

x = float(input("Enter a number: "))
if x == 3:
    print("You entered 3.")
else:
    print("You did not enter 3.")

# 3. Make the following program work.

answer = str(input("What is the name of Poe Dameron's Droid? "))
if answer.upper() == "BB8":
    print("Correct!")
else:
    print("Incorrect! It is BB8.")

    # 4. Make the following program work.

x = str(input("Name one of the top 3 greatest Jedi."))
if x == "Yoda" or x == "Luke Skywalker" or x == "Obi-Wan Kenobi":
    print ("That is correct!")
else:
    print("That is wrong.")

# 5. Make the following program work whether they enter a, A, Jedi Master or jedi master
#    Print "Not a choice!" if they don't choose any of the three and set sensitivity to blank text.

print("Welcome to the Jedi Academy!")

print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")

user_input = str(input("Choose a character."))
sentence.strip(user_input)

if user_input.lower() == "a" or user_input.lower(). == "jedimaster":
    sensitivity = 1000
elif user_input.lower() == "b" or user_input.lower() == "sith lord":
    sensitivity = 900
elif user_input.lower() == "c" or user_input.lower() == "droid":
    sensitivity = 0
else:
    print ("Not a choice.")
    sensitivity = None

print("Your sensitivity is", sensitivity)