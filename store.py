#it will be like a store, so they ask you what do you want and shows you options

# apples - 1
# oranges - 2
# bananas - 3

# it can be others just showing you the options. Then the user types one of those options and lets say types 1, so then it says "how many apples do you want" and then type the number

# then calculate the price, apples cost 1$ (per apple), organges 2$, bananas 3$ finally show the cost and yes

#Prices
import random
secret_number=random.randint(1,10000)
carrot=1
cucumber=2
ginger=3 
potato=4
cost=0
gambler=0
sin=0
life=1

drugs=100
prostetution=50

name=input("what's my name?     :")
money=int(input("And how much money do I have?    :"))

print(name,":  I need to get to the store")

print("Store owner: Welcome to our store.\n\nWe mainly sell vegetables, but do you have anything special to say before we start?")
Beat_Rice=input("Store owner: So what did you want to say?       :")
if(Beat_Rice=="Beat_Rice"):
    print("Store owner: Oh... So you're here for the secret stash?\n\n Figured out the moment I saw you.\nThis is what we sell, let me know and I'll tell you the price.\n\n1.Gambling\n\n2.Drugs\n\n3.Prostetution")
    answerbad=input("So what which of these would you want? Only pick one btw      :")
    if(answerbad=="1" or answerbad=="gambling" or answerbad=="Gambling"):
        gambler= gambler+1
        print("Store owner: Yeah, you can win big, but be ready to lose as well.")
        bet=int(input("So how much do you want to bet?   :"))
        if(bet==money or bet<money):
            guess=int(input("Guess a number between 1 and 10000 if you're right you win    :"))
            if(guess==secret_number):
                print("you won!! now get out of here!!")
                money= money+ bet*2
            else:
                print("you lost you loser!")
                money= money-bet
        else:
            print("well you don't got the money for that...")
    elif(answerbad=="2" or answerbad=="Drugs" or answerbad=="drugs"):
        sin=sin+1
        print("oh well, I can help you with that. It's gonna cost you tho, are you sure you're ready for that?")
        cost=cost+drugs
    elif(answerbad=="3" or answerbad=="Prostetution" or answerbad=="prostetution"):
        sin=sin+2
        cost=cost+prostetution
        print("Who the hell do you think you are??\n\n Well you are kinda cute I guess, so I tell you what. For some money I will give you the best night ever")
else:
    print("Store owner: These are the vegetables we got today. Don't spend too much time looking and let me know what you want.\n\n1.Carrot\n2.Cucumber\n3.Ginger\n4.Potato")
    answer=input("so what do you want? Remember only pick one      :")
    if(answer=="1" or answer=="Carrot" or answer=="carrot"):
        amount=int(input("how many do you want?"))
        cost=cost+carrot*amount
    elif(answer=="2" or answer=="Cucumber" or answer=="cucumber"):
        amount=int(input("how many do you want?"))
        cost=cost+cucumber*amount
    elif(answer=="3" or answer=="ginger" or answer=="Ginger"):
        amount=int(input("how many do you want?"))
        cost=cost+ginger*amount
    elif(answer=="4" or answer=="Potato" or answer=="potato"):
        amount=int(input("how many do you want?"))
        cost=cost+potato*amount
    else:
        print("learn how to spell!")
        life= life-1


if(gambler==0):
    if(life==1):
        print(money,cost)
        final=input("So are you okay with what you got? answer yes or no     :")
        if(final=="yes" and sin==0):
            money=money-cost
            print(name,"finaly got home with her money they had",money,"$ left")
        elif(final=="no"and sin==0):
            print("okay then get the hell out of here... \n\n",name,"got out of there and went home witouth getting anything",money,"$ left")
        elif(final=="yes" and sin==2):
            print("oh my you're going to love this\n\n",name,"had a wonderful night with the Store owner. They fell madly in love and they kept seeing eachother. \n\n Well that was at least until the police showed up to take both of you.")
            money=0
            print(money,"with no money",name,"spent the rest of their life in jail, but at least the police put you inn wiht your lover the store owner.")
        elif(final=="no" and sin==2):
            print("I knew you were a scumbag from the begining, die!!")
        else:
            print(name,"got shot by the shop owner for being annoying")
    else:
        print(name,"got shot")
else:
    print(name,"got out of there with",money,"$ well hope you're happy with what you did")