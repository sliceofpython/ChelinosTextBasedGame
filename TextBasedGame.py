#shebanghere
#documentation here
#This is a simple(ish) text based game I am creating to enhance my Python skills

#import modules HERE
import threading
import random
import time
from colorama import Fore, Style, init
init(autoreset=True)


#class item HERE
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.attackBonus = 0
        self.defenseBonus = 0
        
#create items Here
kitchenKnife = Item(Fore.CYAN + Style.DIM + "kitchen knife",
                    Fore.CYAN + Style.DIM + "\n---A Kitchen Knife---\n" + Fore.WHITE + Style.BRIGHT + "\tIt's a kitchen knife, good for cutting and good for stabbing.\n")

note = Item(Fore.CYAN + Style.DIM + "note",
                    Fore.CYAN + Style.DIM + "\n---A Note---\n" + Fore.WHITE + Style.BRIGHT + "\tDear self,\n\t\tDO IT! DO IT NOW!!!\n")

oldPants = Item(Fore.CYAN + Style.DIM + "pair of old pants",
                    Fore.CYAN + Style.DIM + "\n---A Pair of Old Pants---\n" + Fore.WHITE + Style.BRIGHT + "\tThese pants smell like old.\n")

kitchenKnife.attackBonus = 10

oldPants.defenseBonus = 5

#class creature HERE
class Creature:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.inventory = []
        self.hp = 0
        self.attack = 0
        self.defense = 0
        self.give_xp = 0


#create creatures here

bob = Creature(Fore.CYAN + Style.BRIGHT + "Bob",
               Fore.CYAN + Style.BRIGHT + "\n===Bob===\n" + Fore.WHITE + "\tA middle aged man dressed like a cowboy.\n")

bob.hp = 5
bob.attack = 2
bob.defense = 1
bob.give_xp = 15

ghost = Creature(Fore.CYAN + Style.BRIGHT + "A ghost",
                 Fore.CYAN + Style.BRIGHT + "\n===Ghost===\n" + Fore.WHITE + "\tThis is a scary ghost.\n")

ghost.hp = 10
ghost.attack = 3
ghost.defense = 1
ghost.give_xp = 25

girl = Creature(Fore.CYAN + Style.BRIGHT + "A small girl",
                Fore.CYAN + Style.BRIGHT + "\n===A Small Girl===\n" + Fore.WHITE + "\tThis girls looks to be about 3 years old.\n")

girl.hp = 2
girl.attack = 1
girl.defense = 0
girl.give_xp = 100

fatTony = Creature(Fore.CYAN + Style.BRIGHT + "Fat Tony",
                Fore.CYAN + Style.BRIGHT + "\n===Motherfucking Fat Tony===\n" + Fore.WHITE + "\tGod damnit I hate this guy! Fucking Fat Tony!\n")

fatTony.hp = 100
fatTony.attack = 10
fatTony.defense = 7
fatTony.give_xp = 1000

#class room HERE
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.north = 0
        self.east = 0
        self.south = 0
        self.west = 0
        self.creatures = []
        self.inventory = []


#create rooms here       
livingRoom = Room(Fore.RED + Style.BRIGHT + "\n---The Living Room---",
                  Style.BRIGHT + "\tThis is the living room.  It looks much like any other living room. There is couch and a few armchairs.  Oooh, the coffe table is nice!  It'd be a shame is someone were to stain it with some blood.\n" + Fore.GREEN + Style.BRIGHT + "Exits: North, East, West\n")

kitchen = Room(Fore.RED + Style.BRIGHT + "\n---The Kitchen---",
               Style.BRIGHT + Fore.WHITE + "\tThis is the kitchen.  There's a countertop made of marble.  A refrigerator sits against the south wall.  Shit it's messy up in here.  Hell, it'd actually be an improvement of someone were to add a little blood.\n" + Fore.GREEN + Style.BRIGHT + "Exits: East\n")

