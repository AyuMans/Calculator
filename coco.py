import random
from myfunc import clear_screen
class player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.xp = 0
        self.money = 0
    def attack(self, enemy):
        
        while True:
            
            move = input("Punch/Kick\n> ").strip().lower()
            if move in ["punch", "p"]:
                fist = random.randint(5, 10)
                print(f"{self.name} Punched {enemy.name} for {fist} damage!")
                if fist == 10:
                    print("Critical Hit!")
                enemy.hp -= fist
                if enemy.hp <= 0:
                    print(f"{self.name} HP: {self.hp} | {enemy.name} HP: {enemy.hp}")
                    print(f"{self.name} has defeated {enemy.name}!")
                    print(f"{self.name} gained {enemy.xp} xp!")
                    print(f"{self.name} earned {enemy.money} EchoCoins!")
                    self.xp += enemy.xp
                    self.money += enemy.money
                    return True
                return False
            elif move in ["kick", "k"]:
                foot = random.randint(7, 14)
                print(f"{self.name} Kicked {enemy.name} for {foot} damage!")
                if foot == 14:
                    print("Critical Hit!")
                enemy.hp -= foot
                if enemy.hp <= 0:
                    print(f"{self.name} HP: {self.hp} | {enemy.name} HP: {enemy.hp}")
                    print(f"{self.name} has defeated {enemy.name}!")
                    print(f"{self.name} gained {enemy.xp} xp!")
                    print(f"{self.name} earned {enemy.money} EchoCoins!")
                    self.xp += enemy.xp
                    self.money += enemy.money
                    return True
                return False
            else:
                print("Invalid Move")
                continue
    def alive(self):
        return self.hp > 0
    def status(self):
        return f"{self.name}\n{self.hp}HP\n{self.xp}XP\n{self.money} EchoCoins"
    
class enemy:
    def __init__(self, name, hp, xp, money):
        self.name = name
        self.hp = hp
        self.xp = xp
        self.money = money
        
    def attack(self, player):
        attack_types = ["slap","punch", "kick"]
        move = random.choice(attack_types)
        if move == "slap":
            owww = random.randint(2, 3)
            print(f"{self.name} Slapped {player.name} for {owww} damage!")
            if owww == 3:
                print("Critical Hit!")
            player.hp -= owww
            if player.hp <= 0:
                print(f"{player.name} has fallen...")
                 
                
        elif move == "punch":
            oww = random.randint(3, 6)
            print(f"{self.name} Punched {player.name} for {oww} damage!")
            if oww == 6:
                print("Critical Hit!")
            player.hp -= oww
            if player.hp <= 0:
                print(f"{player.name} has fallen...")
                 
        elif move == "kick":
            ouu = random.randint(5, 10)
            print(f"{self.name} Kicked {player.name} for {ouu} damage!")
            if ouu == 10:
                print("Critical Hit!")
            player.hp -= ouu
            if player.hp <= 0:
                print(f"{player.name} has fallen...")
                
    def attack_nullveil(self, player):
        attack_types = ["Oblivion Thread", "Echo Collapse", "NullGlitch Surge"]
        move = random.choice(attack_types)
        if move == "Oblivion Thread":
            ouch = random.randint(15, 25)
            print(f"{self.name} used Oblivion Thread on {player.name} for {ouch} damage!")
            if ouch == 25:
                print("Critical Hit!")
            player.hp -= ouch
            if player.hp <= 0:
                print(f"{player.name} has blacked out....")
        elif move == "Echo Collapse":
            ow = random.randint(24, 30)
            print(f"{self.name} used Echo Collapse on {player.name} for {ow} damage!")
            if ow == 30:
                print("Critical Hit!")
            player.hp -= ow
            if player.hp <= 0:
                print(f"{player.name} has blacked out....")
        elif move == "NullGlitch Surge":
            ou = random.randint(30, 40)
            print(f"{self.name} used NullGlitch Surge on {player.name} for {ou} damage!")
            if ou == 40:
                print("Critical Hit!")
            player.hp -= ou
            if player.hp <= 0:
                print(f"{player.name} has blacked out....")
                
class bag:
    def __init__(self, med, weapon, armour, other):
        self.med = []
        self.weapon = []
        self.armour = []
        self.other = []
        
    def show_items(self, player):
        while True:
            
            choose = input("Med/Wpn/Amr/Other/Back\n(m/w/a/o/b)> ").strip().lower()
            if choose in ["back", "b"]:
                clear_screen()
                return False
            elif choose in ["med", "m"]:
                clear_screen()
                while True:
                    if self.med:
                        pass
                    else:
                        print("Empty...")
                        bck = input("Back\n(b)> ").strip().lower()
                        if bck in ["back", "b"]:
                            clear_screen()
                            break
                        else:
                            print("Invalid Option")
                            continue
            elif choose in ["weapon", "w"]:
                clear_screen()
                while True:
                    if self.weapon:
                        pass
                    else:
                        print("Empty...")
                        bck = input("Back\n(b)> ").strip().lower()
                        if bck in ["back", "b"]:
                            clear_screen()
                            break
                        else:
                            print("Invalid Option")
                            continue
            elif choose in ["armour", "amr", "a"]:
                clear_screen()
                while True:
                    if self.armour:
                        pass
                    else:
                        print("Empty...")
                        bck = input("Back\n(b)> ").strip().lower()
                        if bck in ["back", "b"]:
                            clear_screen()
                            break
                        else:
                            print("Invalid Option")
                            continue
            elif choose in ["other", "oth", "o"]:
                clear_screen()
                while True:
                    if self.other:
                        pass
                    else:
                        print("Empty...")
                        bck = input("Back\n(b)> ").strip().lower()
                        if bck in ["back", "b"]:
                            clear_screen()
                            break
                        else:
                            print("Invalid Option")
                            continue
                
                        
        
            
            
                
            
            
        
                
        