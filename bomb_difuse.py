#your task c: before 5 (17:00 norway time 18th september 2026) 
# if you want to make it cause then i want to talk to you c: 
# you can try to JUST make what i tell you to, don’t get more creative not necessary 
# (i love your creativity tho but it will take you long then) 
# if you don’t have time gotta leave it to saturday, need my cutie time🫢 
# not allowed to use AI i will question you about it c:


#it will be like deactivate the bomb kinda, 
# and you will have 60 seconds to solve x amount of math problems 
# (simple ones like idk division multiplication add etc, 
# hint:you can generate with the random dlc the numbers to add and then use the operators) 
# if it’s right answer then you add bonus seconds c: but if wrong is 10 seconds penalty or something 
# (: you loose you die, but if you solve all the problems you win :D

import random
import time
startingtime=time.time()
addtime=0

retry=1
while(retry==1):

    bomb=60
    bombdefuse=0


    while(bomb>0 or bomb>0 and bombdefuse==10):
        print(f"the bomb will explode in {bomb}s")
        question=random.randint(1,3)
        if(question==1):
                addisjon1=random.randint(1,50)
                addisjon2=random.randint(1,50)
                questionad=int(input(f"what is {addisjon1}+{addisjon2}?     ="))
                if(questionad==addisjon1+addisjon2):
                    bomb+=5
                    addtime+=5
                    bombdefuse+=1
                    print(f"+1 defuse\n+5 time\{bomb}s left")
                elif(questionad!=addisjon1+addisjon2):
                    bomb-=5
                    addtime-=5
        elif(question==2):
            #subtraction
            subtrack1=random.randint(10,20)
            subtrack2=random.randint(1,10)
            questionsub=int(input(f"what is {subtrack1}-{subtrack2}?     ="))
            if(questionsub==subtrack1-subtrack2):
                bomb+=5
                addtime+=5
                bombdefuse+=1
                print(f"+1 defuse\n+5 time\{bomb}s left")
            elif(questionsub!=subtrack1-subtrack2):
                bomb-=5
                addtime-=5
        elif(question==0):
            #divisjon=temporary not working
            divi1=random.random(10,20,30,40,50,60,70,80,90,100)
            divi2=random.random(2,4,5,6,8,10)
            questiondiv=int(input(f"what is {divi1}/{divi2}?     ="))
            if(questiondiv==divi1/divi2):
                bomb+=5
                addtime+=5
                bombdefuse+=1
                print(f"+1 defuse\n+5 time\{bomb}s left")
            elif(questiondiv!=divi1/divi2):
                bomb-=5
                addtime-=5
        elif(question==3):
            #multiplication
            mult1=random.randint(1,10)
            mult2=random.randint(1,10)
            questionmult=int(input(f"what is {mult1}*{mult2}?     ="))
            if(questionmult==mult1*mult2):
                bomb+=5
                addtime+=5
                bombdefuse+=1
                print(f"+1 defuse\n+5 time\{bomb}s left")
            elif(questionmult!=mult1*mult2):
                bomb-=5
                addtime-=5
        currenttime=time.time()-startingtime
        bomb=bomb+addtime-currenttime
        time.sleep=1
    if(bomb<=0 and bombdefuse<10):
        print("booooomb\nyou lost")
        retrylost=input("want to retry? \n Type yes or 1 to retry, and anything else if not    :")
        if(retrylost=="yes" or retrylost=="1"):
            retry==1
        else:
            retry=0
    else:
        print("bomb defused \n congratulations, but I think you just got lucky")
        retrywin=input("want to retry? \n Type yes or 1 to retry, and anything else if not    :")
        if(retrylost=="yes" or retrylost=="1"):
            retry==1
        else:
            retry=0
print("thank you for playing")