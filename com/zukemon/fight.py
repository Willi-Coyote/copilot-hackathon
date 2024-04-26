from random import random

from com.zukemon.arena_display import ArenaDisplay
from com.zukemon.zukemon_factory import ZukemonFactory
from com.zukemon.zukemons.fight_mode import FightMode


class Fight:
    def __init__(self):
        self.zukemon_factory = ZukemonFactory()
        self.arena_display = ArenaDisplay()
        self.high_score = 0

    def fight(self, fight_mode):
        if fight_mode == FightMode.NORMAL:
            attacker = self.zukemon_factory.create_random_zukemon()
            defender = self.zukemon_factory.create_random_zukemon()
            while True:
                attacker_damage = attacker.hit()
                defender.reduce_life_points_by(attacker_damage)
                self.arena_display.update(attacker, attacker_damage)
                if attacker_damage > self.high_score:
                    self.high_score = attacker_damage
                    print("New highscore from " + type(attacker).__name__ + ": " + str(
                        self.high_score))
                history_record = "Zukemon '" + type(attacker).__name__ + "' made " + str(
                    attacker_damage) + " damage at '" + type(defender).__name__ + "'\n"
                with open("history.txt", "a") as history_file:
                    history_file.write(history_record)
                    if defender.is_dead():
                        dead_message = "Zukemon '" + type(defender).__name__ + "' is dead looser"
                        history_file.write(dead_message)
                if defender.is_dead():
                    return attacker
                defender_damage = defender.hit()
                attacker.reduce_life_points_by(defender_damage)
                history_record = "Zukemon '" + type(defender).__name__ + "' made " + str(
                    defender_damage) + " damage at '" + type(attacker).__name__ + "'\n"
                with open("history.txt", "a") as history_file:
                    history_file.write(history_record)
                    if attacker.is_dead():
                        dead_message = "Zukemon '" + type(attacker).__name__ + "' is dead looser"
                        history_file.write(dead_message)
                print(defender_damage)
                if defender_damage > self.high_score:
                    self.high_score = attacker_damage
                    print("New highscore from " + type(attacker).__name__ + ": " + str(
                        self.high_score))
                self.arena_display.update(defender, defender_damage)
                if attacker.is_dead():
                    return defender
        elif fight_mode == FightMode.DEFEND:
            attacker = self.zukemon_factory.create_random_zukemon()
            defender = self.zukemon_factory.create_random_zukemon()
            initial_life_points = defender.get_life_points()
            defender.increase_life_points_by(5000)
            number_of_survived_rounds = 0
            while True:
                attacker_damage = attacker.hit()
                defender.reduce_life_points_by(attacker_damage)
                self.arena_display.update(attacker, attacker_damage)
                if attacker_damage > self.high_score:
                    self.high_score = attacker_damage
                    print("New highscore from " + type(attacker).__name__ + ": " + str(
                        self.high_score))
                history_record = "Zukemon '" + type(
                    attacker).__name__ + "' made " + str(
                    attacker_damage) + " damage at '" + type(defender).__name__ + "'\n"
                with open("history.txt", "a") as history_file:
                    history_file.write(history_record)
                    if defender.is_dead():
                        dead_message = "Zukemon '" + type(
                            defender).__name__ + "' has survived " + str(
                            number_of_survived_rounds) + " rounds.\n"
                        history_file.write(dead_message)
                if defender.is_dead():
                    return attacker
                defender.increase_life_points_by(initial_life_points / 10)
                number_of_survived_rounds += 1
        elif fight_mode == FightMode.ROYAL_RUMBLE:
            fighters = [self.zukemon_factory.create_random_zukemon() for _ in range(5)]
            while len(fighters) > 1:
                attacker = random.choice(fighters)
                defender = random.choice(fighters)
                while attacker == defender:
                    defender = random.choice(fighters)
                attacker_damage = attacker.hit()
                defender.reduce_life_points_by(attacker_damage)
                self.arena_display.update(attacker, attacker_damage)
                if attacker_damage > self.high_score:
                    self.high_score = attacker_damage
                    print("New highscore from " + type(attacker).__name__ + ": " + str(
                        self.high_score))
                history_record = "Zukemon '" + type(
                    attacker).__name__ + "' made " + str(
                    attacker_damage) + " damage at '" + type(defender).__name__ + "'\n"
                with open("history.txt", "a") as history_file:
                    history_file.write(history_record)
                    if defender.is_dead():
                        dead_message = "Zukemon '" + type(
                            defender).__name__ + "' is out of the royal rumble.\n"
                        history_file.write(dead_message)
                if defender.is_dead():
                    fighters.remove(defender)
            return fighters[0]
        else:
            raise ValueError(
                "FightMode '" + str(fight_mode) + "' is not a valid or known fight mode")

    def get_high_score(self):
        return self.high_score
