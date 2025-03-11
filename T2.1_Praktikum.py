import random

class Robot:
    def __init__(self, name, attack, hp, accuracy, strength):
        self.name = name
        self.attack = attack
        self.hp = hp
        self.max_hp = hp
        self.regen_point = 0
        self.attack_accuracy = accuracy
        self.defence_strength = strength

    def attack_enemy(self, enemy):
        if random.random() < self.attack_accuracy:
            damage = self.attack
            enemy.hp = max(0, enemy.hp - damage)
            print(f"{self.name} berhasil menyerang {enemy.name} dengan attack {damage}!")
        else:
            print(f"{self.name} serangannya meleset!")

    def defence(self, enemy):
        if random.random() < self.defence_strength:
            blocked_damage = enemy.attack
            self.hp = min(self.max_hp, self.hp + blocked_damage)
            print(f"{self.name} berhasil bertahan dan mengurangi damage sebesar {blocked_damage}!")
            self.regen_point += 0.1
        else:
            print(f"{self.name} gagal bertahan!")

    def regen_health(self):
        if self.regen_point >= 0.3:
            regen = 5
            self.hp = min(self.max_hp, self.hp + regen)
            print(f"{self.name} berhasil regenerasi sebanyak {regen} HP!")
            self.regen_point -= 0.2
        else:
            print(f"Regenerasi gagal! Regenerasi point anda kurang {7 - self.regen_point}")

    def is_alive(self):
        return self.hp > 0

class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2

    def start(self):
        round_num = 1
        print(f"Robot: {self.robot1.name} [Attack: {self.robot1.attack} | HP: {self.robot1.hp}]")
        print(f"Robot: {self.robot2.name} [Attack: {self.robot2.attack} | HP: {self.robot2.hp}]")
        while self.robot1.is_alive() and self.robot2.is_alive():
            print(f"\n===== Ronde {round_num} =====")
            print("1. Attack    2. Bertahan    3.  Regenerasi   4. Giveup")
            
            action1 = input(f"{self.robot1.name} memilih: ")
            action2 = input(f"{self.robot2.name} memilih: ")
            
            if action1 == "1":
                self.robot1.attack_enemy(self.robot2)
            elif action1 == "2":
                self.robot1.defence(self.robot1)
            elif action1 == "3":
                self.robot1.regen_health()
            elif action1 == "4":
                print(f"{self.robot1.name} menyerah!")
                break
            
            if self.robot2.is_alive():
                if action2 == "1":
                    self.robot2.attack_enemy(self.robot1)
                elif action2 == "2":
                    self.robot2.defence(self.robot2)
                elif action2 == "3":
                    self.robot2.regen_health()
                elif action2 == "4":
                    print(f"{self.robot2.name} menyerah!")
                    break
            
            print(f"{self.robot1.name} [HP: {self.robot1.hp} | RP: {self.robot1.regen_point}]")
            print(f"{self.robot2.name} [HP: {self.robot2.hp} | RP: {self.robot2.regen_point}]")
            round_num += 1

        if self.robot1.is_alive() and not self.robot2.is_alive():
            print(f"\n{self.robot1.name} menang!")
        elif self.robot2.is_alive() and not self.robot1.is_alive():
            print(f"\n{self.robot2.name} menang!")
        else:
            print("\nPertarungan berakhir tanpa pemenang.")

# Contoh permainan
robot1 = Robot("Titan", 10, 140, 0.4, 0.2)
robot2 = Robot("Mecha", 30, 100, 0.1, 0.5)

game = Game(robot1, robot2)
game.start()
