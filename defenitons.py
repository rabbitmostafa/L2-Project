import time
import random

choice_1 = "1"
choice_2 = "2"
total_score = 0


class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage
        self.uses = 0

    def damage_randomize(self):
        if self.max_damage == 0:
            return 0
        self.damage = random.randint(4, self.max_damage)
        return self.damage


class Character:
    def __init__(self, name, max_health, list_of_abilities, graphic):
        self.name = name
        self.max_health = max_health
        self.health = self.max_health
        self.max_dashes = max_health / 5
        self.list_of_abilities = list_of_abilities
        self.graphic = graphic

    def draw_health_bar(self):
        dashes = int(self.health / 5)
        empty_dashes = int(self.max_dashes - dashes)
        empty_dashes_string = " " * empty_dashes
        dashes_string = "-" * dashes
        if self.health < 0:
            self.health = 0
        print_pause(f"{self.name} HP:{self.health}")
        print_pause("[" + dashes_string + empty_dashes_string + "]")


def process_input():
    while True:
        input_ = str(input())
        if input_ != choice_1 and input_ != choice_2:
            print_pause("please enter a valid input")
            continue
        else:
            break
    return input_


def print_pause(text):
    print(text)
    time.sleep(2)


def fight(spider, enemy):
    print_pause(
        f"""


                  {spider.graphic}         {enemy.graphic}
            --------------------------------------------------
            """
    )
    start_time = time.time()
    while spider.health >= 0:
        spider_turn(spider, enemy)
        enemy_turn(spider, enemy)
        if enemy.health <= 0:
            end_time = time.time()
            time_taken = end_time - start_time
            time_penalty = 5
            print_pause("You win! play again yes = 1 no = 2")
            spider.level += 1
            global total_score
            total_score = int(100 + (time_taken * time_penalty))
            print_pause(f"Score: {total_score}")
            break
        if spider.health <= 0:
            end_time = time.time()
            time_taken = end_time - start_time
            time_penalty = 5
            total_score = int(0 + (time_taken * time_penalty))
            print_pause("You lost . play again ? yes = 1 no = 2")
            print_pause(f"Score: {total_score}")
            break


def spider_turn(spider, enemy):
    print_pause("your turn!")
    spider.draw_health_bar()
    print_pause("choose a skill move!")
    i = 1
    for a in spider.list_of_abilities:
        print_pause(f"{i}>{a.name}")
        i += 1
    while True:
        try:
            input_ = process_input_for_fight()
            input_int = int(input_) - 1
            damage_value_randomized = spider.list_of_abilities[input_int].damage_randomize()
            ability_name = spider.list_of_abilities[input_int].name
            break
        except:
            print_pause("please enter a valid input")
    print_pause(
        f"the spider used its {ability_name} ability "
        f"and dealt {damage_value_randomized}HP of damage!"
    )

    enemy.health -= damage_value_randomized
    enemy.draw_health_bar()


def enemy_turn(spider, enemy):
    if enemy.health == 0:
        return
    print_pause(f"{enemy.name} turn!")
    skill_enemy_move = random.randint(0, len(enemy.list_of_abilities)) - 1
    damage_randomized = enemy.list_of_abilities[skill_enemy_move].damage_randomize()
    ability_name = enemy.list_of_abilities[skill_enemy_move].name
    print_pause(
        f"the {enemy.name} used its {ability_name} ability "
        f".and dealt {damage_randomized} HP of damage!"
    )
    spider.health -= damage_randomized

def process_input_for_fight():
    while True:
        try:
            return int(input())
        except:
            print_pause("please enter a valid input")
