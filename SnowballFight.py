''' 
    Name: Snowball-Mania
    Author: Zayin D
    Date: 12/3/24
    Class: AP Computer Science Principles
    Python: 3.11.5
'''

import random
import time

def main():
    # the main runner of the game
	# welcome the player, gather names, and run the snowball fight!
    print("Welcome to Snowball Mania!")
    name = input("What is your name?  ")
    print("Great to have you here, " + name + "! Who do you want to play against?  ")
    opp = input()
    print(name + " vs. " + opp)
    players = []
    players.append(name)
    players.append(opp)
    nextPlayer = ""

    while (nextPlayer != "Complete"):
        nextPlayer = input("If there are any more Opps, please enter their names one at a time, when done type Complete. ")
        players.append(nextPlayer)
    players.remove("Complete")

    manual = input("Do you want to choose who you throw the snowball at? (Yes or No)  ")

    gameplay(name, players, manual)

def gameplay(name, players, manual):
    while (len(players) >1):
        starter = random.choice(players)
        if (starter == name):
            if (manual == "Yes" and len(players) <= 2):
                print (players)
                target = input("Select the opp to throw a snowball at - ")
            else:
                target = random.choice(players)
                while target == starter:
                    target = random.choice(players)
        else:
            target = random.choice(players)
            while target == starter:
                target = random.choice(players)
        print (starter + " is throwing a snowball at " + target + "!")
        hitNum = random.randint(1, 8)
        success = hitResult(hitNum)
        time.sleep(1)
        if (success == True):
            print ("⚪    ")
            print ("..⚪  ")
            print ("..'.''⚪  ")
            print ("..'.''-'💦")
            print("It's a hit! " + target + " is down!")
            print ("")
            players.remove(target)
        elif (success == "Hurt"):
            print ("⚪    ")
            print ("..⚪  ")
            print ("..'.''⚪  ")
            print ("..'.''-.⚪  ")
            print("A tough shot... " + target + " got grazed")
            print ("")
        elif (success == "Fail"):
            print ("⚪    ")
            print ("..⚪  ")
            print ("..'.''⚪  ")
            print ("You hurt your shoulder and missed...")
            print ("")
        elif (success == "quiet"):
            print (starter + " backs down and all is quiet, lucky")
            print ("Currently alive: " + str(players))
            print ("")
            time.sleep(3)
        else:
            print ("⚪    ")
            print ("..⚪  ")
            print ("..'.''⚪  ")
            print (starter + " kind of sucks, so " + target + " was able to escape from your terrible grasp")
            print ("")
        time.sleep(0.5)
    print(players[0] + " is the winner!")


def hitResult(hitNum):
    # based on the number that is passed in, return True or False 
    # indicating if this was a hit or a miss
    if (hitNum == 1):
        return True
    if (hitNum == 4):
        return "Hurt"
    if (hitNum == 6):
        return "Fail"
    if (hitNum == 3):
        return "quiet"
    return False

main()
