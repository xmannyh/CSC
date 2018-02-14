name = input("Character name: ")
weapon = input("What's your weapon of choice?: ")
potion = input("Favourite drink?: ")
enemy = input("What're you most afraid of?: ")
hp = 100
ehp = 100
charge = 0
print(name, weapon)

validAnswer = False
while validAnswer != True:
    print("Choose your difficulty: ")
    print("1) Easy")
    print('2) Medium')
    print('3) Hard')
    answer = input("Enter 1, 3 or 2: ")
    if answer == '1':
        validAnswer = True
        print('Tactics disabled')
        ehp = 50
    elif answer == '2':
        validAnswer = True
        print('Welcome to the playground')
        ehp = 75
    elif answer == '3':
        validAnswer = True
        print('I hope you brought a first-aid kit')
        ehp = 200
    else:
        print('please enter a valid number')

print('You encounter a ' + enemy + '!')

while hp > 0 and ehp > 0:
    print("===============================================")
    validAnswer = False
    while validAnswer != True:
        print("Attack Mode Engaged: ")
        print("1) Stab")
        print('2) Slash')
        print('3) Heal')
        answer = input("Enter 1, 3 or 2: ")
        if answer == '1':
            validAnswer = True
            print('You stab the ' + enemy + ' with your ' + weapon + '!')
            ehp = ehp - 20 - charge
            charge = 0
        elif answer == '2':
            validAnswer = True
            print('You slash the ' + enemy + ' with your ' + weapon + '!')
            ehp = ehp - 40 - charge
            charge = 0
        elif answer == '3':
            validAnswer = True
            print('You drink ' + potion)
            print('It fills you with determination!')
            hp = hp + 20
        else:
            print('Please enter a valid number')

    print('-----------------------------------------')
    validAnswer = False
    while validAnswer != True:
        print("Monsters turn: ")
        print("1) Counter")
        print('2) Defend')
        print('3) Charge')
        answer = input("Enter 1, 3 or 2: ")
        if answer == '1':
            validAnswer = True
            print('You stab the ' + enemy + ' with your ' + weapon + '!')
            hp = hp - 20
            ehp = ehp - 10
        elif answer == '2':
            validAnswer = True
            print('You slash the ' + enemy + ' with your ' + weapon + '!')
            hp = hp - 10
        elif answer == '3':
            validAnswer = True
            print('You focus your energy into your ' + weapon)
            hp = hp - 40
            charge = 10
        else:
            print('Please enter a valid number')

    print('**************************************')
    print("HP: " + str(hp))
    print("Enemy HP: " + str(ehp))
    print("Charge: " + str(charge))
    print('**************************************')

if ehp <= 0:
    print('You slayed the ogre!')
if hp <= 0:
    print('GAME OVER')
    print('You died')
else:
    print('You win!')
