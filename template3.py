name = input("Character name: ")
weapon = input("What's your weapon of choice?: ")
potion = input("Favourite drink?: ")
enemy = input("What're you most afraid of?: ")

# keeps track of the players health
hp = 100
# keeps track of the enemies health
ehp = 100
# keeps track of any additional damage our weapon could do to the enemy
charge = 0


validAnswer = False
# Check if a valid answer has been given to us, if not, then continue
while validAnswer != True:
    print("chose your difficulty: ")
    print("1) Easy")
    print('2) Medium')
    print('3) Hard')
    answer = input("Enter 1, 3 or 2: ")

    # The player chose answer 1
    if answer == '1':
        #set validAnswer to True to exit the loop
        validAnswer = True
        print('Tactics disabled')

        # we chose easy, so bring down the enemy hp
        ehp = 50

    # The player chose answer 2
    elif answer == '2':
        #set validAnswer to True to exit the loop
        validAnswer = True
        print('Welcome to the playground')

        # we chose medium, so bring down the enemy hp
        ehp = 75

    # The player chose answer 3
    elif answer == '3':
        #set validAnswer to True to exit the loop
        validAnswer = True
        print('I hope you brought a first-aid kit')

        # we chose hard, so show no mercy!
        ehp = 200

    # The player didn't chose a valid answer. ask again
    else:
        print('please enter a valid number')

print('You encounter a ' + enemy + '!')

# Check if a either the player or the enemy is still alive
# if not lets go to the next part of the game
while hp > 0 and ehp > 0:
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
            print('You counter the ' + enemy + ' with your ' + weapon + '!')

            # the player got hit, so substract 20 health from yourself
            hp = hp - 20
            # the player hit the enemy, so decrease their health
            ehp = ehp - 10

        # The player chose answer 2
        elif answer == '2':
            #set validAnswer to True to exit the loop
            validAnswer = True
            print('You defend from the ' + enemy + 's attack!')

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
else:
    print('You win!')
