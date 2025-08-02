class player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.xp = 0
        self.money = 0
        
    def attack(self, enemy):
        moves = input("Punch/Kick(p/k)\n> ").strip().lower()
        
    def stats(self):

        print(f"{self.name}|{self.hp}HP")

print("Hello")
