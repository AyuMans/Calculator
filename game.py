
from char import player

type_name = input("What is your name?\n> ").strip()



print(f"Hello {type_name}.")
print("Ready for your first Mission?")
while True:
    ask1 = input("y/n: ").strip().lower()
    if ask1 != "y":
        print("You do not have a choice.")
   
    
    print("First Mission: Catch the Burglar")
    while True:
        begin = input("Start(s)> ").strip().lower()
        if begin == "s":
            print("A burglary has taken place at the jewellery store.")
            print(f"{type_name}, as for your first mission, Defeat The Burglar.")
            while True:
                fight1 = input("(z)> ").strip().lower()
                if fight1 == "z":
                    print("You are challenged by the Burglar")
                
                else:
                    print("Invalid")
                    continue 
        else:
            print("Invalid Option")
            continue
        
    
