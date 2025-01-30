def main():
    print ("you wake up on a a lush, tropical paradise with a dense jungle interior, a sandy beach, and a lagoon, but with hints of potential danger lurking beneath its beauty, including steep cliffs, thick vegetation, and a sense of isolation due to its remote location in the middle of the ocean. do you go towards the mountain or lagoon?")
    MountainLagoon = int(input("Enter Mountain or Lagoon: "))
    if MountainLagoon == ("Mountain"):
        mountain()
    if MountainLagoon == ("Lagoon"):
        lagoon()
    
def mountain():
    print("You head towards the Moutain, on your way there you encounter a group of boys, they introduce themselves as THE CHOIR, led by Jack Merridew would you like to stay with them or go to the Lagoon?")
    Mountain = int(input("Enter StayChoirBoys or Lagoon"))
    if Mountain == ("Lagoon"):
        lagoon()
    if Mountain == ("StayChoirBoys"):
        staychoirboys()

def staychoirboys():
    print("you befriend Jack and join the CHOIR BOYS, quickly making friends with most of them. there are two distinct groups within the choir, Jack and Rogers, and the one with Simon and Sam n Eric")
    
def lagoon():
    print("You head towards the Lagoon, on your way there you encounter a boy named Piggy, would you like to stay with him or head to the Mountain?")
    Lagoon = int(input("Enter StayPiggy or Mountain"))
    if Lagoon == ("Mountain"):
        mountain()
    if Lagoon == ("StayPiggy"):
        staypiggy()

def staypiggy():
    print("You head down to the Lagoon with Piggy acompannying you. you and Piggy find a large white conch")