diningRoom = Room(Fore.RED + Style.BRIGHT + "\n---The Dining Room---",
                  Style.BRIGHT + Fore.WHITE + "\tThis is the place where we eat our meals.  It's quite open and there is a good air flow in here.  Six wooden chairs surround a large wooden table.  The only thing missing in this room is a little blood.\n" + Fore.GREEN + Style.BRIGHT + "Exits: South, West\n")

hallway = Room(Fore.RED + Style.BRIGHT + "\n---The Hallway---",
               Style.BRIGHT + Fore.WHITE + "\tThis is a simple hallway.  No, seriously, it's just a freaking hallway.  Why are you so interested in a long fancy description about this place?  Mind your own damn business and get on with it.  Also, blood.\n" + Fore.GREEN + Style.BRIGHT + "Exits: North, East, West\n")

bathroom = Room(Fore.RED + Style.BRIGHT + "\n---The Bathroom---",
                Style.BRIGHT + Fore.WHITE + "\tThis is where we poop.  Well, in the toilet maybe.  Of which there is one.  There is also a fancy shmancy marble bathtub big enough to fit an elephant.  I wonder what it would look like if it were filled with blood.\n" + Fore.GREEN + Style.BRIGHT + "Exits: South\n")

bedroom = Room(Fore.RED + Style.BRIGHT + "\n---A Child's Bedroom---",
               Style.BRIGHT + Fore.WHITE + "\tThis seems to be the bedroom of a small child.  Aw hell no!  You don't think I'm gonna write some crazy ass description eventually leading to... blood, do you?  That shit's wicked cray.  Leave the children alone.\n" + Fore.GREEN + Style.BRIGHT + "Exits: West\n")

masterBedroom = Room(Fore.RED + Style.BRIGHT + "\n---The Master Bedroom---",
                     Style.BRIGHT + Fore.WHITE + "\tThis is the bedroom of the master.  Or is it?  Maybe it's your bedroom?  Maybe... you're the master.  Well, is you is or is you ain't the master?  Proove it by spilling a little blood... or a lot!\n" + Fore.GREEN + Style.BRIGHT + "Exits: East\n")

#TODO: add monsters to rooms

livingRoom.north = diningRoom
livingRoom.east = hallway
livingRoom.west = masterBedroom
livingRoom.creatures = [bob]

kitchen.east = diningRoom
kitchen.creatures = [fatTony]
kitchen.inventory = [kitchenKnife]

diningRoom.south = livingRoom
diningRoom.west = kitchen

hallway.north = bathroom
hallway.east = bedroom
hallway.west = livingRoom

bathroom.south = hallway
bathroom.creatures = [ghost]

bedroom.west = hallway
bedroom.creatures = [girl]

masterBedroom.east = livingRoom
masterBedroom.inventory = [oldPants]


#MAIN HERE
def main():

#move command to switch between rooms   
    def move(direction):
        global currentRoom

        exitsDict = {"north":currentRoom.north, "east":currentRoom.east, "south":currentRoom.south, "west":currentRoom.west}
        
        if direction in exitsDict and exitsDict[direction] != 0:
            currentRoom = exitsDict[direction]
            checkRoom()
        else:
            print(Fore.WHITE + Style.BRIGHT + "\nYou can't go that way.\n")

#used to translate dict value to class object instance
    def translateObject(translateThis):
        global nextObject
        
        if translateThis == ['bob']:
            nextObject = bob
        elif translateThis == ['ghost']:
            nextObject = ghost
        elif translateThis == ['girl']:
            nextObject = girl
        elif translateThis == ['tony']:
            nextObject = fatTony
        elif translateThis == ['knife']:
            nextObject = kitchenKnife
        elif translateThis == ['note']:
            nextObject = note
        elif translateThis == ['pants']:
            nextObject = oldPants      

