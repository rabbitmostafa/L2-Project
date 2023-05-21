
from defenitons import *
# Spider
poison = Ability("Poison", 10)
web = Ability("Web", 5)
nothing = Ability("Do nothing", 0)
rifle = Ability("Assualt rifle shooting",50)
spider = Character("Spider", 50, [poison, web, nothing], "🕷️")
# Ahmed
shoe = Ability("Shoe Strike",30)
spary = Ability("Persol Spray",40)
ahmed = Character("Ahmed",100,[shoe,spary],"🧍‍♂️")
# Alaa
punch = Ability("Punching",30)
kick = Ability("Kicking",30)
alaa = Character("Alaa",80,[punch,kick],"a")





def street():
    if rifle not in spider.list_of_abilities:
        print_pause("You walk down the street")
        print_pause("You find a new weapon!")

        spider.list_of_abilities.append(rifle)
        global  total_score
        total_score += 100
        print_pause("Assualt rifel acuaried!")
        start()
    else:
        print_pause("You walk down the street")
        print_pause("You find nothing and return back")
        start()


def house():
    print_pause("you see a human inside the house ")
    print_pause("the human notices you!")
    print_pause("the fight between the spider and the human has started")
    fight(spider,random.choice())
    input_ = process_input()
    if input_ == choice_1:
        total_score = 0
        start()
    if input_ == choice_2:
        exit()

def start():
    print_pause("You are a spider wandering in the streets")
    print_pause("you find  a house that seems to have humans inside ")
    print_pause("enter 1 to enter the house ")
    print_pause("enter 2 to keep wandering")
    input_ = process_input()
    if input_ == choice_1:
        house()
    if input_ == choice_2:
        street()


start()
