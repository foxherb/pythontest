# Create a training arena with 5 adventurers in a list.
# Each adventurer should complete Strength, Agility, and Intelligence training.
# Each skill gets a random score from 1 to 20.
# Make a function called do_training() that generates the scores and returns the total.
# Use a for loop to send every adventurer through the training.
# Store each adventurer's total score in a second list.
# After everyone finishes, print their names and total scores.
# Finally, find and announce the adventurer with the highest score.
# New things to practice: def and return.

import random

def do_training():
    skillevel=list(range(1,21))
    result=random.choice(skillevel)
    return result


adventurers = ["Foxy", "Bob", "Lucy", "Duck", "Vikram"]
strength=[]
agility=[]
intelligence=[]



for adventurer in adventurers:
    strength.append(do_training())
    if(strength[len(strength)-1]!=1 or strength[len(strength)-1]!=20):
        print(f"Announcer: Our adventurer {adventurer} got {strength[len(strength)-1]} strenght")
    elif(strength[len(strength)-1]==1):
        print(f"Announcer: Our adventurer {adventurer} got a critical fail with only {strength[len(strength)-1]} strength")
    elif(strength[len(strength)-1]==20):
        print(f"Announcer: Our adventurer {adventurer} got a critical sucsess with {strength[len(strength)-1]} strength")
    agility.append(do_training())
    if(agility[len(agility)-1]!=1 or agility[len(agility)-1]!=20):
        print(f"Announcer: Our adventurer {adventurer} got {agility[len(agility)-1]} agility")
    elif(agility[len(agility)-1]==1):
        print(f"Announcer: Our adventurer {adventurer} got a critical fail with only {agility[len(agility)-1]} agility")
    elif(agility[len(agility)-1]==20):
        print(f"Announcer: Our adventurer {adventurer} got a critical sucsess with {agility[len(agility)-1]} agility")    
    intelligence.append(do_training())
    if(intelligence[len(intelligence)-1]!=1 or intelligence[len(intelligence)-1]!=20):
        print(f"Announcer: Our adventurer {adventurer} got {intelligence[len(intelligence)-1]} intelligence")
    elif(intelligence[len(intelligence)-1]==1):
        print(f"Announcer: Our adventurer {adventurer} got a critical fail with only {intelligence[len(intelligence)-1]} intelligence")
    elif(intelligence[len(intelligence)-1]==20):
        print(f"Announcer: Our adventurer {adventurer} got a critical sucsess with {intelligence[len(intelligence)-1]} intelligence")

#was too hard so I'm stopping this one for now, didn't completly understand functions with this excersise as of now