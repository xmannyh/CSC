name = input("Character name: ")
weapon = input("What's your weapon of choice?: ")
potion = input("Favourite drink?: ")

# keeps track of the players health
hp = 100
# keeps track of any additional damage our weapon could do to the enemy
charge = 0
#keeps track of whether or not we should be battling
battle = False

print('While our hero ' + name + 'was out for a walk, they encountered their valentine')
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
        print("You show them how loud it can go and you blow their eardrums. They are enraged and become a valentines monster!")

        # They got it wrong! Engage in the battle!
        battle = True

    # The player chose answer 3
    elif answer == '3':
        #set validAnswer to True to exit the loop
        validAnswer = True
        print("They invite you over for some nachos. +40 hp.")

        # Cheesy goodness increases the helth of the player
        hp = hp + 40

    # The player didn't chose a valid answer. ask again
    else:
        # we haven't recieved valid input yet, ask again
        print('Please enter a valid number')


# keeps track of the enemies health
ehp = 100
#The name of the enemy
enemy = 'Valentines Monster'
# Check if a either the player or the enemy is still alive
# if not lets go to the next part of the game
while hp > 0 and ehp > 0 and battle == True:
    print("===============================================")
    validAnswer = False
    # Check if a valid answer has been given to us, if not, then continue
    while validAnswer != True:
        print("Attack Mode Engaged: ")
        print("1) Stab")
        print('2) Slash')
        print('3) Heal')
        answer = input("Enter 1, 3 or 2: ")

        # The player chose answer 1
        if answer == '1':
            #set validAnswer to True to exit the loop
            validAnswer = True
            print('You stab the ' + enemy + ' with your ' + weapon + '!')

            # the player hit the enemy, so decrease their health
            ehp = ehp - 20 - charge
            # we used the charge in our weapon, so reset it
            charge = 0

        # The player chose answer 2
        elif answer == '2':
            #set validAnswer to True to exit the loop
            validAnswer = True
            print('You slash the ' + enemy + ' with your ' + weapon + '!')

            # the player hit the enemy, so decrease their health
            ehp = ehp - 40 - charge
            # we used the charge in our weapon, so reset it
            charge = 0

        # The player chose answer 3
        elif answer == '3':
            #set validAnswer to True to exit the loop
            validAnswer = True
            print('You drink ' + potion)
            print('It fills you with determination!')

            # the player drank the potion, so increase their health by 20
            hp = hp + 20

        # The player didn't chose a valid answer. ask again
        else:
            print('Please enter a valid number')

    print('-----------------------------------------')
    validAnswer = False
    # Check if a valid answer has been given to us, if not, then continue
    while validAnswer != True:
        print("Monsters turn: ")
        print("1) Counter")
        print('2) Defend')
        print('3) Charge')
        answer = input("Enter 1, 3 or 2: ")

        # The player chose answer 1
        if answer == '1':
            #set validAnswer to True to exit the loop
            validAnswer = True
            print('You counter the ' + enemy + 's crush attack with your ' + weapon + '!')

            # the player got hit, so substract 20 health from yourself
            hp = hp - 20
            # the player hit the enemy, so decrease their health
            ehp = ehp - 10

        # The player chose answer 2
        elif answer == '2':
            #set validAnswer to True to exit the loop
            validAnswer = True
            print('You defend from the ' + enemy + 's crush attack!')

            # the player got hit, so substract 20 health from yourself
            hp = hp - 10

        # The player chose answer 3
        elif answer == '3':
            #set validAnswer to True to exit the loop
            validAnswer = True
            print('You focus your energy into your ' + weapon)

            # the player got hit, so substract 20 health from yourself
            hp = hp - 40
            # the player is charging their weapon, so add a charge to their weapon
            charge = charge + 10

        # The player didn't chose a valid answer. ask again
        else:
            print('Please enter a valid number')

    # print the current status of the player and enemy
    print('**************************************')
    print("HP: "       + str(hp))
    print("Enemy HP: " + str(ehp))
    print("Charge: "   + str(charge))
    print('**************************************')

if ehp <= 0:
    print('You slayed the ogre!')
if hp <= 0:
    print('GAME OVER')
    print('You died')
    exit()


print('=====================STAGE 1 COMPLETE==========================')

