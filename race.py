#write a program that simulates a race (you figure out what is in the race). #
# but every car/animal/etc has some hp, so lets say its 10 of them. Randomly they can get attacked an lose some hp, 
# #and the game has to run in a loop until no one is alive or until one of them wins (you figure out the standard for the win). 
# then gotta say who wins and all the parameters (or if everyone loses).

#my notes
# spectetors, statidum, going to the race, start race, race runs until one wins, or all lose. Race until death. Diffrent racers. hp per racer.
# Betting on the racers. winning, money, start wiht a set amount, if you loose you gotta wash dishes to earn money.
# .

#If I need import put here
import random
import time

#Veriables
have_i_opened_internett=0
am_I_interested_in_watching_race_today=1
have_I_watched_a_race_today=0
spectetors_amature=100
spectetors_profesional=10000
spectetors_elite=100000
in_amature_arena=0
in_profesional_arena=0
in_elite_arena=0
player_money=100
normal_amature_race=0
normal_profesional_race=0
gambling_profesional_racer="0"
gambling_profesional_money=0
profesional_winner="0"
favorite_profesional_racer="0"
profesional_potion_offer=0
profesional_ending_no_deaths=0
profesional_ending_few_deaths=0
profesional_ending_many_deaths=0
profesional_ending_only_winner_survived=0
profesional_ending_everyone_died=0

#racers
speed_amature=15
speed_profesional=30
speed_elite=60


#amature racers
amature_racer1_speed=speed_amature+random.randint(-2,3)
amature_racer1_position_x=0
amature_racer1_life=10
amature_racer1_name="nr 1: George"
amature_racer1_fans=0
amature_racer1_fans_excitment=0
amature_racer1_fans_annoyens=0
amature_racer1_is_leader=0

amature_racer2_speed=speed_amature+random.randint(-2,3)
amature_racer2_position_x=0
amature_racer2_life=10
amature_racer2_name="nr 2: Bob"
amature_racer2_fans=0
amature_racer2_fans_excitment=0
amature_racer2_fans_annoyens=0
amature_racer2_is_leader=0

amature_racer3_speed=speed_amature+random.randint(-2,3)
amature_racer3_position_x=0
amature_racer3_life=10
amature_racer3_name="nr 3: Anna"
amature_racer3_fans=0
amature_racer3_fans_excitment=0
amature_racer3_fans_annoyens=0
amature_racer3_is_leader=0

amature_racer4_speed=speed_amature+random.randint(-2,3)
amature_racer4_position_x=0
amature_racer4_life=10
amature_racer4_name="nr 4: Marcus"
amature_racer4_fans=0
amature_racer4_fans_excitment=0
amature_racer4_fans_annoyens=0
amature_racer4_is_leader=0

amature_racer5_speed=speed_amature+random.randint(-2,3)
amature_racer5_position_x=0
amature_racer5_life=10
amature_racer5_name="nr 5: Lily"
amature_racer5_fans=0
amature_racer5_fans_excitment=0
amature_racer5_fans_annoyens=0
amature_racer5_is_leader=0

amature_racer6_speed=speed_amature+random.randint(-2,3)
amature_racer6_position_x=0
amature_racer6_life=10
amature_racer6_name="nr 6: Daniel"
amature_racer6_fans=0
amature_racer6_fans_excitment=0
amature_racer6_fans_annoyens=0
amature_racer6_is_leader=0

amature_racer7_speed=speed_amature+random.randint(-2,3)
amature_racer7_position_x=0
amature_racer7_life=10
amature_racer7_name="nr 7: Sofia"
amature_racer7_fans=0
amature_racer7_fans_excitment=0
amature_racer7_fans_annoyens=0
amature_racer7_is_leader=0

amature_racer8_speed=speed_amature+random.randint(-2,3)
amature_racer8_position_x=0
amature_racer8_life=10
amature_racer8_name="nr 8: Leo"
amature_racer8_fans=0
amature_racer8_fans_excitment=0
amature_racer8_fans_annoyens=0
amature_racer8_is_leader=0

amature_racer9_speed=speed_amature+random.randint(-2,3)
amature_racer9_position_x=0
amature_racer9_life=10
amature_racer9_name="nr 9: Emma"
amature_racer9_fans=0
amature_racer9_fans_excitment=0
amature_racer9_fans_annoyens=0
amature_racer9_is_leader=0

amature_racer10_speed=speed_amature+random.randint(-2,3)
amature_racer10_position_x=0
amature_racer10_life=10
amature_racer10_name="nr 10: Victor"
amature_racer10_fans=0
amature_racer10_fans_excitment=0
amature_racer10_fans_annoyens=0
amature_racer10_is_leader=0

#pro racers
pro_racer_1_speed=speed_profesional+random.randint(-4,4)
pro_racer_1_position_x=0
pro_racer_1_life=10
pro_racer_1_name="nr 1: Alex"
pro_racer_1_fans=0
pro_racer_1_fans_excitment=0
pro_racer_1_fans_annoyens=0
pro_racer_1_is_leader=0

pro_racer_2_speed=speed_profesional+random.randint(-4,4)
pro_racer_2_position_x=0
pro_racer_2_life=10
pro_racer_2_name="nr 2: Mia"
pro_racer_2_fans=0
pro_racer_2_fans_excitment=0
pro_racer_2_fans_annoyens=0
pro_racer_2_is_leader=0

pro_racer_3_speed=speed_profesional+random.randint(-4,4)
pro_racer_3_position_x=0
pro_racer_3_life=10
pro_racer_3_name="nr 3: Lucas"
pro_racer_3_fans=0
pro_racer_3_fans_excitment=0
pro_racer_3_fans_annoyens=0
pro_racer_3_is_leader=0

pro_racer_4_speed=speed_profesional+random.randint(-4,4)
pro_racer_4_position_x=0
pro_racer_4_life=10
pro_racer_4_name="nr 4: Chloe"
pro_racer_4_fans=0
pro_racer_4_fans_excitment=0
pro_racer_4_fans_annoyens=0
pro_racer_4_is_leader=0

pro_racer_5_speed=speed_profesional+random.randint(-4,4)
pro_racer_5_position_x=0
pro_racer_5_life=10
pro_racer_5_name="nr 5: Noah"
pro_racer_5_fans=0
pro_racer_5_fans_excitment=0
pro_racer_5_fans_annoyens=0
pro_racer_5_is_leader=0

pro_racer_6_speed=speed_profesional+random.randint(-4,4)
pro_racer_6_position_x=0
pro_racer_6_life=10
pro_racer_6_name="nr 6: Elena"
pro_racer_6_fans=0
pro_racer_6_fans_excitment=0
pro_racer_6_fans_annoyens=0
pro_racer_6_is_leader=0

pro_racer_7_speed=speed_profesional+random.randint(-4,4)
pro_racer_7_position_x=0
pro_racer_7_life=10
pro_racer_7_name="nr 7: Ethan"
pro_racer_7_fans=0
pro_racer_7_fans_excitment=0
pro_racer_7_fans_annoyens=0
pro_racer_7_is_leader=0

pro_racer_8_speed=speed_profesional+random.randint(-4,4)
pro_racer_8_position_x=0
pro_racer_8_life=10
pro_racer_8_name="nr 8: Isabella"
pro_racer_8_fans=0
pro_racer_8_fans_excitment=0
pro_racer_8_fans_annoyens=0
pro_racer_8_is_leader=0

pro_racer_9_speed=speed_profesional+random.randint(-4,4)
pro_racer_9_position_x=0
pro_racer_9_life=10
pro_racer_9_name="nr 9: Mateo"
pro_racer_9_fans=0
pro_racer_9_fans_excitment=0
pro_racer_9_fans_annoyens=0
pro_racer_9_is_leader=0

pro_racer_10_speed=speed_profesional+random.randint(-4,4)
pro_racer_10_position_x=0
pro_racer_10_life=10
pro_racer_10_name="nr 10: Zoe"
pro_racer_10_fans=0
pro_racer_10_fans_excitment=0
pro_racer_10_fans_annoyens=0
pro_racer_10_is_leader=0

#elite racers
elite_racer_1_speed=speed_elite+random.randint(-10,10)
elite_racer_1_position_x=0
elite_racer_1_life=10

elite_racer_2_speed=speed_elite+random.randint(-10,10)
elite_racer_2_position_x=0
elite_racer_2_life=10

elite_racer_3_speed=speed_elite+random.randint(-10,10)
elite_racer_3_position_x=0
elite_racer_3_life=10

elite_racer_4_speed=speed_elite+random.randint(-10,10)
elite_racer_4_position_x=0
elite_racer_4_life=10

elite_racer_5_speed=speed_elite+random.randint(-10,10)
elite_racer_5_position_x=0
elite_racer_5_life=10

elite_racer_6_speed=speed_elite+random.randint(-10,10)
elite_racer_6_position_x=0
elite_racer_6_life=10

elite_racer_7_speed=speed_elite+random.randint(-10,10)
elite_racer_7_position_x=0
elite_racer_7_life=10

elite_racer_8_speed=speed_elite+random.randint(-10,10)
elite_racer_8_position_x=0
elite_racer_8_life=10

elite_racer_9_speed=speed_elite+random.randint(-10,10)
elite_racer_9_position_x=0
elite_racer_9_life=10

elite_racer_10_speed=speed_elite+random.randint(-10,10)
elite_racer_10_position_x=0
elite_racer_10_life=10


#code start?
name=input("What's your name?      :")

print(name,": Today I really feel like going to a race, let's see where I can watch this.")
while(have_i_opened_internett==0):
    openinternett=input("should I serch online to see where I can watch today?            :").lower()
    if(openinternett=="yes"):
        have_i_opened_internett=1
        print(name,": Wow there are three stadiums that has races today. It seems like they all are to death races. odd...\n Well what can I do, not go? haha ain't happening. They seem kinda simular to be honest\nI think the only real diffrent is in the skill of the racers. There is 1. amuture league, 2. pro league and 3. champions league.")
    elif(openinternett=="no"):
        have_i_opened_internett=1
        am_I_interested_in_watching_race_today=am_I_interested_in_watching_race_today-1
        print(name,": Well when I think about it, I don't really feel like going out today. Let me go to my couch instead.")
    else:
        print("Wait, I think i misspealed. Let me try again.")