#the look command will return descriptions of the object looked at (or the room if no object specified)
    def look(atObject = 0):   
        if atObject == 0:
            checkRoom()
        elif atObject in currentRoom.creatures or atObject in currentRoom.inventory:
            print(atObject.description)
        elif atObject in heroInventory:
            print(atObject.description)
        elif atObject != 0 and atObject not in currentRoom.creatures or atObject not in currentRoom.inventory or atObject not in heroInventory:
            print("\n{} ".format(atObject.name) + Fore.WHITE + Style.BRIGHT + "is not in this room.\n")

#The drop command for use with items
    def drop(item):
        if item not in heroInventory:
            print("\nYou don't have that item.\n")
        else:
            heroInventory.remove(item)
            currentRoom.inventory.append(item)
            print("\nYou dropped it.\n")
            
#The get command
    def get(item):
        if item not in currentRoom.inventory:
            print("\nThat item is not here.\n")
        else:
            currentRoom.inventory.remove(item)
            heroInventory.append(item)
            print("\nYou got it.\n")
            
#the wear command
    def wear(item):
        global wearingAnything
        global heroDefense
        
        if item not in heroInventory:
            print("\nYou don't have that item.\n")
        elif wearingAnything == True:
            print("\nTry removing something first.\n")
        else:
            wearingAnything = True
            heroDefense = heroDefense + item.defenseBonus
            item.name = item.name + " (wearing)"
            print("\nYou wore it.\n")
            
#the remove command
    def remove(item):
        global wearingAnything
        global heroDefense
        
        if item not in heroInventory:
            print("\nYou don't have that item.\n")
        elif wearingAnything == False:
            print("\nTry wearing something first.\n")
        else:
            wearingAnything = False
            heroDefense = heroDefense - item.defenseBonus
            item.name = item.name[:-10] #this removes (wearing) from the end of the item.name
            print("\nYou took it off.\n")

#the wield command
    def wield(weapon):
        global wieldingAnything
        global heroAttack
        
        if weapon not in heroInventory:
            print("\nYou don't have that item.\n")
        elif wieldingAnything == True:
            print("\nTry removing something first.\n")
        else:
            wieldingAnything = True
            heroAttack = heroAttack + weapon.attackBonus
            weapon.name = weapon.name + " (wielding)"
            print("\nYou wielded it.\n")       

#the unwield command
    def unwield(weapon):
        global wieldingAnything
        global heroAttack
        
        if weapon not in heroInventory:
            print("\nYou don't have that item.\n")
        elif wieldingAnything == False:
            print("\nTry wielding something first.\n")
        else:
            wieldingAnything = False
            heroAttack = heroAttack - weapon.attackBonus
            weapon.name = item.name[:-11] #this removes (wielding) from the end of the weapon.name
            print("\nYou took it off.\n")

#checkRoom
    def checkRoom():
        print(currentRoom.name)
        print(currentRoom.description)
        if currentRoom.creatures != []:
            for creature in currentRoom.creatures:
                print(creature.name + Fore.WHITE + " is here.")
        if currentRoom.inventory != []:
                    for item in currentRoom.inventory:
                        print(Fore.WHITE + Style.BRIGHT + "A " + item.name + Fore.WHITE + Style.BRIGHT + " is here.")