# reset things as necessary
battle = False


print('As our hero ' + name + ' continued on their journey, they encountered a stranger the path.')
print('They asked a weird question:')

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
        print('Sometimes the truth hurts. Carry on.')

    # The player chose answer 2
    elif answer == '2':
        #set validAnswer to True to exit the loop
        validAnswer = True
        print("Thats apple! I'll show you who's boss!")

        # They got it wrong! Engage in the battle!
        battle = True

    # The player chose answer 3
    elif answer == '3':
        #set validAnswer to True to exit the loop
        validAnswer = True
        print("Gates = Windows. Let me teach you a lesson!")

        # They got it wrong! Engage in the battle!
        battle = True

    # The player didn't chose a valid answer. ask again
    else:
        # we haven't recieved valid input yet, ask again
        print('Please enter a valid number')

# keeps track of the enemies health
ehp = 100
#The name of the enemy
enemy = 'The Zucc'
# Check if a either the player or the enemy is still alive
# if not lets go to the next part of the game
while hp > 0 and ehp > 0 and battle == True:
    print("===============================================")
    validAnswer = False
    # Check if a valid answer has been given to us, if not, then continue
    while validAnswer != True:
        print("Attack Mode Engaged: ")
        print("1) Stab")
        print('2) Slash')
        print('3) Heal')
        answer = input("Enter 1, 3 or 2: ")

        # The player chose answer 1
        if answer == '1':
            #set validAnswer to True to exit the loop
            validAnswer = True
            print('You stab the ' + enemy + ' with your ' + weapon + '!')

            # the player hit the enemy, so decrease their health
            ehp = ehp - 20 - charge
            # we used the charge in our weapon, so reset it
            charge = 0

        # The player chose answer 2
        elif answer == '2':
            #set validAnswer to True to exit the loop
            validAnswer = True
            print('You slash the ' + enemy + ' with your ' + weapon + '!')

            # the player hit the enemy, so decrease their health
            ehp = ehp - 40 - charge
            # we used the charge in our weapon, so reset it
            charge = 0

        # The player chose answer 3
        elif answer == '3':
            #set validAnswer to True to exit the loop
            validAnswer = True
            print('You drink ' + potion)
            print('It fills you with determination!')

            # the player drank the potion, so increase their health by 20
            hp = hp + 20

        # The player didn't chose a valid answer. ask again
        else:
            print('Please enter a valid number')

    print('-----------------------------------------')
    validAnswer = False
    # Check if a valid answer has been given to us, if not, then continue
    while validAnswer != True:
        print(enemy + "s turn: ")
        print("1) Counter")
        print('2) Defend')
        print('3) Charge')
        answer = input("Enter 1, 3 or 2: ")

        # The player chose answer 1
        if answer == '1':
            #set validAnswer to True to exit the loop
            validAnswer = True
            print('You counter the ' + enemy + 's crush attack with your ' + weapon + '!')

            # the player got hit, so substract 20 health from yourself
            hp = hp - 20
            # the player hit the enemy, so decrease their health
            ehp = ehp - 10

        # The player chose answer 2
        elif answer == '2':
            #set validAnswer to True to exit the loop
            validAnswer = True
            print('You defend from the ' + enemy + 's crush attack!')

            # the player got hit, so substract 20 health from yourself
            hp = hp - 10

        # The player chose answer 3
        elif answer == '3':
            #set validAnswer to True to exit the loop
            validAnswer = True
            print('You focus your energy into your ' + weapon)

            # the player got hit, so substract 20 health from yourself
            hp = hp - 40
            # the player is charging their weapon, so add a charge to their weapon
            charge = charge + 10

        # The player didn't chose a valid answer. ask again
        else:
            print('Please enter a valid number')

    # print the current status of the player and enemy
    print('**************************************')
    print("HP: "       + str(hp))
    print("Enemy HP: " + str(ehp))
    print("Charge: "   + str(charge))
    print('**************************************')

if ehp <= 0:
    print('You slayed ' + enemy + '!')
if hp <= 0:
    print('GAME OVER')
    print('You died')
    exit()

print('=====================STAGE 2 COMPLETE==========================')
print('Congratulations! ' + name + ' was able to pass all the trials!')
