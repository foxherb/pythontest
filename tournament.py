#Create a tournament program with 6 fighters stored in a list.
#Each round, randomly choose two different fighters and randomly decide who wins. The loser should be removed from the list, and the program should show who is still in the tournament.
#Keep running rounds until only one fighter remains, then announce that fighter as the champion.
#**Extra challenge:** Create a second list called `eliminated` and add each losing fighter to it. At the end, print the elimination order as well as the champion.

import random
fighters=["Toad","Charls","Sebastian","Frogs","Foxy","Timoty"]
tempfighters=[]
Eliminated=[]
round=0

print(f"Anouncer: Welcome welcome, to this spectatical evining. We got {len(fighters)} champions competing today.\n It's going to be a specactural fight, so get to your seats and lets start this thing!")

while(len(fighters)!=1):
    if(round==0):
        print("Anouncer: Let's start with our first competition, to see whos going to fight agains eachother, let's see who is our lucky first contender")
        tempfighters.append(random.choice(fighters))
        fighters.remove(tempfighters[0])
        tempfighters.append(random.choice(fighters))
        fighters.remove(tempfighters[1])
        Eliminated.append(random.choice(tempfighters))
        tempfighters.remove(Eliminated[0])
        print(f"Anouncer: We see it was a though battle, but {tempfighters[0]} was the one to take the victory and will continue.")
        fighters.append(tempfighters[0])
        tempfighters.remove(tempfighters[0])
        round+=1
    if(round==1):
        while(round==1):
            tempfighters.append(random.choice(fighters))
            fighters.remove(tempfighters[0])
            tempfighters.append(random.choice(fighters))
            fighters.remove(tempfighters[1])
            Eliminated.append(random.choice(tempfighters))
            tempfighters.remove(Eliminated[1])
            print(f"Anouncer: We see it was a though battle, but {tempfighters[0]} was the one to take the victory and will continue.")
            fighters.append(tempfighters[0])
            tempfighters.remove(tempfighters[0])
            round+=1
    if(round==2):
        while(round==2):
            tempfighters.append(random.choice(fighters))
            fighters.remove(tempfighters[0])
            tempfighters.append(random.choice(fighters))
            fighters.remove(tempfighters[1])
            Eliminated.append(random.choice(tempfighters))
            tempfighters.remove(Eliminated[2])
            print(f"Anouncer: We see it was a though battle, but {tempfighters[0]} was the one to take the victory and will continue.")
            fighters.append(tempfighters[0])
            tempfighters.remove(tempfighters[0])
            round+=1
    if(round==3):
        while(round==3):
            tempfighters.append(random.choice(fighters))
            fighters.remove(tempfighters[0])
            tempfighters.append(random.choice(fighters))
            fighters.remove(tempfighters[1])
            Eliminated.append(random.choice(tempfighters))
            tempfighters.remove(Eliminated[3])
            print(f"Anouncer: We see it was a though battle, but {tempfighters[0]} was the one to take the victory and will continue.")
            fighters.append(tempfighters[0])
            tempfighters.remove(tempfighters[0])
            round+=1
    if(round==4):
        while(round==4):
            tempfighters.append(random.choice(fighters))
            fighters.remove(tempfighters[0])
            tempfighters.append(random.choice(fighters))
            fighters.remove(tempfighters[1])
            Eliminated.append(random.choice(tempfighters))
            tempfighters.remove(Eliminated[4])
            print(f"Anouncer: We see it was a though battle, but {tempfighters[0]} was the one to take the victory and will continue.")
            fighters.append(tempfighters[0])
            tempfighters.remove(tempfighters[0])
            round+=1
print(f"Anouncer: and with that we can see that the winner of this competiotion is {fighters[0]}")
print(f"Anouncer: Well as you can see these are the losers {Eliminated} give them an applacue for trying \n and congratulations again to {fighters} for winning today")