#combat system HERE                        
    def kill(creature):
        global heroHp
        global heroExperience
        global heroAttack
        global heroDefense
        global heroLevel
        global still_alive
        
        translateObject(creature)
        while True:
            heroHit = random.randint(0,6) + heroAttack
            enemyHit = random.randint(0,6) + nextObject.attack
            heroDamageTaken = enemyHit - heroDefense
            if heroDamageTaken < 0:
                heroDamageTaken = 0
            enemyDamageTaken = heroHit - nextObject.defense
            if enemyDamageTaken < 0:
                enemyDamageTaken = 0
            
            print(Fore.WHITE + Style.BRIGHT + "\nYou deal " + Fore.MAGENTA + Style.BRIGHT + str(enemyDamageTaken) + Fore.WHITE + Style.BRIGHT + " damage to " + str(nextObject.name) + "!\n")    
            nextObject.hp = nextObject.hp - enemyDamageTaken
            if nextObject.hp <= 0:
                print(Fore.WHITE + Style.BRIGHT + "\nYou killed " + str(nextObject.name) + "!\n")
                heroExperience = heroExperience + nextObject.give_xp
                currentRoom.creatures.remove(nextObject)
                gonnaRespawn = threading.Thread(target=respawn, args=(nextObject, currentRoom))
                gonnaRespawn.start()
                #add items drop function and call
                while heroExperience >= 100:
                    heroAttack += 5
                    heroDefense += 2
                    heroHp += 10
                    heroExperience -= 100
                    heroLevel += 1
                break
            print(str(nextObject.name) + Fore.WHITE + Style.BRIGHT + " deals " + Fore.MAGENTA + Style.BRIGHT + str(heroDamageTaken) + Fore.WHITE + Style.BRIGHT + " damage to you!\n")
            heroHp = heroHp - heroDamageTaken
            if heroHp <= 0:
                still_alive = False
                print("\n" + str(nextObject.name) + Fore.YELLOW + Style.BRIGHT + " KILLED" + Fore.WHITE + Style.BRIGHT + " you!\n")
                break
            print(Fore.YELLOW + Style.BRIGHT + "Hero:" + Fore.BLUE + " HP " + Fore.WHITE + str(heroHp) + Fore.BLUE +
                           " Exp " + Fore.WHITE + str(heroExperience) + Fore.BLUE + ">> ")
            time.sleep(2)

#respawn HOLY CRAP THIS IS HARDER THAN I THOUGHT, lookup parallel programming, do this later
    def respawn(who, where):
        global nextObject
        global currentRoom
        who = nextObject
        where = currentRoom
        
        time.sleep(20)
        where.creatures.append(who)
        
#Rest command
    def rest():
        global heroHp
        
        print(Fore.WHITE + Style.BRIGHT + "\nYou are resting...")
        time.sleep(2)
        print(Fore.WHITE + Style.BRIGHT + "\n...")
        time.sleep(2)
        print(Fore.WHITE + Style.BRIGHT + "\n...")
        time.sleep(1)
        print(Fore.WHITE + Style.BRIGHT + "\nResting complete!\n")
        heroHp = heroHp + 10
        #add a max to hp

#help command list commands
    helpCommand = (Fore.YELLOW + Style.BRIGHT + "\nTry typing in one of the following commands\n\n" 
    + Fore.MAGENTA + Style.BRIGHT + "north, south, east, west " + Fore.WHITE + Style.BRIGHT + "- move to adjacent room\n"
    + Fore.MAGENTA + Style.BRIGHT + "look " + Fore.WHITE + Style.BRIGHT + "- look at current room\n"
    + Fore.MAGENTA + Style.BRIGHT + "look <creature> " + Fore.WHITE + Style.BRIGHT + "- look at a creature\n"
    + Fore.MAGENTA + Style.BRIGHT + "look <object> " + Fore.WHITE + Style.BRIGHT + "- look at an object\n"
    + Fore.MAGENTA + Style.BRIGHT + "stats " + Fore.WHITE + Style.BRIGHT + "- see hero's stats\n"
    + Fore.MAGENTA + Style.BRIGHT + "inv " + Fore.WHITE + Style.BRIGHT + "- view hero's inventory\n"
    + Fore.MAGENTA + Style.BRIGHT + "get " + Fore.WHITE + Style.BRIGHT + "- pick up an object\n"
    + Fore.MAGENTA + Style.BRIGHT + "drop " + Fore.WHITE + Style.BRIGHT + "- drop an object\n"
    + Fore.MAGENTA + Style.BRIGHT + "wear " + Fore.WHITE + Style.BRIGHT + "- wear an item\n"
    + Fore.MAGENTA + Style.BRIGHT + "wield " + Fore.WHITE + Style.BRIGHT + "- hold a weapon\n"
    + Fore.MAGENTA + Style.BRIGHT + "remove " + Fore.WHITE + Style.BRIGHT + "- take off an item\n"
    + Fore.MAGENTA + Style.BRIGHT + "unwield " + Fore.WHITE + Style.BRIGHT + "- remove a weapon\n"
    + Fore.MAGENTA + Style.BRIGHT + "kill <creature> " + Fore.WHITE + Style.BRIGHT + "- fight a creature\n"
    + Fore.MAGENTA + Style.BRIGHT + "rest " + Fore.WHITE + Style.BRIGHT + "- rest and regenerate hp\n"
    + Fore.MAGENTA + Style.BRIGHT + "quit " + Fore.WHITE + Style.BRIGHT + "- leave the game\n")
    