if(am_I_interested_in_watching_race_today==1):
    #keepplaying
    while(am_I_interested_in_watching_race_today==1 and have_I_watched_a_race_today==0):
        what_stadium_do_I_go_to=input(f"{name}:  hmm, which one did I want to watch again?").lower()
        if(what_stadium_do_I_go_to=="1" or what_stadium_do_I_go_to=="amature"):
            #code here for amature legua
            print(name,": wow I'm finally at the amature stadium. I think even though there are less people here, there's still going to be fun. And probably a bit less dangerous as well")
            in_amature_arena=1
            have_I_watched_a_race_today=1
            who_does_player_want_to_cheer_on=input(f"{name}: Hmm, who should i root for? I think i saw that these are the ones that are racing\nnr 1: George\nnr 2: Bob \nnr 3: Anna \nnr 4: Marcus \nnr 5: Lily \nnr 6: Daniel \nnr 7: Sofia \nnr 8: Leo \nnr 9: Emma \nnr 10: Victor\nI think I should just type the number btw                     : ")
            if(who_does_player_want_to_cheer_on=="1"):
                amature_racer1_fans+=1
            elif(who_does_player_want_to_cheer_on=="2"):
                amature_racer2_fans+=1
            elif(who_does_player_want_to_cheer_on=="3"):
                amature_racer3_fans+=1
            elif(who_does_player_want_to_cheer_on=="4"):
                amature_racer4_fans+=1
            elif(who_does_player_want_to_cheer_on=="5"):
                amature_racer5_fans+=1
            elif(who_does_player_want_to_cheer_on=="6"):
                amature_racer6_fans+=1
            elif(who_does_player_want_to_cheer_on=="7"):
                amature_racer7_fans+=1
            elif(who_does_player_want_to_cheer_on=="8"):
                amature_racer8_fans+=1
            elif(who_does_player_want_to_cheer_on=="9"):
                amature_racer9_fans+=1
            elif(who_does_player_want_to_cheer_on=="10"):
                amature_racer10_fans+=1
            else:
                print(name,": I think I'd rather just watch from the sideline")

            while(spectetors_amature!=0):
                amature_fans_goes_to=random.randint(1,10)
                if(amature_fans_goes_to==1):
                    amature_racer1_fans+=1
                    spectetors_amature-=1
                elif(amature_fans_goes_to==2):
                    amature_racer2_fans+=1
                    spectetors_amature-=1
                elif(amature_fans_goes_to==3):
                    amature_racer3_fans+=1
                    spectetors_amature-=1
                elif(amature_fans_goes_to==4):
                    amature_racer4_fans+=1
                    spectetors_amature-=1
                elif(amature_fans_goes_to==5):
                    amature_racer5_fans+=1
                    spectetors_amature-=1
                elif(amature_fans_goes_to==6):
                    amature_racer6_fans+=1
                    spectetors_amature-=1
                elif(amature_fans_goes_to==7):
                    amature_racer7_fans+=1
                    spectetors_amature-=1
                elif(amature_fans_goes_to==8):
                    amature_racer8_fans+=1
                    spectetors_amature-=1
                elif(amature_fans_goes_to==9):
                    amature_racer9_fans+=1
                    spectetors_amature-=1
                elif(amature_fans_goes_to==10):
                    amature_racer10_fans+=1
                    spectetors_amature-=1
            while(in_amature_arena==1):
                amature_goal=1000
                if(amature_racer10_life>0):
                    amature_racer10_position_x+=amature_racer10_speed+random.randint(-5,5)
                if(amature_racer9_life>0):
                    amature_racer9_position_x+=amature_racer9_speed+random.randint(-5,5)
                if(amature_racer8_life>0):
                    amature_racer8_position_x+=amature_racer8_speed+random.randint(-5,5)
                if(amature_racer7_life>0):
                    amature_racer7_position_x+=amature_racer7_speed+random.randint(-5,5)
                if(amature_racer6_life>0):
                    amature_racer6_position_x+=amature_racer6_speed+random.randint(-5,5)
                if(amature_racer5_life>0):
                    amature_racer5_position_x+=amature_racer5_speed+random.randint(-5,5)
                if(amature_racer4_life>0):
                    amature_racer4_position_x+=amature_racer4_speed+random.randint(-5,5)
                if(amature_racer3_life>0):
                    amature_racer3_position_x+=amature_racer3_speed+random.randint(-5,5)
                if(amature_racer2_life>0):
                    amature_racer2_position_x+=amature_racer2_speed+random.randint(-5,5)
                if(amature_racer1_life>0):
                    amature_racer1_position_x+=amature_racer1_speed+random.randint(-5,5)

                amature_leader=max(amature_racer10_position_x, amature_racer9_position_x, amature_racer8_position_x, amature_racer7_position_x, amature_racer6_position_x, amature_racer5_position_x, amature_racer4_position_x, amature_racer3_position_x, amature_racer2_position_x, amature_racer1_position_x, )
                if(amature_leader==amature_racer10_position_x):
                    print(f"comentator: {amature_racer10_name} is leading, and is now {amature_goal-amature_leader} meters away from goal")#say which contestent is closest to goal
                    amature_racer10_is_leader=1
                elif(amature_leader==amature_racer9_position_x):
                    print(f"comentator: {amature_racer9_name} is leading, and is now {amature_goal-amature_leader} meters away from goal")
                    amature_racer9_is_leader=1
                elif(amature_leader==amature_racer8_position_x):
                    print(f"comentator: {amature_racer8_name} is leading, and is now {amature_goal-amature_leader} meters away from goal")
                    amature_racer8_is_leader=1
                elif(amature_leader==amature_racer7_position_x):
                    print(f"comentator: {amature_racer7_name} is leading, and is now {amature_goal-amature_leader} meters away from goal")
                    amature_racer7_is_leader=1
                elif(amature_leader==amature_racer6_position_x):
                    print(f"comentator: {amature_racer6_name} is leading, and is now {amature_goal-amature_leader} meters away from goal")
                    amature_racer6_is_leader=1
                elif(amature_leader==amature_racer5_position_x):
                    print(f"comentator: {amature_racer5_name} is leading, and is now {amature_goal-amature_leader} meters away from goal")
                    amature_racer5_is_leader=1
                elif(amature_leader==amature_racer4_position_x):
                    print(f"comentator: {amature_racer4_name} is leading, and is now {amature_goal-amature_leader} meters away from goal")
                    amature_racer4_is_leader=1
                elif(amature_leader==amature_racer3_position_x):
                    print(f"comentator: {amature_racer3_name} is leading, and is now {amature_goal-amature_leader} meters away from goal")
                    amature_racer3_is_leader=1
                elif(amature_leader==amature_racer2_position_x):
                    print(f"comentator: {amature_racer2_name} is leading, and is now {amature_goal-amature_leader} meters away from goal")
                    amature_racer2_is_leader=1
                elif(amature_leader==amature_racer1_position_x):
                    print(f"comentator: {amature_racer1_name} is leading, and is now {amature_goal-amature_leader} meters away from goal")
                    amature_racer1_is_leader=1
                if(amature_leader!=amature_racer1_position_x):
                    amature_racer1_is_leader=0

                if(amature_leader!=amature_racer2_position_x):
                    amature_racer2_is_leader=0

                if(amature_leader!=amature_racer3_position_x):
                    amature_racer3_is_leader=0

                if(amature_leader!=amature_racer4_position_x):
                    amature_racer4_is_leader=0

                if(amature_leader!=amature_racer5_position_x):
                    amature_racer5_is_leader=0

                if(amature_leader!=amature_racer6_position_x):
                    amature_racer6_is_leader=0

                if(amature_leader!=amature_racer7_position_x):
                    amature_racer7_is_leader=0

                if(amature_leader!=amature_racer8_position_x):
                    amature_racer8_is_leader=0

                if(amature_leader!=amature_racer9_position_x):
                    amature_racer9_is_leader=0

                if(amature_leader!=amature_racer10_position_x):
                    amature_racer10_is_leader=0


                
                if(amature_leader-amature_racer10_position_x>0 and amature_racer10_life>0):
                    if(amature_leader-amature_racer10_position_x<10):
                        print(f"comentator: {amature_racer10_name} is close behind, might take the lead")
                        amature_racer10_fans_excitment+=10
                        if(amature_racer10_fans_excitment==100):
                            amature_racer10_speed+=1      
                    elif(10 <= amature_leader - amature_racer10_position_x <= 50):
                        amature_racer10_fans_excitment-=1
                        if(amature_racer10_fans_excitment<0):
                            amature_racer10_fans_excitment=0
                    elif(50<= amature_leader - amature_racer10_position_x <=100):
                        print("comentator: It seems like some of the fans are getting a bit rowdy, hopfully nothing bad will happen")
                    elif(amature_leader-amature_racer10_position_x>100):
                        amature_racer10_speed+=0.2*amature_racer10_fans
                        amature_racer10_fans_annoyens+=1
                        if(amature_racer10_fans_annoyens==100 or amature_racer10_fans_annoyens>100):
                            amature_racer_10_fans_shoot=random.randint(1,1000)
                            if(amature_racer_10_fans_shoot==1):
                                print("PANG!,\n Comentator: OMG! We can see that the leader got shot. May he rest in peac. Anyway we got a race to finish")
                                if(amature_racer1_is_leader):
                                    amature_racer1_life-=10
                                elif(amature_racer2_is_leader):
                                    amature_racer2_life-=10
                                elif(amature_racer3_is_leader):
                                    amature_racer3_life-=10
                                elif(amature_racer4_is_leader):
                                    amature_racer4_life-=10
                                elif(amature_racer5_is_leader):
                                    amature_racer5_life-=10
                                elif(amature_racer6_is_leader):
                                    amature_racer6_life-=10
                                elif(amature_racer7_is_leader):
                                    amature_racer7_life-=10
                                elif(amature_racer8_is_leader):
                                    amature_racer8_life-=10
                                elif(amature_racer9_is_leader):
                                    amature_racer9_life-=10
                                elif(amature_racer10_is_leader):
                                    amature_racer10_life-=10

                #RACER 1 FANS
                if(amature_leader-amature_racer1_position_x>0 and amature_racer1_life>0):
                    if(amature_leader-amature_racer1_position_x<10):
                        print(f"comentator: {amature_racer1_name} is close behind, might take the lead")
                        amature_racer1_fans_excitment+=10
                        if(amature_racer1_fans_excitment==100):
                            amature_racer1_speed+=1

                    elif(10 <= amature_leader-amature_racer1_position_x <= 50):
                        amature_racer1_fans_excitment-=1
                        if(amature_racer1_fans_excitment<0):
                            amature_racer1_fans_excitment=0

                    elif(50 <= amature_leader-amature_racer1_position_x <= 100):
                        print("comentator: It seems like some of the fans are getting a bit rowdy, hopfully nothing bad will happen")

                    elif(amature_leader-amature_racer1_position_x>100):
                        amature_racer1_speed+=0.2*amature_racer1_fans
                        amature_racer1_fans_annoyens+=1

                        if(amature_racer1_fans_annoyens==100):
                            amature_racer_1_fans_shoot=random.randint(1,100000)

                            if(amature_racer_1_fans_shoot==1):
                                print("PANG!,\n Comentator: OMG! We can see that the leader got shot. May he rest in peac. Anyway we got a race to finish")

                                if(amature_racer1_is_leader):
                                    amature_racer1_life-=10
                                elif(amature_racer2_is_leader):
                                    amature_racer2_life-=10
                                elif(amature_racer3_is_leader):
                                    amature_racer3_life-=10
                                elif(amature_racer4_is_leader):
                                    amature_racer4_life-=10
                                elif(amature_racer5_is_leader):
                                    amature_racer5_life-=10
                                elif(amature_racer6_is_leader):
                                    amature_racer6_life-=10
                                elif(amature_racer7_is_leader):
                                    amature_racer7_life-=10
                                elif(amature_racer8_is_leader):
                                    amature_racer8_life-=10
                                elif(amature_racer9_is_leader):
                                    amature_racer9_life-=10
                                elif(amature_racer10_is_leader):
                                    amature_racer10_life-=10


                #RACER 2 FANS
                if(amature_leader-amature_racer2_position_x>0 and amature_racer2_life>0):
                    if(amature_leader-amature_racer2_position_x<10):
                        print(f"comentator: {amature_racer2_name} is close behind, might take the lead")
                        amature_racer2_fans_excitment+=10
                        if(amature_racer2_fans_excitment==100):
                            amature_racer2_speed+=1

                    elif(10 <= amature_leader-amature_racer2_position_x <= 50):
                        amature_racer2_fans_excitment-=1
                        if(amature_racer2_fans_excitment<0):
                            amature_racer2_fans_excitment=0

                    elif(50 <= amature_leader-amature_racer2_position_x <= 100):
                        print("comentator: It seems like some of the fans are getting a bit rowdy, hopfully nothing bad will happen")

                    elif(amature_leader-amature_racer2_position_x>100):
                        amature_racer2_speed+=0.2*amature_racer2_fans
                        amature_racer2_fans_annoyens+=1

                        if(amature_racer2_fans_annoyens==100):
                            amature_racer_2_fans_shoot=random.randint(1,100000)

                            if(amature_racer_2_fans_shoot==1):
                                print("PANG!,\n Comentator: OMG! We can see that the leader got shot. May he rest in peac. Anyway we got a race to finish")

                                if(amature_racer1_is_leader):
                                    amature_racer1_life-=10
                                elif(amature_racer2_is_leader):
                                    amature_racer2_life-=10
                                elif(amature_racer3_is_leader):
                                    amature_racer3_life-=10
                                elif(amature_racer4_is_leader):
                                    amature_racer4_life-=10
                                elif(amature_racer5_is_leader):
                                    amature_racer5_life-=10
                                elif(amature_racer6_is_leader):
                                    amature_racer6_life-=10
                                elif(amature_racer7_is_leader):
                                    amature_racer7_life-=10
                                elif(amature_racer8_is_leader):
                                    amature_racer8_life-=10
                                elif(amature_racer9_is_leader):
                                    amature_racer9_life-=10
                                elif(amature_racer10_is_leader):
                                    amature_racer10_life-=10


                #RACER 3 FANS
                if(amature_leader-amature_racer3_position_x>0 and amature_racer3_life>0):
                    if(amature_leader-amature_racer3_position_x<10):
                        print(f"comentator: {amature_racer3_name} is close behind, might take the lead")
                        amature_racer3_fans_excitment+=10
                        if(amature_racer3_fans_excitment==100):
                            amature_racer3_speed+=1

                    elif(10 <= amature_leader-amature_racer3_position_x <= 50):
                        amature_racer3_fans_excitment-=1
                        if(amature_racer3_fans_excitment<0):
                            amature_racer3_fans_excitment=0

                    elif(50 <= amature_leader-amature_racer3_position_x <= 100):
                        print("comentator: It seems like some of the fans are getting a bit rowdy, hopfully nothing bad will happen")

                    elif(amature_leader-amature_racer3_position_x>100):
                        amature_racer3_speed+=0.2*amature_racer3_fans
                        amature_racer3_fans_annoyens+=1

                        if(amature_racer3_fans_annoyens==100):
                            amature_racer_3_fans_shoot=random.randint(1,100000)

                            if(amature_racer_3_fans_shoot==1):
                                print("PANG!,\n Comentator: OMG! We can see that the leader got shot. May he rest in peac. Anyway we got a race to finish")

                                if(amature_racer1_is_leader):
                                    amature_racer1_life-=10
                                elif(amature_racer2_is_leader):
                                    amature_racer2_life-=10
                                elif(amature_racer3_is_leader):
                                    amature_racer3_life-=10
                                elif(amature_racer4_is_leader):
                                    amature_racer4_life-=10
                                elif(amature_racer5_is_leader):
                                    amature_racer5_life-=10
                                elif(amature_racer6_is_leader):
                                    amature_racer6_life-=10
                                elif(amature_racer7_is_leader):
                                    amature_racer7_life-=10
                                elif(amature_racer8_is_leader):
                                    amature_racer8_life-=10
                                elif(amature_racer9_is_leader):
                                    amature_racer9_life-=10
                                elif(amature_racer10_is_leader):
                                    amature_racer10_life-=10


                #RACER 4 FANS
                if(amature_leader-amature_racer4_position_x>0 and amature_racer4_life>0):
                    if(amature_leader-amature_racer4_position_x<10):
                        print(f"comentator: {amature_racer4_name} is close behind, might take the lead")
                        amature_racer4_fans_excitment+=10
                        if(amature_racer4_fans_excitment==100):
                            amature_racer4_speed+=1

                    elif(10 <= amature_leader-amature_racer4_position_x <= 50):
                        amature_racer4_fans_excitment-=1
                        if(amature_racer4_fans_excitment<0):
                            amature_racer4_fans_excitment=0

                    elif(50 <= amature_leader-amature_racer4_position_x <= 100):
                        print("comentator: It seems like some of the fans are getting a bit rowdy, hopfully nothing bad will happen")

                    elif(amature_leader-amature_racer4_position_x>100):
                        amature_racer4_speed+=0.2*amature_racer4_fans
                        amature_racer4_fans_annoyens+=1

                        if(amature_racer4_fans_annoyens==100):
                            amature_racer_4_fans_shoot=random.randint(1,100000)

                            if(amature_racer_4_fans_shoot==1):
                                print("PANG!,\n Comentator: OMG! We can see that the leader got shot. May he rest in peac. Anyway we got a race to finish")

                                if(amature_racer1_is_leader):
                                    amature_racer1_life-=10
                                elif(amature_racer2_is_leader):
                                    amature_racer2_life-=10
                                elif(amature_racer3_is_leader):
                                    amature_racer3_life-=10
                                elif(amature_racer4_is_leader):
                                    amature_racer4_life-=10
                                elif(amature_racer5_is_leader):
                                    amature_racer5_life-=10
                                elif(amature_racer6_is_leader):
                                    amature_racer6_life-=10
                                elif(amature_racer7_is_leader):
                                    amature_racer7_life-=10
                                elif(amature_racer8_is_leader):
                                    amature_racer8_life-=10
                                elif(amature_racer9_is_leader):
                                    amature_racer9_life-=10
                                elif(amature_racer10_is_leader):
                                    amature_racer10_life-=10


                #RACER 5 FANS
                if(amature_leader-amature_racer5_position_x>0 and amature_racer5_life>0):
                    if(amature_leader-amature_racer5_position_x<10):
                        print(f"comentator: {amature_racer5_name} is close behind, might take the lead")
                        amature_racer5_fans_excitment+=10
                        if(amature_racer5_fans_excitment==100):
                            amature_racer5_speed+=1

                    elif(10 <= amature_leader-amature_racer5_position_x <= 50):
                        amature_racer5_fans_excitment-=1
                        if(amature_racer5_fans_excitment<0):
                            amature_racer5_fans_excitment=0

                    elif(50 <= amature_leader-amature_racer5_position_x <= 100):
                        print("comentator: It seems like some of the fans are getting a bit rowdy, hopfully nothing bad will happen")

                    elif(amature_leader-amature_racer5_position_x>100):
                        amature_racer5_speed+=0.2*amature_racer5_fans
                        amature_racer5_fans_annoyens+=1

                        if(amature_racer5_fans_annoyens==100):
                            amature_racer_5_fans_shoot=random.randint(1,100000)

                            if(amature_racer_5_fans_shoot==1):
                                print("PANG!,\n Comentator: OMG! We can see that the leader got shot. May he rest in peac. Anyway we got a race to finish")

                                if(amature_racer1_is_leader):
                                    amature_racer1_life-=10
                                elif(amature_racer2_is_leader):
                                    amature_racer2_life-=10
                                elif(amature_racer3_is_leader):
                                    amature_racer3_life-=10
                                elif(amature_racer4_is_leader):
                                    amature_racer4_life-=10
                                elif(amature_racer5_is_leader):
                                    amature_racer5_life-=10
                                elif(amature_racer6_is_leader):
                                    amature_racer6_life-=10
                                elif(amature_racer7_is_leader):
                                    amature_racer7_life-=10
                                elif(amature_racer8_is_leader):
                                    amature_racer8_life-=10
                                elif(amature_racer9_is_leader):
                                    amature_racer9_life-=10
                                elif(amature_racer10_is_leader):
                                    amature_racer10_life-=10


                #RACER 6 FANS
                if(amature_leader-amature_racer6_position_x>0 and amature_racer6_life>0):
                    if(amature_leader-amature_racer6_position_x<10):
                        print(f"comentator: {amature_racer6_name} is close behind, might take the lead")
                        amature_racer6_fans_excitment+=10
                        if(amature_racer6_fans_excitment==100):
                            amature_racer6_speed+=1

                    elif(10 <= amature_leader-amature_racer6_position_x <= 50):
                        amature_racer6_fans_excitment-=1
                        if(amature_racer6_fans_excitment<0):
                            amature_racer6_fans_excitment=0

                    elif(50 <= amature_leader-amature_racer6_position_x <= 100):
                        print("comentator: It seems like some of the fans are getting a bit rowdy, hopfully nothing bad will happen")

                    elif(amature_leader-amature_racer6_position_x>100):
                        amature_racer6_speed+=0.2*amature_racer6_fans
                        amature_racer6_fans_annoyens+=1

                        if(amature_racer6_fans_annoyens==100):
                            amature_racer_6_fans_shoot=random.randint(1,100000)

                            if(amature_racer_6_fans_shoot==1):
                                print("PANG!,\n Comentator: OMG! We can see that the leader got shot. May he rest in peac. Anyway we got a race to finish")

                                if(amature_racer1_is_leader):
                                    amature_racer1_life-=10
                                elif(amature_racer2_is_leader):
                                    amature_racer2_life-=10
                                elif(amature_racer3_is_leader):
                                    amature_racer3_life-=10
                                elif(amature_racer4_is_leader):
                                    amature_racer4_life-=10
                                elif(amature_racer5_is_leader):
                                    amature_racer5_life-=10
                                elif(amature_racer6_is_leader):
                                    amature_racer6_life-=10
                                elif(amature_racer7_is_leader):
                                    amature_racer7_life-=10
                                elif(amature_racer8_is_leader):
                                    amature_racer8_life-=10
                                elif(amature_racer9_is_leader):
                                    amature_racer9_life-=10
                                elif(amature_racer10_is_leader):
                                    amature_racer10_life-=10


                #RACER 7 FANS
                if(amature_leader-amature_racer7_position_x>0 and amature_racer7_life>0):
                    if(amature_leader-amature_racer7_position_x<10):
                        print(f"comentator: {amature_racer7_name} is close behind, might take the lead")
                        amature_racer7_fans_excitment+=10
                        if(amature_racer7_fans_excitment==100):
                            amature_racer7_speed+=1

                    elif(10 <= amature_leader-amature_racer7_position_x <= 50):
                        amature_racer7_fans_excitment-=1
                        if(amature_racer7_fans_excitment<0):
                            amature_racer7_fans_excitment=0

                    elif(50 <= amature_leader-amature_racer7_position_x <= 100):
                        print("comentator: It seems like some of the fans are getting a bit rowdy, hopfully nothing bad will happen")

                    elif(amature_leader-amature_racer7_position_x>100):
                        amature_racer7_speed+=0.2*amature_racer7_fans
                        amature_racer7_fans_annoyens+=1

                        if(amature_racer7_fans_annoyens==100):
                            amature_racer_7_fans_shoot=random.randint(1,100000)

                            if(amature_racer_7_fans_shoot==1):
                                print("PANG!,\n Comentator: OMG! We can see that the leader got shot. May he rest in peac. Anyway we got a race to finish")

                                if(amature_racer1_is_leader):
                                    amature_racer1_life-=10
                                elif(amature_racer2_is_leader):
                                    amature_racer2_life-=10
                                elif(amature_racer3_is_leader):
                                    amature_racer3_life-=10
                                elif(amature_racer4_is_leader):
                                    amature_racer4_life-=10
                                elif(amature_racer5_is_leader):
                                    amature_racer5_life-=10
                                elif(amature_racer6_is_leader):
                                    amature_racer6_life-=10
                                elif(amature_racer7_is_leader):
                                    amature_racer7_life-=10
                                elif(amature_racer8_is_leader):
                                    amature_racer8_life-=10
                                elif(amature_racer9_is_leader):
                                    amature_racer9_life-=10
                                elif(amature_racer10_is_leader):
                                    amature_racer10_life-=10


                #RACER 8 FANS
                if(amature_leader-amature_racer8_position_x>0 and amature_racer8_life>0):
                    if(amature_leader-amature_racer8_position_x<10):
                        print(f"comentator: {amature_racer8_name} is close behind, might take the lead")
                        amature_racer8_fans_excitment+=10
                        if(amature_racer8_fans_excitment==100):
                            amature_racer8_speed+=1

                    elif(10 <= amature_leader-amature_racer8_position_x <= 50):
                        amature_racer8_fans_excitment-=1
                        if(amature_racer8_fans_excitment<0):
                            amature_racer8_fans_excitment=0

                    elif(50 <= amature_leader-amature_racer8_position_x <= 100):
                        print("comentator: It seems like some of the fans are getting a bit rowdy, hopfully nothing bad will happen")

                    elif(amature_leader-amature_racer8_position_x>100):
                        amature_racer8_speed+=0.2*amature_racer8_fans
                        amature_racer8_fans_annoyens+=1

                        if(amature_racer8_fans_annoyens==100):
                            amature_racer_8_fans_shoot=random.randint(1,100000)

                            if(amature_racer_8_fans_shoot==1):
                                print("PANG!,\n Comentator: OMG! We can see that the leader got shot. May he rest in peac. Anyway we got a race to finish")

                                if(amature_racer1_is_leader):
                                    amature_racer1_life-=10
                                elif(amature_racer2_is_leader):
                                    amature_racer2_life-=10
                                elif(amature_racer3_is_leader):
                                    amature_racer3_life-=10
                                elif(amature_racer4_is_leader):
                                    amature_racer4_life-=10
                                elif(amature_racer5_is_leader):
                                    amature_racer5_life-=10
                                elif(amature_racer6_is_leader):
                                    amature_racer6_life-=10
                                elif(amature_racer7_is_leader):
                                    amature_racer7_life-=10
                                elif(amature_racer8_is_leader):
                                    amature_racer8_life-=10
                                elif(amature_racer9_is_leader):
                                    amature_racer9_life-=10
                                elif(amature_racer10_is_leader):
                                    amature_racer10_life-=10


                #RACER 9 FANS
                if(amature_leader-amature_racer9_position_x>0 and amature_racer9_life>0):
                    if(amature_leader-amature_racer9_position_x<10):
                        print(f"comentator: {amature_racer9_name} is close behind, might take the lead")
                        amature_racer9_fans_excitment+=10
                        if(amature_racer9_fans_excitment==100):
                            amature_racer9_speed+=1

                    elif(10 <= amature_leader-amature_racer9_position_x <= 50):
                        amature_racer9_fans_excitment-=1
                        if(amature_racer9_fans_excitment<0):
                            amature_racer9_fans_excitment=0

                    elif(50 <= amature_leader-amature_racer9_position_x <= 100):
                        print("comentator: It seems like some of the fans are getting a bit rowdy, hopfully nothing bad will happen")

                    elif(amature_leader-amature_racer9_position_x>100):
                        amature_racer9_speed+=0.2*amature_racer9_fans
                        amature_racer9_fans_annoyens+=1

                        if(amature_racer9_fans_annoyens==100):
                            amature_racer_9_fans_shoot=random.randint(1,100000)

                            if(amature_racer_9_fans_shoot==1):
                                print("PANG!,\n Comentator: OMG! We can see that the leader got shot. May he rest in peac. Anyway we got a race to finish")

                                if(amature_racer1_is_leader):
                                    amature_racer1_life-=10
                                elif(amature_racer2_is_leader):
                                    amature_racer2_life-=10
                                elif(amature_racer3_is_leader):
                                    amature_racer3_life-=10
                                elif(amature_racer4_is_leader):
                                    amature_racer4_life-=10
                                elif(amature_racer5_is_leader):
                                    amature_racer5_life-=10
                                elif(amature_racer6_is_leader):
                                    amature_racer6_life-=10
                                elif(amature_racer7_is_leader):
                                    amature_racer7_life-=10
                                elif(amature_racer8_is_leader):
                                    amature_racer8_life-=10
                                elif(amature_racer9_is_leader):
                                    amature_racer9_life-=10
                                elif(amature_racer10_is_leader):
                                    amature_racer10_life-=10




                                                
                time.sleep(0.2)
                

                if(amature_racer1_life<=0):
                    amature_racer1_speed=0
                    amature_racer1_position_x=-1
                    amature_racer1_is_leader=0
                    amature_racer1_fans=0

                if(amature_racer2_life<=0):
                    amature_racer2_speed=0
                    amature_racer2_position_x=-1
                    amature_racer2_is_leader=0
                    amature_racer2_fans=0

                if(amature_racer3_life<=0):
                    amature_racer3_speed=0
                    amature_racer3_position_x=-1
                    amature_racer3_is_leader=0
                    amature_racer3_fans=0

                if(amature_racer4_life<=0):
                    amature_racer4_speed=0
                    amature_racer4_position_x=-1
                    amature_racer4_is_leader=0
                    amature_racer4_fans=0

                if(amature_racer5_life<=0):
                    amature_racer5_speed=0
                    amature_racer5_position_x=-1
                    amature_racer5_is_leader=0
                    amature_racer5_fans=0

                if(amature_racer6_life<=0):
                    amature_racer6_speed=0
                    amature_racer6_position_x=-1
                    amature_racer6_is_leader=0
                    amature_racer6_fans=0

                if(amature_racer7_life<=0):
                    amature_racer7_speed=0
                    amature_racer7_position_x=-1
                    amature_racer7_is_leader=0
                    amature_racer7_fans=0

                if(amature_racer8_life<=0):
                    amature_racer8_speed=0
                    amature_racer8_position_x=-1
                    amature_racer8_is_leader=0
                    amature_racer8_fans=0

                if(amature_racer9_life<=0):
                    amature_racer9_speed=0
                    amature_racer9_position_x=-1
                    amature_racer9_is_leader=0
                    amature_racer9_fans=0

                if(amature_racer10_life<=0):
                    amature_racer10_speed=0
                    amature_racer10_position_x=-1
                    amature_racer10_is_leader=0
                    amature_racer10_fans=0

                                    
                if(amature_goal==amature_leader or amature_goal<amature_leader):
                    normal_amature_race=1
                    in_amature_arena=0

                    if(amature_racer1_is_leader==1):
                        print(f"comentator: now we see that racer {amature_racer1_name} has won the race!")

                    elif(amature_racer2_is_leader==1):
                        print(f"comentator: now we see that racer {amature_racer2_name} has won the race!")

                    elif(amature_racer3_is_leader==1):
                        print(f"comentator: now we see that racer {amature_racer3_name} has won the race!")

                    elif(amature_racer4_is_leader==1):
                        print(f"comentator: now we see that racer {amature_racer4_name} has won the race!")

                    elif(amature_racer5_is_leader==1):
                        print(f"comentator: now we see that racer {amature_racer5_name} has won the race!")

                    elif(amature_racer6_is_leader==1):
                        print(f"comentator: now we see that racer {amature_racer6_name} has won the race!")

                    elif(amature_racer7_is_leader==1):
                        print(f"comentator: now we see that racer {amature_racer7_name} has won the race!")

                    elif(amature_racer8_is_leader==1):
                        print(f"comentator: now we see that racer {amature_racer8_name} has won the race!")

                    elif(amature_racer9_is_leader==1):
                        print(f"comentator: now we see that racer {amature_racer9_name} has won the race!")

                    elif(amature_racer10_is_leader==1):
                        print(f"comentator: now we see that racer {amature_racer10_name} has won the race!")

                if(amature_racer1_life<=0 and amature_racer2_life<=0 and amature_racer3_life<=0 and amature_racer4_life<=0 and amature_racer5_life<=0 and amature_racer6_life<=0 and amature_racer7_life<=0 and amature_racer8_life<=0 and amature_racer9_life<=0 and amature_racer10_life<=0):
                    print("comentator: wow, well I knew fans can get rowdy, but dind't expect this")
                    print("Secret ending 1, mass murder")
                    in_amature_arena=0


        elif(what_stadium_do_I_go_to=="2" or what_stadium_do_I_go_to=="pro" or what_stadium_do_I_go_to=="pro league"):
            #code pro leagua here
            print(name,": Wow, this place is huge. This is definitely different from the amateur stadium.")
            in_profesional_arena=1
            have_I_watched_a_race_today=1

            favorite_profesional_racer=input(f"""{name}: Who should I support?
            1. Alex
            2. Mia
            3. Lucas
            4. Chloe
            5. Noah
            6. Elena
            7. Ethan
            8. Isabella
            9. Mateo
            10. Zoe
            I'll type the number: """)

            if(favorite_profesional_racer=="1"):
                pro_racer_1_fans+=1
            elif(favorite_profesional_racer=="2"):
                pro_racer_2_fans+=1
            elif(favorite_profesional_racer=="3"):
                pro_racer_3_fans+=1
            elif(favorite_profesional_racer=="4"):
                pro_racer_4_fans+=1
            elif(favorite_profesional_racer=="5"):
                pro_racer_5_fans+=1
            elif(favorite_profesional_racer=="6"):
                pro_racer_6_fans+=1
            elif(favorite_profesional_racer=="7"):
                pro_racer_7_fans+=1
            elif(favorite_profesional_racer=="8"):
                pro_racer_8_fans+=1
            elif(favorite_profesional_racer=="9"):
                pro_racer_9_fans+=1
            elif(favorite_profesional_racer=="10"):
                pro_racer_10_fans+=1

            print(f"{name}: I have ${player_money}. Maybe I should place a bet.")

            gambling_profesional_racer=input("Which racer do I want to bet on? Type 1-10: ")

            gambling_profesional_money=int(input(f"How much do I want to bet? I currently have ${player_money}: "))

            while(gambling_profesional_money<0 or gambling_profesional_money>player_money):
                print(name,": I can't bet that amount.")
                gambling_profesional_money=int(input(f"How much should I bet? I have ${player_money}: "))

            player_money-=gambling_profesional_money

            print(f"{name}: Alright. I have ${player_money} left, and ${gambling_profesional_money} is on racer {gambling_profesional_racer}.")

            while(spectetors_profesional!=0):
                profesional_fans_goes_to=random.randint(1,10)

                if(profesional_fans_goes_to==1):
                    pro_racer_1_fans+=1
                    spectetors_profesional-=1

                elif(profesional_fans_goes_to==2):
                    pro_racer_2_fans+=1
                    spectetors_profesional-=1

                elif(profesional_fans_goes_to==3):
                    pro_racer_3_fans+=1
                    spectetors_profesional-=1

                elif(profesional_fans_goes_to==4):
                    pro_racer_4_fans+=1
                    spectetors_profesional-=1

                elif(profesional_fans_goes_to==5):
                    pro_racer_5_fans+=1
                    spectetors_profesional-=1

                elif(profesional_fans_goes_to==6):
                    pro_racer_6_fans+=1
                    spectetors_profesional-=1

                elif(profesional_fans_goes_to==7):
                    pro_racer_7_fans+=1
                    spectetors_profesional-=1

                elif(profesional_fans_goes_to==8):
                    pro_racer_8_fans+=1
                    spectetors_profesional-=1

                elif(profesional_fans_goes_to==9):
                    pro_racer_9_fans+=1
                    spectetors_profesional-=1

                elif(profesional_fans_goes_to==10):
                    pro_racer_10_fans+=1
                    spectetors_profesional-=1

            while(in_profesional_arena==1):
                profesional_goal=5000

                if(pro_racer_1_life>0):
                    pro_racer_1_position_x+=pro_racer_1_speed+random.randint(-8,8)

                if(pro_racer_2_life>0):
                    pro_racer_2_position_x+=pro_racer_2_speed+random.randint(-8,8)

                if(pro_racer_3_life>0):
                    pro_racer_3_position_x+=pro_racer_3_speed+random.randint(-8,8)

                if(pro_racer_4_life>0):
                    pro_racer_4_position_x+=pro_racer_4_speed+random.randint(-8,8)

                if(pro_racer_5_life>0):
                    pro_racer_5_position_x+=pro_racer_5_speed+random.randint(-8,8)

                if(pro_racer_6_life>0):
                    pro_racer_6_position_x+=pro_racer_6_speed+random.randint(-8,8)

                if(pro_racer_7_life>0):
                    pro_racer_7_position_x+=pro_racer_7_speed+random.randint(-8,8)

                if(pro_racer_8_life>0):
                    pro_racer_8_position_x+=pro_racer_8_speed+random.randint(-8,8)

                if(pro_racer_9_life>0):
                    pro_racer_9_position_x+=pro_racer_9_speed+random.randint(-8,8)

                if(pro_racer_10_life>0):
                    pro_racer_10_position_x+=pro_racer_10_speed+random.randint(-8,8)

                profesional_leader=max(
                    pro_racer_1_position_x,
                    pro_racer_2_position_x,
                    pro_racer_3_position_x,
                    pro_racer_4_position_x,
                    pro_racer_5_position_x,
                    pro_racer_6_position_x,
                    pro_racer_7_position_x,
                    pro_racer_8_position_x,
                    pro_racer_9_position_x,
                    pro_racer_10_position_x
                )

                pro_racer_1_is_leader=0
                pro_racer_2_is_leader=0
                pro_racer_3_is_leader=0
                pro_racer_4_is_leader=0
                pro_racer_5_is_leader=0
                pro_racer_6_is_leader=0
                pro_racer_7_is_leader=0
                pro_racer_8_is_leader=0
                pro_racer_9_is_leader=0
                pro_racer_10_is_leader=0

                if(profesional_leader==pro_racer_1_position_x):
                    pro_racer_1_is_leader=1
                    print(f"comentator: {pro_racer_1_name} is leading and is {profesional_goal-profesional_leader} meters from the goal")

                elif(profesional_leader==pro_racer_2_position_x):
                    pro_racer_2_is_leader=1
                    print(f"comentator: {pro_racer_2_name} is leading and is {profesional_goal-profesional_leader} meters from the goal")

                elif(profesional_leader==pro_racer_3_position_x):
                    pro_racer_3_is_leader=1
                    print(f"comentator: {pro_racer_3_name} is leading and is {profesional_goal-profesional_leader} meters from the goal")

                elif(profesional_leader==pro_racer_4_position_x):
                    pro_racer_4_is_leader=1
                    print(f"comentator: {pro_racer_4_name} is leading and is {profesional_goal-profesional_leader} meters from the goal")

                elif(profesional_leader==pro_racer_5_position_x):
                    pro_racer_5_is_leader=1
                    print(f"comentator: {pro_racer_5_name} is leading and is {profesional_goal-profesional_leader} meters from the goal")

                elif(profesional_leader==pro_racer_6_position_x):
                    pro_racer_6_is_leader=1
                    print(f"comentator: {pro_racer_6_name} is leading and is {profesional_goal-profesional_leader} meters from the goal")

                elif(profesional_leader==pro_racer_7_position_x):
                    pro_racer_7_is_leader=1
                    print(f"comentator: {pro_racer_7_name} is leading and is {profesional_goal-profesional_leader} meters from the goal")

                elif(profesional_leader==pro_racer_8_position_x):
                    pro_racer_8_is_leader=1
                    print(f"comentator: {pro_racer_8_name} is leading and is {profesional_goal-profesional_leader} meters from the goal")

                elif(profesional_leader==pro_racer_9_position_x):
                    pro_racer_9_is_leader=1
                    print(f"comentator: {pro_racer_9_name} is leading and is {profesional_goal-profesional_leader} meters from the goal")

                elif(profesional_leader==pro_racer_10_position_x):
                    pro_racer_10_is_leader=1
                    print(f"comentator: {pro_racer_10_name} is leading and is {profesional_goal-profesional_leader} meters from the goal")

                    #PRO RACER 1 FANS
                if(profesional_leader-pro_racer_1_position_x>0 and pro_racer_1_life>0):

                    if(profesional_leader-pro_racer_1_position_x<10):
                        pro_racer_1_fans_excitment+=10

                        if(pro_racer_1_fans_excitment==100):
                            pro_racer_1_speed+=1

                    elif(10 <= profesional_leader-pro_racer_1_position_x <= 50):
                        pro_racer_1_fans_excitment-=1

                        if(pro_racer_1_fans_excitment<0):
                            pro_racer_1_fans_excitment=0

                    elif(50 < profesional_leader-pro_racer_1_position_x <= 100):

                        profesional_rowdy_warning=random.randint(1,20)

                        if(profesional_rowdy_warning==1):
                            print(f"comentator: The fans of {pro_racer_1_name} are starting to get a little rowdy.")

                        profesional_food_attack=random.randint(1,100)

                        if(profesional_food_attack==1):

                            if(pro_racer_1_is_leader==0):

                                if(pro_racer_2_is_leader==1):
                                    pro_racer_2_life-=1
                                    pro_racer_2_position_x-=25
                                    print(f"comentator: We see that {pro_racer_2_name} got hit by some food from the spectators! They must really hate them being in the lead. They lost some ground and look a bit hurt, but they're back to it again now.")

                                elif(pro_racer_3_is_leader==1):
                                    pro_racer_3_life-=1
                                    pro_racer_3_position_x-=25
                                    print(f"comentator: We see that {pro_racer_3_name} got hit by some food from the spectators! They lost some ground and look a bit hurt.")

                                elif(pro_racer_4_is_leader==1):
                                    pro_racer_4_life-=1
                                    pro_racer_4_position_x-=25

                                elif(pro_racer_5_is_leader==1):
                                    pro_racer_5_life-=1
                                    pro_racer_5_position_x-=25

                                elif(pro_racer_6_is_leader==1):
                                    pro_racer_6_life-=1
                                    pro_racer_6_position_x-=25

                                elif(pro_racer_7_is_leader==1):
                                    pro_racer_7_life-=1
                                    pro_racer_7_position_x-=25

                                elif(pro_racer_8_is_leader==1):
                                    pro_racer_8_life-=1
                                    pro_racer_8_position_x-=25

                                elif(pro_racer_9_is_leader==1):
                                    pro_racer_9_life-=1
                                    pro_racer_9_position_x-=25

                                elif(pro_racer_10_is_leader==1):
                                    pro_racer_10_life-=1
                                    pro_racer_10_position_x-=25


                    elif(profesional_leader-pro_racer_1_position_x>100):

                        pro_racer_1_fans_annoyens+=1

                        if(pro_racer_1_fans_annoyens>=100):

                            pro_racer_1_fans_attacking=pro_racer_1_fans

                            while(pro_racer_1_fans_attacking>0):

                                pro_racer_1_fan_attack=random.randint(1,100000)

                                if(pro_racer_1_fan_attack==1):
                                    print("PANG!")
                                    
                                    if(pro_racer_1_is_leader==0):

                                        if(pro_racer_2_is_leader==1):
                                            pro_racer_2_life-=10

                                        elif(pro_racer_3_is_leader==1):
                                            pro_racer_3_life-=10

                                        elif(pro_racer_4_is_leader==1):
                                            pro_racer_4_life-=10

                                        elif(pro_racer_5_is_leader==1):
                                            pro_racer_5_life-=10

                                        elif(pro_racer_6_is_leader==1):
                                            pro_racer_6_life-=10

                                        elif(pro_racer_7_is_leader==1):
                                            pro_racer_7_life-=10

                                        elif(pro_racer_8_is_leader==1):
                                            pro_racer_8_life-=10

                                        elif(pro_racer_9_is_leader==1):
                                            pro_racer_9_life-=10

                                        elif(pro_racer_10_is_leader==1):
                                            pro_racer_10_life-=10

                                elif(2 <= pro_racer_1_fan_attack <= 101):

                                    if(pro_racer_2_is_leader==1):
                                        pro_racer_2_life-=1
                                        pro_racer_2_position_x-=25

                                    elif(pro_racer_3_is_leader==1):
                                        pro_racer_3_life-=1
                                        pro_racer_3_position_x-=25

                                    elif(pro_racer_4_is_leader==1):
                                        pro_racer_4_life-=1
                                        pro_racer_4_position_x-=25

                                    elif(pro_racer_5_is_leader==1):
                                        pro_racer_5_life-=1
                                        pro_racer_5_position_x-=25

                                    elif(pro_racer_6_is_leader==1):
                                        pro_racer_6_life-=1
                                        pro_racer_6_position_x-=25

                                    elif(pro_racer_7_is_leader==1):
                                        pro_racer_7_life-=1
                                        pro_racer_7_position_x-=25

                                    elif(pro_racer_8_is_leader==1):
                                        pro_racer_8_life-=1
                                        pro_racer_8_position_x-=25

                                    elif(pro_racer_9_is_leader==1):
                                        pro_racer_9_life-=1
                                        pro_racer_9_position_x-=25

                                    elif(pro_racer_10_is_leader==1):
                                        pro_racer_10_life-=1
                                        pro_racer_10_position_x-=25

                                pro_racer_1_fans_attacking-=1
                                pro_racer_1_fans_annoyens=50




                #PRO RACER 2 FANS
                if(profesional_leader-pro_racer_2_position_x>0 and pro_racer_2_life>0):

                    if(profesional_leader-pro_racer_2_position_x<10):
                        pro_racer_2_fans_excitment+=10

                        if(pro_racer_2_fans_excitment==100):
                            pro_racer_2_speed+=1

                    elif(10 <= profesional_leader-pro_racer_2_position_x <= 50):
                        pro_racer_2_fans_excitment-=1

                        if(pro_racer_2_fans_excitment<0):
                            pro_racer_2_fans_excitment=0

                    elif(50 < profesional_leader-pro_racer_2_position_x <= 100):

                        profesional_rowdy_warning=random.randint(1,20)

                        if(profesional_rowdy_warning==1):
                            print(f"comentator: The fans of {pro_racer_2_name} are starting to get a little rowdy.")

                        profesional_food_attack=random.randint(1,100)

                        if(profesional_food_attack==1):

                            if(pro_racer_1_is_leader==1):
                                pro_racer_1_life-=1
                                pro_racer_1_position_x-=25
                                print(f"comentator: We see that {pro_racer_1_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_3_is_leader==1):
                                pro_racer_3_life-=1
                                pro_racer_3_position_x-=25
                                print(f"comentator: We see that {pro_racer_3_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_4_is_leader==1):
                                pro_racer_4_life-=1
                                pro_racer_4_position_x-=25
                                print(f"comentator: We see that {pro_racer_4_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_5_is_leader==1):
                                pro_racer_5_life-=1
                                pro_racer_5_position_x-=25
                                print(f"comentator: We see that {pro_racer_5_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_6_is_leader==1):
                                pro_racer_6_life-=1
                                pro_racer_6_position_x-=25
                                print(f"comentator: We see that {pro_racer_6_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_7_is_leader==1):
                                pro_racer_7_life-=1
                                pro_racer_7_position_x-=25
                                print(f"comentator: We see that {pro_racer_7_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_8_is_leader==1):
                                pro_racer_8_life-=1
                                pro_racer_8_position_x-=25
                                print(f"comentator: We see that {pro_racer_8_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_9_is_leader==1):
                                pro_racer_9_life-=1
                                pro_racer_9_position_x-=25
                                print(f"comentator: We see that {pro_racer_9_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_10_is_leader==1):
                                pro_racer_10_life-=1
                                pro_racer_10_position_x-=25
                                print(f"comentator: We see that {pro_racer_10_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                    elif(profesional_leader-pro_racer_2_position_x>100):

                        pro_racer_2_fans_annoyens+=1

                        if(pro_racer_2_fans_annoyens>=100):

                            pro_racer_2_fans_attacking=pro_racer_2_fans

                            while(pro_racer_2_fans_attacking>0):

                                pro_racer_2_fan_attack=random.randint(1,100000)

                                if(pro_racer_2_fan_attack==1):
                                    print("PANG!")

                                    if(pro_racer_1_is_leader==1):
                                        pro_racer_1_life-=10

                                    elif(pro_racer_3_is_leader==1):
                                        pro_racer_3_life-=10

                                    elif(pro_racer_4_is_leader==1):
                                        pro_racer_4_life-=10

                                    elif(pro_racer_5_is_leader==1):
                                        pro_racer_5_life-=10

                                    elif(pro_racer_6_is_leader==1):
                                        pro_racer_6_life-=10

                                    elif(pro_racer_7_is_leader==1):
                                        pro_racer_7_life-=10

                                    elif(pro_racer_8_is_leader==1):
                                        pro_racer_8_life-=10

                                    elif(pro_racer_9_is_leader==1):
                                        pro_racer_9_life-=10

                                    elif(pro_racer_10_is_leader==1):
                                        pro_racer_10_life-=10

                                elif(2 <= pro_racer_2_fan_attack <= 101):

                                    if(pro_racer_1_is_leader==1):
                                        pro_racer_1_life-=1
                                        pro_racer_1_position_x-=25

                                    elif(pro_racer_3_is_leader==1):
                                        pro_racer_3_life-=1
                                        pro_racer_3_position_x-=25

                                    elif(pro_racer_4_is_leader==1):
                                        pro_racer_4_life-=1
                                        pro_racer_4_position_x-=25

                                    elif(pro_racer_5_is_leader==1):
                                        pro_racer_5_life-=1
                                        pro_racer_5_position_x-=25

                                    elif(pro_racer_6_is_leader==1):
                                        pro_racer_6_life-=1
                                        pro_racer_6_position_x-=25

                                    elif(pro_racer_7_is_leader==1):
                                        pro_racer_7_life-=1
                                        pro_racer_7_position_x-=25

                                    elif(pro_racer_8_is_leader==1):
                                        pro_racer_8_life-=1
                                        pro_racer_8_position_x-=25

                                    elif(pro_racer_9_is_leader==1):
                                        pro_racer_9_life-=1
                                        pro_racer_9_position_x-=25

                                    elif(pro_racer_10_is_leader==1):
                                        pro_racer_10_life-=1
                                        pro_racer_10_position_x-=25

                                pro_racer_2_fans_attacking-=1

                            pro_racer_2_fans_annoyens=50

                #PRO RACER 3 FANS
                if(profesional_leader-pro_racer_3_position_x>0 and pro_racer_3_life>0):

                    if(profesional_leader-pro_racer_3_position_x<10):
                        pro_racer_3_fans_excitment+=10

                        if(pro_racer_3_fans_excitment==100):
                            pro_racer_3_speed+=1

                    elif(10 <= profesional_leader-pro_racer_3_position_x <= 50):
                        pro_racer_3_fans_excitment-=1

                        if(pro_racer_3_fans_excitment<0):
                            pro_racer_3_fans_excitment=0

                    elif(50 < profesional_leader-pro_racer_3_position_x <= 100):

                        profesional_rowdy_warning=random.randint(1,20)

                        if(profesional_rowdy_warning==1):
                            print(f"comentator: The fans of {pro_racer_3_name} are starting to get a little rowdy.")

                        profesional_food_attack=random.randint(1,100)

                        if(profesional_food_attack==1):

                            if(pro_racer_1_is_leader==1):
                                pro_racer_1_life-=1
                                pro_racer_1_position_x-=25
                                print(f"comentator: We see that {pro_racer_1_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_2_is_leader==1):
                                pro_racer_2_life-=1
                                pro_racer_2_position_x-=25
                                print(f"comentator: We see that {pro_racer_2_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_4_is_leader==1):
                                pro_racer_4_life-=1
                                pro_racer_4_position_x-=25
                                print(f"comentator: We see that {pro_racer_4_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_5_is_leader==1):
                                pro_racer_5_life-=1
                                pro_racer_5_position_x-=25
                                print(f"comentator: We see that {pro_racer_5_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_6_is_leader==1):
                                pro_racer_6_life-=1
                                pro_racer_6_position_x-=25
                                print(f"comentator: We see that {pro_racer_6_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_7_is_leader==1):
                                pro_racer_7_life-=1
                                pro_racer_7_position_x-=25
                                print(f"comentator: We see that {pro_racer_7_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_8_is_leader==1):
                                pro_racer_8_life-=1
                                pro_racer_8_position_x-=25
                                print(f"comentator: We see that {pro_racer_8_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_9_is_leader==1):
                                pro_racer_9_life-=1
                                pro_racer_9_position_x-=25
                                print(f"comentator: We see that {pro_racer_9_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_10_is_leader==1):
                                pro_racer_10_life-=1
                                pro_racer_10_position_x-=25
                                print(f"comentator: We see that {pro_racer_10_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                    elif(profesional_leader-pro_racer_3_position_x>100):

                        pro_racer_3_fans_annoyens+=1

                        if(pro_racer_3_fans_annoyens>=100):

                            pro_racer_3_fans_attacking=pro_racer_3_fans

                            while(pro_racer_3_fans_attacking>0):

                                pro_racer_3_fan_attack=random.randint(1,100000)

                                if(pro_racer_3_fan_attack==1):
                                    print("PANG!")

                                    if(pro_racer_1_is_leader==1):
                                        pro_racer_1_life-=10

                                    elif(pro_racer_2_is_leader==1):
                                        pro_racer_2_life-=10

                                    elif(pro_racer_4_is_leader==1):
                                        pro_racer_4_life-=10

                                    elif(pro_racer_5_is_leader==1):
                                        pro_racer_5_life-=10

                                    elif(pro_racer_6_is_leader==1):
                                        pro_racer_6_life-=10

                                    elif(pro_racer_7_is_leader==1):
                                        pro_racer_7_life-=10

                                    elif(pro_racer_8_is_leader==1):
                                        pro_racer_8_life-=10

                                    elif(pro_racer_9_is_leader==1):
                                        pro_racer_9_life-=10

                                    elif(pro_racer_10_is_leader==1):
                                        pro_racer_10_life-=10

                                elif(2 <= pro_racer_3_fan_attack <= 101):

                                    if(pro_racer_1_is_leader==1):
                                        pro_racer_1_life-=1
                                        pro_racer_1_position_x-=25

                                    elif(pro_racer_2_is_leader==1):
                                        pro_racer_2_life-=1
                                        pro_racer_2_position_x-=25

                                    elif(pro_racer_4_is_leader==1):
                                        pro_racer_4_life-=1
                                        pro_racer_4_position_x-=25

                                    elif(pro_racer_5_is_leader==1):
                                        pro_racer_5_life-=1
                                        pro_racer_5_position_x-=25

                                    elif(pro_racer_6_is_leader==1):
                                        pro_racer_6_life-=1
                                        pro_racer_6_position_x-=25

                                    elif(pro_racer_7_is_leader==1):
                                        pro_racer_7_life-=1
                                        pro_racer_7_position_x-=25

                                    elif(pro_racer_8_is_leader==1):
                                        pro_racer_8_life-=1
                                        pro_racer_8_position_x-=25

                                    elif(pro_racer_9_is_leader==1):
                                        pro_racer_9_life-=1
                                        pro_racer_9_position_x-=25

                                    elif(pro_racer_10_is_leader==1):
                                        pro_racer_10_life-=1
                                        pro_racer_10_position_x-=25

                                pro_racer_3_fans_attacking-=1

                            pro_racer_3_fans_annoyens=50

                #PRO RACER 4 FANS
                if(profesional_leader-pro_racer_4_position_x>0 and pro_racer_4_life>0):

                    if(profesional_leader-pro_racer_4_position_x<10):
                        pro_racer_4_fans_excitment+=10

                        if(pro_racer_4_fans_excitment==100):
                            pro_racer_4_speed+=1

                    elif(10 <= profesional_leader-pro_racer_4_position_x <= 50):
                        pro_racer_4_fans_excitment-=1

                        if(pro_racer_4_fans_excitment<0):
                            pro_racer_4_fans_excitment=0

                    elif(50 < profesional_leader-pro_racer_4_position_x <= 100):

                        profesional_rowdy_warning=random.randint(1,20)

                        if(profesional_rowdy_warning==1):
                            print(f"comentator: The fans of {pro_racer_4_name} are starting to get a little rowdy.")

                        profesional_food_attack=random.randint(1,100)

                        if(profesional_food_attack==1):

                            if(pro_racer_1_is_leader==1):
                                pro_racer_1_life-=1
                                pro_racer_1_position_x-=25
                                print(f"comentator: We see that {pro_racer_1_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_2_is_leader==1):
                                pro_racer_2_life-=1
                                pro_racer_2_position_x-=25
                                print(f"comentator: We see that {pro_racer_2_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_3_is_leader==1):
                                pro_racer_3_life-=1
                                pro_racer_3_position_x-=25
                                print(f"comentator: We see that {pro_racer_3_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_5_is_leader==1):
                                pro_racer_5_life-=1
                                pro_racer_5_position_x-=25
                                print(f"comentator: We see that {pro_racer_5_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_6_is_leader==1):
                                pro_racer_6_life-=1
                                pro_racer_6_position_x-=25
                                print(f"comentator: We see that {pro_racer_6_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_7_is_leader==1):
                                pro_racer_7_life-=1
                                pro_racer_7_position_x-=25
                                print(f"comentator: We see that {pro_racer_7_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_8_is_leader==1):
                                pro_racer_8_life-=1
                                pro_racer_8_position_x-=25
                                print(f"comentator: We see that {pro_racer_8_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_9_is_leader==1):
                                pro_racer_9_life-=1
                                pro_racer_9_position_x-=25
                                print(f"comentator: We see that {pro_racer_9_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_10_is_leader==1):
                                pro_racer_10_life-=1
                                pro_racer_10_position_x-=25
                                print(f"comentator: We see that {pro_racer_10_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                    elif(profesional_leader-pro_racer_4_position_x>100):

                        pro_racer_4_fans_annoyens+=1

                        if(pro_racer_4_fans_annoyens>=100):

                            pro_racer_4_fans_attacking=pro_racer_4_fans

                            while(pro_racer_4_fans_attacking>0):

                                pro_racer_4_fan_attack=random.randint(1,100000)

                                if(pro_racer_4_fan_attack==1):
                                    print("PANG!")

                                    if(pro_racer_1_is_leader==1):
                                        pro_racer_1_life-=10

                                    elif(pro_racer_2_is_leader==1):
                                        pro_racer_2_life-=10

                                    elif(pro_racer_3_is_leader==1):
                                        pro_racer_3_life-=10

                                    elif(pro_racer_5_is_leader==1):
                                        pro_racer_5_life-=10

                                    elif(pro_racer_6_is_leader==1):
                                        pro_racer_6_life-=10

                                    elif(pro_racer_7_is_leader==1):
                                        pro_racer_7_life-=10

                                    elif(pro_racer_8_is_leader==1):
                                        pro_racer_8_life-=10

                                    elif(pro_racer_9_is_leader==1):
                                        pro_racer_9_life-=10

                                    elif(pro_racer_10_is_leader==1):
                                        pro_racer_10_life-=10

                                elif(2 <= pro_racer_4_fan_attack <= 101):

                                    if(pro_racer_1_is_leader==1):
                                        pro_racer_1_life-=1
                                        pro_racer_1_position_x-=25

                                    elif(pro_racer_2_is_leader==1):
                                        pro_racer_2_life-=1
                                        pro_racer_2_position_x-=25

                                    elif(pro_racer_3_is_leader==1):
                                        pro_racer_3_life-=1
                                        pro_racer_3_position_x-=25

                                    elif(pro_racer_5_is_leader==1):
                                        pro_racer_5_life-=1
                                        pro_racer_5_position_x-=25

                                    elif(pro_racer_6_is_leader==1):
                                        pro_racer_6_life-=1
                                        pro_racer_6_position_x-=25

                                    elif(pro_racer_7_is_leader==1):
                                        pro_racer_7_life-=1
                                        pro_racer_7_position_x-=25

                                    elif(pro_racer_8_is_leader==1):
                                        pro_racer_8_life-=1
                                        pro_racer_8_position_x-=25

                                    elif(pro_racer_9_is_leader==1):
                                        pro_racer_9_life-=1
                                        pro_racer_9_position_x-=25

                                    elif(pro_racer_10_is_leader==1):
                                        pro_racer_10_life-=1
                                        pro_racer_10_position_x-=25

                                pro_racer_4_fans_attacking-=1

                            pro_racer_4_fans_annoyens=50

                #PRO RACER 5 FANS
                if(profesional_leader-pro_racer_5_position_x>0 and pro_racer_5_life>0):

                    if(profesional_leader-pro_racer_5_position_x<10):
                        pro_racer_5_fans_excitment+=10

                        if(pro_racer_5_fans_excitment==100):
                            pro_racer_5_speed+=1

                    elif(10 <= profesional_leader-pro_racer_5_position_x <= 50):
                        pro_racer_5_fans_excitment-=1

                        if(pro_racer_5_fans_excitment<0):
                            pro_racer_5_fans_excitment=0

                    elif(50 < profesional_leader-pro_racer_5_position_x <= 100):

                        profesional_rowdy_warning=random.randint(1,20)

                        if(profesional_rowdy_warning==1):
                            print(f"comentator: The fans of {pro_racer_5_name} are starting to get a little rowdy.")

                        profesional_food_attack=random.randint(1,100)

                        if(profesional_food_attack==1):

                            if(pro_racer_1_is_leader==1):
                                pro_racer_1_life-=1
                                pro_racer_1_position_x-=25
                                print(f"comentator: We see that {pro_racer_1_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_2_is_leader==1):
                                pro_racer_2_life-=1
                                pro_racer_2_position_x-=25
                                print(f"comentator: We see that {pro_racer_2_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_3_is_leader==1):
                                pro_racer_3_life-=1
                                pro_racer_3_position_x-=25
                                print(f"comentator: We see that {pro_racer_3_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_4_is_leader==1):
                                pro_racer_4_life-=1
                                pro_racer_4_position_x-=25
                                print(f"comentator: We see that {pro_racer_4_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_6_is_leader==1):
                                pro_racer_6_life-=1
                                pro_racer_6_position_x-=25
                                print(f"comentator: We see that {pro_racer_6_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_7_is_leader==1):
                                pro_racer_7_life-=1
                                pro_racer_7_position_x-=25
                                print(f"comentator: We see that {pro_racer_7_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_8_is_leader==1):
                                pro_racer_8_life-=1
                                pro_racer_8_position_x-=25
                                print(f"comentator: We see that {pro_racer_8_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_9_is_leader==1):
                                pro_racer_9_life-=1
                                pro_racer_9_position_x-=25
                                print(f"comentator: We see that {pro_racer_9_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_10_is_leader==1):
                                pro_racer_10_life-=1
                                pro_racer_10_position_x-=25
                                print(f"comentator: We see that {pro_racer_10_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                    elif(profesional_leader-pro_racer_5_position_x>100):

                        pro_racer_5_fans_annoyens+=1

                        if(pro_racer_5_fans_annoyens>=100):

                            pro_racer_5_fans_attacking=pro_racer_5_fans

                            while(pro_racer_5_fans_attacking>0):

                                pro_racer_5_fan_attack=random.randint(1,100000)

                                if(pro_racer_5_fan_attack==1):
                                    print("PANG!")

                                    if(pro_racer_1_is_leader==1):
                                        pro_racer_1_life-=10

                                    elif(pro_racer_2_is_leader==1):
                                        pro_racer_2_life-=10

                                    elif(pro_racer_3_is_leader==1):
                                        pro_racer_3_life-=10

                                    elif(pro_racer_4_is_leader==1):
                                        pro_racer_4_life-=10

                                    elif(pro_racer_6_is_leader==1):
                                        pro_racer_6_life-=10

                                    elif(pro_racer_7_is_leader==1):
                                        pro_racer_7_life-=10

                                    elif(pro_racer_8_is_leader==1):
                                        pro_racer_8_life-=10

                                    elif(pro_racer_9_is_leader==1):
                                        pro_racer_9_life-=10

                                    elif(pro_racer_10_is_leader==1):
                                        pro_racer_10_life-=10

                                elif(2 <= pro_racer_5_fan_attack <= 101):

                                    if(pro_racer_1_is_leader==1):
                                        pro_racer_1_life-=1
                                        pro_racer_1_position_x-=25

                                    elif(pro_racer_2_is_leader==1):
                                        pro_racer_2_life-=1
                                        pro_racer_2_position_x-=25

                                    elif(pro_racer_3_is_leader==1):
                                        pro_racer_3_life-=1
                                        pro_racer_3_position_x-=25

                                    elif(pro_racer_4_is_leader==1):
                                        pro_racer_4_life-=1
                                        pro_racer_4_position_x-=25

                                    elif(pro_racer_6_is_leader==1):
                                        pro_racer_6_life-=1
                                        pro_racer_6_position_x-=25

                                    elif(pro_racer_7_is_leader==1):
                                        pro_racer_7_life-=1
                                        pro_racer_7_position_x-=25

                                    elif(pro_racer_8_is_leader==1):
                                        pro_racer_8_life-=1
                                        pro_racer_8_position_x-=25

                                    elif(pro_racer_9_is_leader==1):
                                        pro_racer_9_life-=1
                                        pro_racer_9_position_x-=25

                                    elif(pro_racer_10_is_leader==1):
                                        pro_racer_10_life-=1
                                        pro_racer_10_position_x-=25

                                pro_racer_5_fans_attacking-=1

                            pro_racer_5_fans_annoyens=50

                #PRO RACER 6 FANS
                if(profesional_leader-pro_racer_6_position_x>0 and pro_racer_6_life>0):

                    if(profesional_leader-pro_racer_6_position_x<10):
                        pro_racer_6_fans_excitment+=10

                        if(pro_racer_6_fans_excitment==100):
                            pro_racer_6_speed+=1

                    elif(10 <= profesional_leader-pro_racer_6_position_x <= 50):
                        pro_racer_6_fans_excitment-=1

                        if(pro_racer_6_fans_excitment<0):
                            pro_racer_6_fans_excitment=0

                    elif(50 < profesional_leader-pro_racer_6_position_x <= 100):

                        profesional_rowdy_warning=random.randint(1,20)

                        if(profesional_rowdy_warning==1):
                            print(f"comentator: The fans of {pro_racer_6_name} are starting to get a little rowdy.")

                        profesional_food_attack=random.randint(1,100)

                        if(profesional_food_attack==1):

                            if(pro_racer_1_is_leader==1):
                                pro_racer_1_life-=1
                                pro_racer_1_position_x-=25
                                print(f"comentator: We see that {pro_racer_1_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_2_is_leader==1):
                                pro_racer_2_life-=1
                                pro_racer_2_position_x-=25
                                print(f"comentator: We see that {pro_racer_2_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_3_is_leader==1):
                                pro_racer_3_life-=1
                                pro_racer_3_position_x-=25
                                print(f"comentator: We see that {pro_racer_3_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_4_is_leader==1):
                                pro_racer_4_life-=1
                                pro_racer_4_position_x-=25
                                print(f"comentator: We see that {pro_racer_4_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_5_is_leader==1):
                                pro_racer_5_life-=1
                                pro_racer_5_position_x-=25
                                print(f"comentator: We see that {pro_racer_5_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_7_is_leader==1):
                                pro_racer_7_life-=1
                                pro_racer_7_position_x-=25
                                print(f"comentator: We see that {pro_racer_7_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_8_is_leader==1):
                                pro_racer_8_life-=1
                                pro_racer_8_position_x-=25
                                print(f"comentator: We see that {pro_racer_8_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_9_is_leader==1):
                                pro_racer_9_life-=1
                                pro_racer_9_position_x-=25
                                print(f"comentator: We see that {pro_racer_9_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_10_is_leader==1):
                                pro_racer_10_life-=1
                                pro_racer_10_position_x-=25
                                print(f"comentator: We see that {pro_racer_10_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                    elif(profesional_leader-pro_racer_6_position_x>100):

                        pro_racer_6_fans_annoyens+=1

                        if(pro_racer_6_fans_annoyens>=100):

                            pro_racer_6_fans_attacking=pro_racer_6_fans

                            while(pro_racer_6_fans_attacking>0):

                                pro_racer_6_fan_attack=random.randint(1,100000)

                                if(pro_racer_6_fan_attack==1):
                                    print("PANG!")

                                    if(pro_racer_1_is_leader==1):
                                        pro_racer_1_life-=10

                                    elif(pro_racer_2_is_leader==1):
                                        pro_racer_2_life-=10

                                    elif(pro_racer_3_is_leader==1):
                                        pro_racer_3_life-=10

                                    elif(pro_racer_4_is_leader==1):
                                        pro_racer_4_life-=10

                                    elif(pro_racer_5_is_leader==1):
                                        pro_racer_5_life-=10

                                    elif(pro_racer_7_is_leader==1):
                                        pro_racer_7_life-=10

                                    elif(pro_racer_8_is_leader==1):
                                        pro_racer_8_life-=10

                                    elif(pro_racer_9_is_leader==1):
                                        pro_racer_9_life-=10

                                    elif(pro_racer_10_is_leader==1):
                                        pro_racer_10_life-=10

                                elif(2 <= pro_racer_6_fan_attack <= 101):

                                    if(pro_racer_1_is_leader==1):
                                        pro_racer_1_life-=1
                                        pro_racer_1_position_x-=25

                                    elif(pro_racer_2_is_leader==1):
                                        pro_racer_2_life-=1
                                        pro_racer_2_position_x-=25

                                    elif(pro_racer_3_is_leader==1):
                                        pro_racer_3_life-=1
                                        pro_racer_3_position_x-=25

                                    elif(pro_racer_4_is_leader==1):
                                        pro_racer_4_life-=1
                                        pro_racer_4_position_x-=25

                                    elif(pro_racer_5_is_leader==1):
                                        pro_racer_5_life-=1
                                        pro_racer_5_position_x-=25

                                    elif(pro_racer_7_is_leader==1):
                                        pro_racer_7_life-=1
                                        pro_racer_7_position_x-=25

                                    elif(pro_racer_8_is_leader==1):
                                        pro_racer_8_life-=1
                                        pro_racer_8_position_x-=25

                                    elif(pro_racer_9_is_leader==1):
                                        pro_racer_9_life-=1
                                        pro_racer_9_position_x-=25

                                    elif(pro_racer_10_is_leader==1):
                                        pro_racer_10_life-=1
                                        pro_racer_10_position_x-=25

                                pro_racer_6_fans_attacking-=1

                            pro_racer_6_fans_annoyens=50

                #PRO RACER 7 FANS
                if(profesional_leader-pro_racer_7_position_x>0 and pro_racer_7_life>0):

                    if(profesional_leader-pro_racer_7_position_x<10):
                        pro_racer_7_fans_excitment+=10

                        if(pro_racer_7_fans_excitment==100):
                            pro_racer_7_speed+=1

                    elif(10 <= profesional_leader-pro_racer_7_position_x <= 50):
                        pro_racer_7_fans_excitment-=1

                        if(pro_racer_7_fans_excitment<0):
                            pro_racer_7_fans_excitment=0

                    elif(50 < profesional_leader-pro_racer_7_position_x <= 100):

                        profesional_rowdy_warning=random.randint(1,20)

                        if(profesional_rowdy_warning==1):
                            print(f"comentator: The fans of {pro_racer_7_name} are starting to get a little rowdy.")

                        profesional_food_attack=random.randint(1,100)

                        if(profesional_food_attack==1):

                            if(pro_racer_1_is_leader==1):
                                pro_racer_1_life-=1
                                pro_racer_1_position_x-=25
                                print(f"comentator: We see that {pro_racer_1_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_2_is_leader==1):
                                pro_racer_2_life-=1
                                pro_racer_2_position_x-=25
                                print(f"comentator: We see that {pro_racer_2_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_3_is_leader==1):
                                pro_racer_3_life-=1
                                pro_racer_3_position_x-=25
                                print(f"comentator: We see that {pro_racer_3_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_4_is_leader==1):
                                pro_racer_4_life-=1
                                pro_racer_4_position_x-=25
                                print(f"comentator: We see that {pro_racer_4_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_5_is_leader==1):
                                pro_racer_5_life-=1
                                pro_racer_5_position_x-=25
                                print(f"comentator: We see that {pro_racer_5_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_6_is_leader==1):
                                pro_racer_6_life-=1
                                pro_racer_6_position_x-=25
                                print(f"comentator: We see that {pro_racer_6_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_8_is_leader==1):
                                pro_racer_8_life-=1
                                pro_racer_8_position_x-=25
                                print(f"comentator: We see that {pro_racer_8_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_9_is_leader==1):
                                pro_racer_9_life-=1
                                pro_racer_9_position_x-=25
                                print(f"comentator: We see that {pro_racer_9_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_10_is_leader==1):
                                pro_racer_10_life-=1
                                pro_racer_10_position_x-=25
                                print(f"comentator: We see that {pro_racer_10_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                    elif(profesional_leader-pro_racer_7_position_x>100):

                        pro_racer_7_fans_annoyens+=1

                        if(pro_racer_7_fans_annoyens>=100):

                            pro_racer_7_fans_attacking=pro_racer_7_fans

                            while(pro_racer_7_fans_attacking>0):

                                pro_racer_7_fan_attack=random.randint(1,100000)

                                if(pro_racer_7_fan_attack==1):
                                    print("PANG!")

                                    if(pro_racer_1_is_leader==1):
                                        pro_racer_1_life-=10

                                    elif(pro_racer_2_is_leader==1):
                                        pro_racer_2_life-=10

                                    elif(pro_racer_3_is_leader==1):
                                        pro_racer_3_life-=10

                                    elif(pro_racer_4_is_leader==1):
                                        pro_racer_4_life-=10

                                    elif(pro_racer_5_is_leader==1):
                                        pro_racer_5_life-=10

                                    elif(pro_racer_6_is_leader==1):
                                        pro_racer_6_life-=10

                                    elif(pro_racer_8_is_leader==1):
                                        pro_racer_8_life-=10

                                    elif(pro_racer_9_is_leader==1):
                                        pro_racer_9_life-=10

                                    elif(pro_racer_10_is_leader==1):
                                        pro_racer_10_life-=10

                                elif(2 <= pro_racer_7_fan_attack <= 101):

                                    if(pro_racer_1_is_leader==1):
                                        pro_racer_1_life-=1
                                        pro_racer_1_position_x-=25

                                    elif(pro_racer_2_is_leader==1):
                                        pro_racer_2_life-=1
                                        pro_racer_2_position_x-=25

                                    elif(pro_racer_3_is_leader==1):
                                        pro_racer_3_life-=1
                                        pro_racer_3_position_x-=25

                                    elif(pro_racer_4_is_leader==1):
                                        pro_racer_4_life-=1
                                        pro_racer_4_position_x-=25

                                    elif(pro_racer_5_is_leader==1):
                                        pro_racer_5_life-=1
                                        pro_racer_5_position_x-=25

                                    elif(pro_racer_6_is_leader==1):
                                        pro_racer_6_life-=1
                                        pro_racer_6_position_x-=25

                                    elif(pro_racer_8_is_leader==1):
                                        pro_racer_8_life-=1
                                        pro_racer_8_position_x-=25

                                    elif(pro_racer_9_is_leader==1):
                                        pro_racer_9_life-=1
                                        pro_racer_9_position_x-=25

                                    elif(pro_racer_10_is_leader==1):
                                        pro_racer_10_life-=1
                                        pro_racer_10_position_x-=25

                                pro_racer_7_fans_attacking-=1

                            pro_racer_7_fans_annoyens=50

                #PRO RACER 8 FANS
                if(profesional_leader-pro_racer_8_position_x>0 and pro_racer_8_life>0):

                    if(profesional_leader-pro_racer_8_position_x<10):
                        pro_racer_8_fans_excitment+=10

                        if(pro_racer_8_fans_excitment==100):
                            pro_racer_8_speed+=1

                    elif(10 <= profesional_leader-pro_racer_8_position_x <= 50):
                        pro_racer_8_fans_excitment-=1

                        if(pro_racer_8_fans_excitment<0):
                            pro_racer_8_fans_excitment=0

                    elif(50 < profesional_leader-pro_racer_8_position_x <= 100):

                        profesional_rowdy_warning=random.randint(1,20)

                        if(profesional_rowdy_warning==1):
                            print(f"comentator: The fans of {pro_racer_8_name} are starting to get a little rowdy.")

                        profesional_food_attack=random.randint(1,100)

                        if(profesional_food_attack==1):

                            if(pro_racer_1_is_leader==1):
                                pro_racer_1_life-=1
                                pro_racer_1_position_x-=25
                                print(f"comentator: We see that {pro_racer_1_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_2_is_leader==1):
                                pro_racer_2_life-=1
                                pro_racer_2_position_x-=25
                                print(f"comentator: We see that {pro_racer_2_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_3_is_leader==1):
                                pro_racer_3_life-=1
                                pro_racer_3_position_x-=25
                                print(f"comentator: We see that {pro_racer_3_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_4_is_leader==1):
                                pro_racer_4_life-=1
                                pro_racer_4_position_x-=25
                                print(f"comentator: We see that {pro_racer_4_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_5_is_leader==1):
                                pro_racer_5_life-=1
                                pro_racer_5_position_x-=25
                                print(f"comentator: We see that {pro_racer_5_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_6_is_leader==1):
                                pro_racer_6_life-=1
                                pro_racer_6_position_x-=25
                                print(f"comentator: We see that {pro_racer_6_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_7_is_leader==1):
                                pro_racer_7_life-=1
                                pro_racer_7_position_x-=25
                                print(f"comentator: We see that {pro_racer_7_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_9_is_leader==1):
                                pro_racer_9_life-=1
                                pro_racer_9_position_x-=25
                                print(f"comentator: We see that {pro_racer_9_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_10_is_leader==1):
                                pro_racer_10_life-=1
                                pro_racer_10_position_x-=25
                                print(f"comentator: We see that {pro_racer_10_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                    elif(profesional_leader-pro_racer_8_position_x>100):

                        pro_racer_8_fans_annoyens+=1

                        if(pro_racer_8_fans_annoyens>=100):

                            pro_racer_8_fans_attacking=pro_racer_8_fans

                            while(pro_racer_8_fans_attacking>0):

                                pro_racer_8_fan_attack=random.randint(1,100000)

                                if(pro_racer_8_fan_attack==1):
                                    print("PANG!")

                                    if(pro_racer_1_is_leader==1):
                                        pro_racer_1_life-=10

                                    elif(pro_racer_2_is_leader==1):
                                        pro_racer_2_life-=10

                                    elif(pro_racer_3_is_leader==1):
                                        pro_racer_3_life-=10

                                    elif(pro_racer_4_is_leader==1):
                                        pro_racer_4_life-=10

                                    elif(pro_racer_5_is_leader==1):
                                        pro_racer_5_life-=10

                                    elif(pro_racer_6_is_leader==1):
                                        pro_racer_6_life-=10

                                    elif(pro_racer_7_is_leader==1):
                                        pro_racer_7_life-=10

                                    elif(pro_racer_9_is_leader==1):
                                        pro_racer_9_life-=10

                                    elif(pro_racer_10_is_leader==1):
                                        pro_racer_10_life-=10

                                elif(2 <= pro_racer_8_fan_attack <= 101):

                                    if(pro_racer_1_is_leader==1):
                                        pro_racer_1_life-=1
                                        pro_racer_1_position_x-=25

                                    elif(pro_racer_2_is_leader==1):
                                        pro_racer_2_life-=1
                                        pro_racer_2_position_x-=25

                                    elif(pro_racer_3_is_leader==1):
                                        pro_racer_3_life-=1
                                        pro_racer_3_position_x-=25

                                    elif(pro_racer_4_is_leader==1):
                                        pro_racer_4_life-=1
                                        pro_racer_4_position_x-=25

                                    elif(pro_racer_5_is_leader==1):
                                        pro_racer_5_life-=1
                                        pro_racer_5_position_x-=25

                                    elif(pro_racer_6_is_leader==1):
                                        pro_racer_6_life-=1
                                        pro_racer_6_position_x-=25

                                    elif(pro_racer_7_is_leader==1):
                                        pro_racer_7_life-=1
                                        pro_racer_7_position_x-=25

                                    elif(pro_racer_9_is_leader==1):
                                        pro_racer_9_life-=1
                                        pro_racer_9_position_x-=25

                                    elif(pro_racer_10_is_leader==1):
                                        pro_racer_10_life-=1
                                        pro_racer_10_position_x-=25

                                pro_racer_8_fans_attacking-=1

                            pro_racer_8_fans_annoyens=50

                #PRO RACER 9 FANS
                if(profesional_leader-pro_racer_9_position_x>0 and pro_racer_9_life>0):

                    if(profesional_leader-pro_racer_9_position_x<10):
                        pro_racer_9_fans_excitment+=10

                        if(pro_racer_9_fans_excitment==100):
                            pro_racer_9_speed+=1

                    elif(10 <= profesional_leader-pro_racer_9_position_x <= 50):
                        pro_racer_9_fans_excitment-=1

                        if(pro_racer_9_fans_excitment<0):
                            pro_racer_9_fans_excitment=0

                    elif(50 < profesional_leader-pro_racer_9_position_x <= 100):

                        profesional_rowdy_warning=random.randint(1,20)

                        if(profesional_rowdy_warning==1):
                            print(f"comentator: The fans of {pro_racer_9_name} are starting to get a little rowdy.")

                        profesional_food_attack=random.randint(1,100)

                        if(profesional_food_attack==1):

                            if(pro_racer_1_is_leader==1):
                                pro_racer_1_life-=1
                                pro_racer_1_position_x-=25
                                print(f"comentator: We see that {pro_racer_1_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_2_is_leader==1):
                                pro_racer_2_life-=1
                                pro_racer_2_position_x-=25
                                print(f"comentator: We see that {pro_racer_2_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_3_is_leader==1):
                                pro_racer_3_life-=1
                                pro_racer_3_position_x-=25
                                print(f"comentator: We see that {pro_racer_3_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_4_is_leader==1):
                                pro_racer_4_life-=1
                                pro_racer_4_position_x-=25
                                print(f"comentator: We see that {pro_racer_4_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_5_is_leader==1):
                                pro_racer_5_life-=1
                                pro_racer_5_position_x-=25
                                print(f"comentator: We see that {pro_racer_5_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_6_is_leader==1):
                                pro_racer_6_life-=1
                                pro_racer_6_position_x-=25
                                print(f"comentator: We see that {pro_racer_6_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_7_is_leader==1):
                                pro_racer_7_life-=1
                                pro_racer_7_position_x-=25
                                print(f"comentator: We see that {pro_racer_7_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_8_is_leader==1):
                                pro_racer_8_life-=1
                                pro_racer_8_position_x-=25
                                print(f"comentator: We see that {pro_racer_8_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_10_is_leader==1):
                                pro_racer_10_life-=1
                                pro_racer_10_position_x-=25
                                print(f"comentator: We see that {pro_racer_10_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                    elif(profesional_leader-pro_racer_9_position_x>100):

                        pro_racer_9_fans_annoyens+=1

                        if(pro_racer_9_fans_annoyens>=100):

                            pro_racer_9_fans_attacking=pro_racer_9_fans

                            while(pro_racer_9_fans_attacking>0):

                                pro_racer_9_fan_attack=random.randint(1,100000)

                                if(pro_racer_9_fan_attack==1):
                                    print("PANG!")

                                    if(pro_racer_1_is_leader==1):
                                        pro_racer_1_life-=10

                                    elif(pro_racer_2_is_leader==1):
                                        pro_racer_2_life-=10

                                    elif(pro_racer_3_is_leader==1):
                                        pro_racer_3_life-=10

                                    elif(pro_racer_4_is_leader==1):
                                        pro_racer_4_life-=10

                                    elif(pro_racer_5_is_leader==1):
                                        pro_racer_5_life-=10

                                    elif(pro_racer_6_is_leader==1):
                                        pro_racer_6_life-=10

                                    elif(pro_racer_7_is_leader==1):
                                        pro_racer_7_life-=10

                                    elif(pro_racer_8_is_leader==1):
                                        pro_racer_8_life-=10

                                    elif(pro_racer_10_is_leader==1):
                                        pro_racer_10_life-=10

                                elif(2 <= pro_racer_9_fan_attack <= 101):

                                    if(pro_racer_1_is_leader==1):
                                        pro_racer_1_life-=1
                                        pro_racer_1_position_x-=25

                                    elif(pro_racer_2_is_leader==1):
                                        pro_racer_2_life-=1
                                        pro_racer_2_position_x-=25

                                    elif(pro_racer_3_is_leader==1):
                                        pro_racer_3_life-=1
                                        pro_racer_3_position_x-=25

                                    elif(pro_racer_4_is_leader==1):
                                        pro_racer_4_life-=1
                                        pro_racer_4_position_x-=25

                                    elif(pro_racer_5_is_leader==1):
                                        pro_racer_5_life-=1
                                        pro_racer_5_position_x-=25

                                    elif(pro_racer_6_is_leader==1):
                                        pro_racer_6_life-=1
                                        pro_racer_6_position_x-=25

                                    elif(pro_racer_7_is_leader==1):
                                        pro_racer_7_life-=1
                                        pro_racer_7_position_x-=25

                                    elif(pro_racer_8_is_leader==1):
                                        pro_racer_8_life-=1
                                        pro_racer_8_position_x-=25

                                    elif(pro_racer_10_is_leader==1):
                                        pro_racer_10_life-=1
                                        pro_racer_10_position_x-=25

                                pro_racer_9_fans_attacking-=1

                            pro_racer_9_fans_annoyens=50

                #PRO RACER 10 FANS
                if(profesional_leader-pro_racer_10_position_x>0 and pro_racer_10_life>0):

                    if(profesional_leader-pro_racer_10_position_x<10):
                        pro_racer_10_fans_excitment+=10

                        if(pro_racer_10_fans_excitment==100):
                            pro_racer_10_speed+=1

                    elif(10 <= profesional_leader-pro_racer_10_position_x <= 50):
                        pro_racer_10_fans_excitment-=1

                        if(pro_racer_10_fans_excitment<0):
                            pro_racer_10_fans_excitment=0

                    elif(50 < profesional_leader-pro_racer_10_position_x <= 100):

                        profesional_rowdy_warning=random.randint(1,20)

                        if(profesional_rowdy_warning==1):
                            print(f"comentator: The fans of {pro_racer_10_name} are starting to get a little rowdy.")

                        profesional_food_attack=random.randint(1,100)

                        if(profesional_food_attack==1):

                            if(pro_racer_1_is_leader==1):
                                pro_racer_1_life-=1
                                pro_racer_1_position_x-=25
                                print(f"comentator: We see that {pro_racer_1_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_2_is_leader==1):
                                pro_racer_2_life-=1
                                pro_racer_2_position_x-=25
                                print(f"comentator: We see that {pro_racer_2_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_3_is_leader==1):
                                pro_racer_3_life-=1
                                pro_racer_3_position_x-=25
                                print(f"comentator: We see that {pro_racer_3_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_4_is_leader==1):
                                pro_racer_4_life-=1
                                pro_racer_4_position_x-=25
                                print(f"comentator: We see that {pro_racer_4_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_5_is_leader==1):
                                pro_racer_5_life-=1
                                pro_racer_5_position_x-=25
                                print(f"comentator: We see that {pro_racer_5_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_6_is_leader==1):
                                pro_racer_6_life-=1
                                pro_racer_6_position_x-=25
                                print(f"comentator: We see that {pro_racer_6_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_7_is_leader==1):
                                pro_racer_7_life-=1
                                pro_racer_7_position_x-=25
                                print(f"comentator: We see that {pro_racer_7_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_8_is_leader==1):
                                pro_racer_8_life-=1
                                pro_racer_8_position_x-=25
                                print(f"comentator: We see that {pro_racer_8_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                            elif(pro_racer_9_is_leader==1):
                                pro_racer_9_life-=1
                                pro_racer_9_position_x-=25
                                print(f"comentator: We see that {pro_racer_9_name} got hit by some food from the spectators! They lost some ground and look a bit hurt, but they are back to it again now.")

                    elif(profesional_leader-pro_racer_10_position_x>100):

                        pro_racer_10_fans_annoyens+=1

                        if(pro_racer_10_fans_annoyens>=100):

                            pro_racer_10_fans_attacking=pro_racer_10_fans

                            while(pro_racer_10_fans_attacking>0):

                                pro_racer_10_fan_attack=random.randint(1,100000)

                                if(pro_racer_10_fan_attack==1):
                                    print("PANG!")

                                    if(pro_racer_1_is_leader==1):
                                        pro_racer_1_life-=10

                                    elif(pro_racer_2_is_leader==1):
                                        pro_racer_2_life-=10

                                    elif(pro_racer_3_is_leader==1):
                                        pro_racer_3_life-=10

                                    elif(pro_racer_4_is_leader==1):
                                        pro_racer_4_life-=10

                                    elif(pro_racer_5_is_leader==1):
                                        pro_racer_5_life-=10

                                    elif(pro_racer_6_is_leader==1):
                                        pro_racer_6_life-=10

                                    elif(pro_racer_7_is_leader==1):
                                        pro_racer_7_life-=10

                                    elif(pro_racer_8_is_leader==1):
                                        pro_racer_8_life-=10

                                    elif(pro_racer_9_is_leader==1):
                                        pro_racer_9_life-=10

                                elif(2 <= pro_racer_10_fan_attack <= 101):

                                    if(pro_racer_1_is_leader==1):
                                        pro_racer_1_life-=1
                                        pro_racer_1_position_x-=25

                                    elif(pro_racer_2_is_leader==1):
                                        pro_racer_2_life-=1
                                        pro_racer_2_position_x-=25

                                    elif(pro_racer_3_is_leader==1):
                                        pro_racer_3_life-=1
                                        pro_racer_3_position_x-=25

                                    elif(pro_racer_4_is_leader==1):
                                        pro_racer_4_life-=1
                                        pro_racer_4_position_x-=25

                                    elif(pro_racer_5_is_leader==1):
                                        pro_racer_5_life-=1
                                        pro_racer_5_position_x-=25

                                    elif(pro_racer_6_is_leader==1):
                                        pro_racer_6_life-=1
                                        pro_racer_6_position_x-=25

                                    elif(pro_racer_7_is_leader==1):
                                        pro_racer_7_life-=1
                                        pro_racer_7_position_x-=25

                                    elif(pro_racer_8_is_leader==1):
                                        pro_racer_8_life-=1
                                        pro_racer_8_position_x-=25

                                    elif(pro_racer_9_is_leader==1):
                                        pro_racer_9_life-=1
                                        pro_racer_9_position_x-=25

                                pro_racer_10_fans_attacking-=1

                            pro_racer_10_fans_annoyens=50













                favorite_profesional_health=10

                if(favorite_profesional_racer=="1"):
                    favorite_profesional_health=pro_racer_1_life
                elif(favorite_profesional_racer=="2"):
                    favorite_profesional_health=pro_racer_2_life
                elif(favorite_profesional_racer=="3"):
                    favorite_profesional_health=pro_racer_3_life
                elif(favorite_profesional_racer=="4"):
                    favorite_profesional_health=pro_racer_4_life
                elif(favorite_profesional_racer=="5"):
                    favorite_profesional_health=pro_racer_5_life
                elif(favorite_profesional_racer=="6"):
                    favorite_profesional_health=pro_racer_6_life
                elif(favorite_profesional_racer=="7"):
                    favorite_profesional_health=pro_racer_7_life
                elif(favorite_profesional_racer=="8"):
                    favorite_profesional_health=pro_racer_8_life
                elif(favorite_profesional_racer=="9"):
                    favorite_profesional_health=pro_racer_9_life
                elif(favorite_profesional_racer=="10"):
                    favorite_profesional_health=pro_racer_10_life

                profesional_potion_offer=0

                if(player_money>=10 and favorite_profesional_health>0):

                    if(5 <= favorite_profesional_health <= 9):
                        profesional_potion_offer=random.randint(1,20)

                    elif(favorite_profesional_health<5):
                        profesional_potion_offer=random.randint(1,2)

                    if(profesional_potion_offer==1):
                        buy_profesional_potion=input(f"A seller nearby offers you a health potion for your racer for $10. You have ${player_money}. Buy it? ").lower()

                        if(buy_profesional_potion=="yes"):
                            player_money-=10

                            if(favorite_profesional_racer=="1"):
                                pro_racer_1_life+=3
                                if(pro_racer_1_life>10):
                                    pro_racer_1_life=10

                            elif(favorite_profesional_racer=="2"):
                                pro_racer_2_life+=3
                                if(pro_racer_2_life>10):
                                    pro_racer_2_life=10

                            elif(favorite_profesional_racer=="3"):
                                pro_racer_3_life+=3
                                if(pro_racer_3_life>10):
                                    pro_racer_3_life=10

                            elif(favorite_profesional_racer=="4"):
                                pro_racer_4_life+=3
                                if(pro_racer_4_life>10):
                                    pro_racer_4_life=10

                            elif(favorite_profesional_racer=="5"):
                                pro_racer_5_life+=3
                                if(pro_racer_5_life>10):
                                    pro_racer_5_life=10

                            elif(favorite_profesional_racer=="6"):
                                pro_racer_6_life+=3
                                if(pro_racer_6_life>10):
                                    pro_racer_6_life=10

                            elif(favorite_profesional_racer=="7"):
                                pro_racer_7_life+=3
                                if(pro_racer_7_life>10):
                                    pro_racer_7_life=10

                            elif(favorite_profesional_racer=="8"):
                                pro_racer_8_life+=3
                                if(pro_racer_8_life>10):
                                    pro_racer_8_life=10

                            elif(favorite_profesional_racer=="9"):
                                pro_racer_9_life+=3
                                if(pro_racer_9_life>10):
                                    pro_racer_9_life=10

                            elif(favorite_profesional_racer=="10"):
                                pro_racer_10_life+=3
                                if(pro_racer_10_life>10):
                                    pro_racer_10_life=10

                            print(f"{name}: Hopefully that helps!")

                if(pro_racer_1_life<=0):
                    pro_racer_1_speed=0
                    pro_racer_1_position_x=-1
                    pro_racer_1_is_leader=0
                    pro_racer_1_fans=0

                if(pro_racer_2_life<=0):
                    pro_racer_2_speed=0
                    pro_racer_2_position_x=-1
                    pro_racer_2_is_leader=0
                    pro_racer_2_fans=0

                if(pro_racer_3_life<=0):
                    pro_racer_3_speed=0
                    pro_racer_3_position_x=-1
                    pro_racer_3_is_leader=0
                    pro_racer_3_fans=0

                if(pro_racer_4_life<=0):
                    pro_racer_4_speed=0
                    pro_racer_4_position_x=-1
                    pro_racer_4_is_leader=0
                    pro_racer_4_fans=0

                if(pro_racer_5_life<=0):
                    pro_racer_5_speed=0
                    pro_racer_5_position_x=-1
                    pro_racer_5_is_leader=0
                    pro_racer_5_fans=0

                if(pro_racer_6_life<=0):
                    pro_racer_6_speed=0
                    pro_racer_6_position_x=-1
                    pro_racer_6_is_leader=0
                    pro_racer_6_fans=0

                if(pro_racer_7_life<=0):
                    pro_racer_7_speed=0
                    pro_racer_7_position_x=-1
                    pro_racer_7_is_leader=0
                    pro_racer_7_fans=0

                if(pro_racer_8_life<=0):
                    pro_racer_8_speed=0
                    pro_racer_8_position_x=-1
                    pro_racer_8_is_leader=0
                    pro_racer_8_fans=0

                if(pro_racer_9_life<=0):
                    pro_racer_9_speed=0
                    pro_racer_9_position_x=-1
                    pro_racer_9_is_leader=0
                    pro_racer_9_fans=0

                if(pro_racer_10_life<=0):
                    pro_racer_10_speed=0
                    pro_racer_10_position_x=-1
                    pro_racer_10_is_leader=0
                    pro_racer_10_fans=0


                 #count how many racers are dead
                profesional_deaths=0

                if(pro_racer_1_life<=0):
                    profesional_deaths+=1
                if(pro_racer_2_life<=0):
                    profesional_deaths+=1
                if(pro_racer_3_life<=0):
                    profesional_deaths+=1
                if(pro_racer_4_life<=0):
                    profesional_deaths+=1
                if(pro_racer_5_life<=0):
                    profesional_deaths+=1
                if(pro_racer_6_life<=0):
                    profesional_deaths+=1
                if(pro_racer_7_life<=0):
                    profesional_deaths+=1
                if(pro_racer_8_life<=0):
                    profesional_deaths+=1
                if(pro_racer_9_life<=0):
                    profesional_deaths+=1
                if(pro_racer_10_life<=0):
                    profesional_deaths+=1

                profesional_leader=max(
                    pro_racer_1_position_x,
                    pro_racer_2_position_x,
                    pro_racer_3_position_x,
                    pro_racer_4_position_x,
                    pro_racer_5_position_x,
                    pro_racer_6_position_x,
                    pro_racer_7_position_x,
                    pro_racer_8_position_x,
                    pro_racer_9_position_x,
                    pro_racer_10_position_x
                )

                pro_racer_1_is_leader=0
                pro_racer_2_is_leader=0
                pro_racer_3_is_leader=0
                pro_racer_4_is_leader=0
                pro_racer_5_is_leader=0
                pro_racer_6_is_leader=0
                pro_racer_7_is_leader=0
                pro_racer_8_is_leader=0
                pro_racer_9_is_leader=0
                pro_racer_10_is_leader=0

                if(profesional_leader==pro_racer_1_position_x):
                    pro_racer_1_is_leader=1
                elif(profesional_leader==pro_racer_2_position_x):
                    pro_racer_2_is_leader=1
                elif(profesional_leader==pro_racer_3_position_x):
                    pro_racer_3_is_leader=1
                elif(profesional_leader==pro_racer_4_position_x):
                    pro_racer_4_is_leader=1
                elif(profesional_leader==pro_racer_5_position_x):
                    pro_racer_5_is_leader=1
                elif(profesional_leader==pro_racer_6_position_x):
                    pro_racer_6_is_leader=1
                elif(profesional_leader==pro_racer_7_position_x):
                    pro_racer_7_is_leader=1
                elif(profesional_leader==pro_racer_8_position_x):
                    pro_racer_8_is_leader=1
                elif(profesional_leader==pro_racer_9_position_x):
                    pro_racer_9_is_leader=1
                elif(profesional_leader==pro_racer_10_position_x):
                    pro_racer_10_is_leader=1


                time.sleep(0.2)

                #everyone died
                if(profesional_deaths==10):
                    profesional_ending_everyone_died=1
                    in_profesional_arena=0

                    print("comentator: Well... there was no winner today. But we will get new racers for next time who will carry the names of the old racers to honor their legacy. See you next time.")
                    print("Secret ending 2: The race with no survivors")


                #someone reached the goal
                elif(profesional_goal<=profesional_leader):

                    normal_profesional_race=1
                    in_profesional_arena=0

                    if(pro_racer_1_is_leader==1):
                        profesional_winner="1"
                        profesional_winner_name=pro_racer_1_name

                    elif(pro_racer_2_is_leader==1):
                        profesional_winner="2"
                        profesional_winner_name=pro_racer_2_name

                    elif(pro_racer_3_is_leader==1):
                        profesional_winner="3"
                        profesional_winner_name=pro_racer_3_name

                    elif(pro_racer_4_is_leader==1):
                        profesional_winner="4"
                        profesional_winner_name=pro_racer_4_name

                    elif(pro_racer_5_is_leader==1):
                        profesional_winner="5"
                        profesional_winner_name=pro_racer_5_name

                    elif(pro_racer_6_is_leader==1):
                        profesional_winner="6"
                        profesional_winner_name=pro_racer_6_name

                    elif(pro_racer_7_is_leader==1):
                        profesional_winner="7"
                        profesional_winner_name=pro_racer_7_name

                    elif(pro_racer_8_is_leader==1):
                        profesional_winner="8"
                        profesional_winner_name=pro_racer_8_name

                    elif(pro_racer_9_is_leader==1):
                        profesional_winner="9"
                        profesional_winner_name=pro_racer_9_name

                    elif(pro_racer_10_is_leader==1):
                        profesional_winner="10"
                        profesional_winner_name=pro_racer_10_name


                    #0 deaths
                    if(profesional_deaths==0):
                        profesional_ending_no_deaths=1

                        print(f"comentator: Nice to see that we had no deaths today, and what an amazing race! Congratulations to {profesional_winner_name} for winning. I hope everyone had a good time, and we hope to see you back here next time!")
                        print("Ending 3: A surprisingly peaceful professional race")


                    #1-3 deaths
                    elif(1 <= profesional_deaths <= 3):
                        profesional_ending_few_deaths=1

                        print("comentator: We send our thoughts to those we sadly lost during today's race.")

                        if(pro_racer_1_life<=0):
                            print(pro_racer_1_name)
                        if(pro_racer_2_life<=0):
                            print(pro_racer_2_name)
                        if(pro_racer_3_life<=0):
                            print(pro_racer_3_name)
                        if(pro_racer_4_life<=0):
                            print(pro_racer_4_name)
                        if(pro_racer_5_life<=0):
                            print(pro_racer_5_name)
                        if(pro_racer_6_life<=0):
                            print(pro_racer_6_name)
                        if(pro_racer_7_life<=0):
                            print(pro_racer_7_name)
                        if(pro_racer_8_life<=0):
                            print(pro_racer_8_name)
                        if(pro_racer_9_life<=0):
                            print(pro_racer_9_name)
                        if(pro_racer_10_life<=0):
                            print(pro_racer_10_name)

                        print(f"comentator: Despite the losses, the race was exciting. Congratulations to {profesional_winner_name} for winning! We hope you had an amazing experience and hope to see you back here next time. We'll find some replacements for the deceased.")
                        print("Ending 4: A dangerous day at the races")


                    #4-8 deaths
                    elif(4 <= profesional_deaths <= 8):
                        profesional_ending_many_deaths=1

                        print("comentator: We really had a lot of deaths today. We send our thoughts to:")

                        if(pro_racer_1_life<=0):
                            print(pro_racer_1_name)
                        if(pro_racer_2_life<=0):
                            print(pro_racer_2_name)
                        if(pro_racer_3_life<=0):
                            print(pro_racer_3_name)
                        if(pro_racer_4_life<=0):
                            print(pro_racer_4_name)
                        if(pro_racer_5_life<=0):
                            print(pro_racer_5_name)
                        if(pro_racer_6_life<=0):
                            print(pro_racer_6_name)
                        if(pro_racer_7_life<=0):
                            print(pro_racer_7_name)
                        if(pro_racer_8_life<=0):
                            print(pro_racer_8_name)
                        if(pro_racer_9_life<=0):
                            print(pro_racer_9_name)
                        if(pro_racer_10_life<=0):
                            print(pro_racer_10_name)

                        print(f"comentator: But there was still a lot of passion between the remaining contestants. Congratulations to {profesional_winner_name} for winning the race!")
                        print("Ending 5: The professional massacre")


                    #9 deaths
                    elif(profesional_deaths==9):
                        profesional_ending_only_winner_survived=1

                        print(f"comentator: ...Well. It seems like only the race winner survived. An applause for {profesional_winner_name}, I suppose. Hope you're proud of yourself.")
                        print("Ending 6: Last racer standing")


            if(normal_profesional_race==1):

                if(gambling_profesional_racer==profesional_winner):
                    gambling_profesional_winnings=gambling_profesional_money*2
                    player_money+=gambling_profesional_winnings

                    print(f"{name}: YES! My racer won! I won ${gambling_profesional_winnings}!")
                    print(f"{name}: I now have ${player_money}.")

                else:
                    print(f"{name}: Damn... racer {gambling_profesional_racer} didn't win.")
                    print(f"{name}: I lost my ${gambling_profesional_money} bet.")
                    print(f"{name}: I now have ${player_money}.")










        elif(what_stadium_do_I_go_to=="3" or what_stadium_do_I_go_to=="champion" or what_stadium_do_I_go_to=="champions league"):
            #code champion league here
            print(f"{name}: I finally arrived at the championship tournament, but apparently the ticket I bought was for a few months from now... Guess there's no game for me today then.")
            print("Ending 7: Wasted afternoon")
        else:
            print("Let me retype that, must have misspealed. I think I could write \n amature\n pro\n champion")

else:
    print("ending 1 (staying at home)")

if(normal_amature_race==1):
    print("ending 2: Normal amature race")