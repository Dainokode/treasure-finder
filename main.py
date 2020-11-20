print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____/__
******************************************************************************* ''')

print("Welcome to Treasure Island. Your mission is to find the treasure.")

choice1 = input("You are at a crossroads, where do you go, left or right?")

if choice1.lower() == "right":
    print("Fall into a hole. Game Over.")
elif choice1.lower() == "left":
    choice2 = input("You come to a lake. Type wait to 'wait' for a boat or type 'swim' to try to swim.")
    if choice2.lower() == "swim":
        print("Attacked by a giant shark. Game Over")
    elif choice2.lower() == "wait":
        choice3 = input("You arrive on an island unharmed. There is a small house with three doors: red, yellow and blue, which one do you choose?")
        if choice3.lower() == "red":
            print("Burned by fire. Game Over")
        elif choice3.lower() == "blue":
            print("Fall into a hole. Game Over")
        elif choice3.lower() == "yellow":
            print("Congratulations, you found the treasure!")