###CURRENT ROOM INITIATED HERE
    global currentRoom
    currentRoom = livingRoom
    checkRoom()

#Hero Stats
    global heroHp
    heroHp = 25
    global heroExperience
    heroExperience = 0
    global heroAttack
    heroAttack = 3
    global heroDefense
    heroDefense = 2
    global heroInventory
    heroInventory = [note]
    global wearingAnything
    wearingAnything = False
    global wieldingAnything 
    wieldingAnything = False
    global heroLevel
    heroLevel = 1
        
#alive loop and commands    
    global still_alive
    still_alive = True
    while still_alive == True:
            
#what do prompt
        userInput = input(Fore.YELLOW + Style.BRIGHT + "Hero:" + Fore.BLUE + " HP " + Fore.WHITE + str(heroHp) + Fore.BLUE +
                           " Exp " + Fore.WHITE + str(heroExperience) + Fore.BLUE + ">> " + Fore.WHITE).lower()
        userInputList = userInput.split(" ")     
        nextCommand = userInputList[0]
        global nextObject
        nextObject = ""
        if len(userInputList) > 1: 
            translateMe = userInputList[1:]
            translateObject(translateMe)
        
        if nextCommand == 'north':
            move(nextCommand)
        elif nextCommand == 'east':
            move(nextCommand)
        elif nextCommand == 'south':
            move(nextCommand)
        elif nextCommand == 'west':
            move(nextCommand)
        elif nextCommand == 'look' and nextObject == '':
            look()
        elif nextCommand == 'look' and nextObject != '':
            look(nextObject)
        elif nextCommand == 'stats':
            print(Fore.YELLOW + Style.BRIGHT + "\n***HERO***\n" + Fore.MAGENTA + "Level: " + Fore.WHITE + str(heroLevel) + "\n"
                  + Fore.WHITE + "Attack Power = " + str(heroAttack) + "\nDefense Power = " + str(heroDefense) + "\n")
        elif nextCommand == 'help':
            print(helpCommand)
        elif  nextCommand == 'inv':
            print("\nYou currently have:")
            for item in heroInventory:
                print(item.name)
            print("")
        elif nextCommand == 'get' and nextObject != '':
            get(nextObject)
        elif nextCommand == 'drop' and nextObject != '':
            drop(nextObject)
        elif nextCommand == 'wear' and nextObject != '':
            wear(nextObject)
        elif nextCommand == 'remove' and nextObject != '':
            remove(nextObject)
        elif nextCommand == 'wield' and nextObject != '':
            wield(nextObject)
        elif nextCommand == 'unwield' and nextObject != '':
            unwield(nextObject)
        elif nextCommand == 'kill' and nextObject == '':
            print(Fore.WHITE + Style.BRIGHT + "\nKill who?\n")
        elif nextCommand == 'kill' and nextObject != '':
            kill(nextObject)
        elif nextCommand == 'rest':
            rest()
        #save
        elif nextCommand == 'quit':
            print("\nNow quitting the game...")
            #need to add proper exit of possible running threads
            quit()
        else:
            print("\nI don't understand.  Try again.\n")
        #add save command

    print(Fore.RED + Style.BRIGHT + "\nYou died!\n\nGame Over!\n")
    #need to add proper exit of possible running threads
    quit()



if __name__ == "__main__": main()
