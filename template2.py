print('Welcome to the Quiz bowl!')
print("Here are the rules:")
print("1) You've got 3 lives. Once you've hit zero. It's done. GAME OVER.")
print("2) You can not cheat. There are no outside sources allowed. And you cannot share the answer's with fellow contestants.")

print("Let's begin!")

# lives keeps track of how many answers we have gotten wrong.
lives = 3

print("===============================================")
validAnswer = False
# Check if a valid answer has been given to us, if not, then continue
while validAnswer != True:
    print("How old is Emmanuel?")
    print("1) Old")
    print('2) Really old')
    print('3) Kinda old')
    answer = input("Enter 1, 3 or 2: ")

    # The player chose answer 1
    if answer == '1':
        #set validAnswer to True to exit the loop
        validAnswer = True
        print('Sometimes the truth hurts.')

    # The player chose answer 2
    elif answer == '2':
        #set validAnswer to True to exit the loop
        validAnswer = True
        print("That's just mean. Ya lose a life.")
        lives = lives - 1

    # The player chose answer 3
    elif answer == '3':
        #set validAnswer to True to exit the loop
        validAnswer = True
        print("Glad you think so but he's old. Ya lose a life.")
        lives = lives - 1

    # The player didn't chose a valid answer. ask again
    else:
        print('Please enter a valid number')


print("===============================================")

validAnswer = False
# Check if a valid answer has been given to us, if not, then continue
while validAnswer != True:
    print("What do you give your valentine?")
    print("1) Chocolate")
    print('2) New sound system')
    print('3) Cheese')
    answer = input("Enter 1, 3 or 2: ")

    # The player chose answer 1
    if answer == '1':
        #set validAnswer to True to exit the loop
        validAnswer = True
        print("It's tasty and they appreciate you.")

    # The player chose answer 2
    elif answer == '2':
        #set validAnswer to True to exit the loop
        validAnswer = True
        print("You show them how loud it can go and you blow their eardrums. Ya lose a life.")
        lives = lives - 1

    # The player chose answer 3
    elif answer == '3':
        #set validAnswer to True to exit the loop
        validAnswer = True
        print("They don't know what to do with a block of cheese. Ya lose a life.")
        lives = lives - 1

    # The player didn't chose a valid answer. ask again
    else:
        # we haven't recieved valid input yet, ask again
        print('Please enter a valid number')


print("===============================================")

validAnswer = False
# Check if a valid answer has been given to us, if not, then continue
while validAnswer != True:
    print("Who is the CEO of Facebook?")
    print("1) The Zucc")
    print('2) Steve Jobs')
    print('3) Bill Gates')
    answer = input("Enter 1, 3 or 2: ")

    # The player chose answer 1
    if answer == '1':
        #set validAnswer to True to exit the loop
        validAnswer = True
        print('Sometimes the truth hurts.')

    # The player chose answer 2
    elif answer == '2':
        #set validAnswer to True to exit the loop
        validAnswer = True
        print("Thats apple folks... Ya lose a life.")
        lives = lives - 1

    # The player chose answer 3
    elif answer == '3':
        #set validAnswer to True to exit the loop
        validAnswer = True
        print("Gates = Windows. Ya lose a life.")
        lives = lives - 1

    # The player didn't chose a valid answer. ask again
    else:
        # we haven't recieved valid input yet, ask again
        print('Please enter a valid number')

# If we have run out of lives, then it's game over and we can't see the secret message
if lives == 0:
    print('You cant see the secret message. Try again next time!')
else:
    print('You did it! Congratulations!')
    print('You are a very smart person.')
    print('Thanks for playing!')
