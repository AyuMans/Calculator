import sys
from coco import bag
from myfunc import clear_screen
viewitems = bag(None, None, None, None)

class men:
    
    def menu_open(self, hero):
        while True:
            op = input("Stats\nBag\nSave\nReturn\nQuit\n(s/b/e/r/q)> ").strip().lower()
            if op in ["quit", "q"]:
                clear_screen()
                ee = input("Quit Game?\n(y/n)> ").strip().lower()
                if ee in ["yes", "y"]:
                    sys.exit()
                elif ee in ["no", "n"]:
                    clear_screen()
                    continue
            elif op in ["return", "r"]:
                clear_screen()
                return False
            elif op in ["st", "stats", "stat", "status", "s"]:
                clear_screen()
                print(f"{hero.name}\n{hero.hp}HP\n{hero.xp}XP\n{hero.money} EchocCoins")
                while True:
                    ppp = input("Back\n(b)> ").strip().lower()
                    if ppp in ["back", "b"]:
                        clear_screen()
                        break
                    else:
                        print("Invalid Option")
                        
                        continue
            elif op in ["bag", "b"]:
                clear_screen()
                open_bag = viewitems.show_items(hero)
                if not open_bag:
                    continue
                
        
                
                 
            