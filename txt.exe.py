'''
    Software Engineer: Martin Belt
    Date: 10/14/18
    Time: 6:47 PM CST
    Program: txt.exe

    Co-Developer: George W. F. Downing
    Joined: 10/25/18
    Time: 9:05 AM CST
'''
import time
import random
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)

Strength = random.randint(0, 100)
Dexterity = random.randint(0, 100)
Willpower = random.randint(0, 100)
Agility = random.randint(0, 100)



delay_print ("You are surrounded in darkness. Everything that you see is dark and confusing. ")
delay_print("A warm light surrounds you and you hear a voice:\n")
name = input("Who are you, Adventurer?\n")
nickName = input("What is your nickname, " + name + "?\n")
time.sleep(1)
delay_print(name + "...that is a good, strong name.")
delay_print(" You have a choice, " + nickName + ". You can become the fabled hero of Falte or you can die in the process.")
delay_print(" I will now transport you into the country of Falte...\n")
time.sleep(6)
delay_print("You wake up in a pool of soothing water. Your memory is hazy, at best, and you can't seem to figure out where you are.")
delay_print(" As you look around, you can't seem to figure out what your body looks like. You try to remember...\n")
print("-------------------------------------------------------\n")

delay_print("As you inspect what little you can see of your body, you remember that you are...\n")
gender = input("What is your gender?\n")
if (gender == 'Female'):
   delay_print("Right. You remember your feminine charms and whims. You are a woman.\n")
if (gender == 'Male'):
   delay_print("Right. You remember your manly muscles and all your feats of strength. You are a man.\n\n")

raceList = [' ', 'Orc', 'Human', 'Elf', 'Dwarf', '']

time.sleep(6)

for i in range(1, 6):
    print(raceList[i])
    print("\n")
    
    
race = input("What is your race, " + name + ". (Type in a race)\n")
delay_print("Yes. That's right. You're a(n) " + race + ".")
time.sleep(5)
if race == 'Elf':
    delay_print(" You look around and see that you are in a tent with guards standing outside. They are Elven.")
    if  gender == 'Female':
        delay_print(" You can't help but feel nauseous while in the pool of water.\n")
        response = input("Would you like to get out?\n")
        if response == 'Yes':
            goodResponse = response
            if  goodResponse == 'Yes':
                  print("You get out of the water. There is a dress, a hair clip and a pair of boots.")
        if response == 'No':
            badResponse = response
            while(badResponse == 'No'):
                print("You think that you should stay in the water for a little while longer.\n")
                input("Would you like to get out?\n")
                if  input == 'Yes':
                    pass
                pass
            print("You get out of the water. There is a dress, a hair clip and a pair of boots.")
            A =  input("Would you like to equip these garments?\n")
            if  (A == goodResponse):
                print(" You quickly put the garments on. You are now clothed.")
    if gender == 'Male':
        delay_print("You can't help but feel nauseous while in the pool of water.\n")
        response = input("Would you like to get out?\n")
        if response == 'Yes':
            goodResponse = response
            if  goodResponse == 'Yes':
                  print("You get out of the water. There is a tunic and a pair of boots.")
        if response == 'No':
            badResponse = response
            askAgain = input("Would you like to get out?\n")
            if (askAgain == 'Yes'):
                print(name)
