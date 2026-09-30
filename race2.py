#Create a racing program with **8 racers stored in a list**.
#Each racer should randomly get a finishing time between **50 and 100 seconds**.
#Use a **`for` loop** so you do not have to write the same code separately for every racer.
#Your program should:
#- Go through every racer using a `for` loop.
#- Give each racer a random finishing time.
#- Print something like `Foxy finished in 67 seconds`.
#- Store all the finishing times in a second list.
#- After everyone has raced, print every racer's name and their finishing time again.
#**Extra challenge:** Figure out which racer had the fastest time and announce the winner.
#Try to solve it mainly with what you already know plus `for` loops. Don't worry about making the winner calculation elegant yet.

import random

racers=["toad","jon","top","bob","vikram","lucy","luis","duck"]
racersfinishtime=[]
racetime=list(range(50,101))
racetimetemp=0
racewinner=("")
racewinnertime=101


for racer in racers:
    racersfinishtime.append(random.choice(racetime))
    print(f"Announcer: we see that {racer} finished in {racersfinishtime[len(racersfinishtime)-1]}s")
    racetimetemp=racersfinishtime[len(racersfinishtime)-1]
    if(racewinnertime>racersfinishtime[len(racersfinishtime)-1]):
        racewinner=racer
        racewinnertime=racersfinishtime[len(racersfinishtime)-1]
print(f"Announcer: and the winner is {racewinner} with an amazing time of {racewinnertime}s")

    