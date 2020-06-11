import random
class Land:#locations
  def __init__ (self, name, bGuy, items, rportal, lportal, riddle, rAnswer):
    self.name = name
    self.bGuy = bGuy
    self.items = items
    self.rportal = rportal
    self.lportal = lportal
    self.riddle = riddle
    self.rAnswer = rAnswer
  
  def printAttribute(self):
    print "The name is " + self.name
    print "The badguy name is " + self.bGuy.name #changed to bguy.name so is able to print actual name
    print "Items are " + self.items 
    print self.rportal.name 
    print "lportal name is " + self.lportal.name 
    print "The riddle is " + self.riddle
    # print "The answer is " + self.rAnswer
  
  def showUp(self):
    print("'\Mah walked in\.'")
    print("MAH!")
    print("You are in the " + str(self.name))
    print("An evil " + str(self.bGuy.name) + " has appeared!")
    print("MAAAHHH")  
    print("Mah: Also i think there is an " + str(self.items))
  
class Player:
  def __init__ (self, sweet, strength, flavor, luck, perception):
    self.currLand = None
    self.sweet = sweet
    self.strength = strength
    self.flavor = flavor
    self.luck = luck
    self.perception = perception
    self.innaccuracy = 10 - perception
    #now the more complicated stats
    self.stealth = (flavor + luck)/2
    self.bSize = (strength + perception)/2.5
    self.constitution = (strength + sweet)/3.5
    self.aheal = (perception + flavor)/2.5
    self.health = 100
    self.bSize = (strength+flavor)/2
    self.stealth = (luck)/2
    self.cDamage = (strength+luck)/2
    self.dodge = (flavor + luck)/2
    self.aheal = (sweet+luck)/2
    self.wins = 0
    
  def win(self):
    self.wins = self.wins+1
    
  def pAttributes(self):
    print ("I think you have changed a lot after that tough battle!")
    print ("You are in " + self.currLand.name)
    print ("You have " + str(self.sweet)+ " sweetness or charisma")
    print ("You have " + str(self.strength) + " healthiness or strength")
    print ("You have " + str(self.flavor) + " flavor or intelligence")
    print ("You have " + str(self.luck) + " candy god mother blessings or luck")
    print ("You have " + str(self.perception) + " perception")
    
  def pBuff(self):
    self.strength = self.strength + 1
    self.sweet = self.sweet + 1
    self.flavor = self.flavor + 1
    self.perception = self.perception + 1
    
# stealth, backpack, crit, dodge, rDamage #agility, charm 
#diabetes, food coma, dehydration, Tounge burn

class bGuy:
  #these are minion's resistance to these same traits in the player
  def __init__ (self, name, strength, health, sweet, flavor, constitution):
    self.name = name
    self.sweet = sweet
    self.health = health
    self.flavor = flavor
    self.strength = strength
    self.constitution = constitution
  def printStats(self):
    print(self.sweet)
    print(self.health)
    print(self.flavor)
    print(self.strength)
    print(self.const)

def choose_attack(Player, bGuy):
  while True:
    print("Do you want to attack with your Strenth, Charisma, or Intelligence")
    attack = input("type 1 for strength, 2 for charisma, or 3 for intelligence")
    if attack == "1":
      return [Player.strength, bGuy.strength]
    elif attack == "2":
      return [Player.sweet, bGuy.sweet]
    elif attack == "3":
      return [Player.flavor, bGuy.flavor]
    else:
      print("Way to go, you gunked it up. Don't worry, I'll give you another chance")
    

def sCheck(playerStat, bGuyStat):
  #this is where the battle occurs
  rNum= random.randint(0,100)
  sTotal = playerStat + bGuyStat  
  percent = 100*(playerStat/sTotal)
  if percent >= rNum:
    print("Congradulations! You are the winner!")
    return True
  else:
    print("This is actually the game over")
    print("WE ARE SORRY TO SAY THAT THE HUNGY LANDERS HAVE BEEN TAKEN CAPTIVE BY MR. TRASHY")
    SystemExit()


def Encounter(Player, bGuy):#changed to suit the purpose with the classes
  Player.currLand.showUp()
  print("You encountered " + bGuy.name)
  bHealth = random.randint(-Player.innaccuracy, Player.innaccuracy) + bGuy.health - Player.perception
  bStrength = random.randint(-Player.innaccuracy, Player.innaccuracy) + bGuy.strength - Player.perception
  bFlavor =  random.randint(-Player.innaccuracy, Player.innaccuracy) + bGuy.flavor - Player.perception
  bConstitution = random.randint(-Player.innaccuracy, Player.innaccuracy) + bGuy.constitution - Player.perception
  bSweet = random.randint(-Player.innaccuracy, Player.innaccuracy) + bGuy.sweet - Player.perception
  print("That guy looks like he has " ) + str(bHealth) + (" Health")
  print("That guy looks like he has " ) + str(bStrength) + (" Healthiness")
  print("That guy looks like he has " ) + str(bFlavor) + (" Flavor")
  print("That guy looks like he has " ) + str(bConstitution) + (" Defence")
  print("That guy looks like he has " ) + str(bSweet) + (" Tastoess")
  #print("Oh no look he actually has ") + (bHealth) + (" Health") (future to try after the battle but feore win/lost)
  [pCheckVal, bGCheckVal] = choose_attack(Player,bGuy)
  win= sCheck(pCheckVal, bGCheckVal)
  if win:
    Player.pBuff()
    Player.win()
    Player.pAttributes()
    print("Where would you like to go:")
    print("Enter one for " + Player.currLand.rportal.name)
    print("Enter two for " + Player.currLand.lportal.name)
    choice = int(input())
    if Player.wins == 4:
      Player.currland = bLand
      Encounter(Player,Player.currland.bGuy)
      if Player.wins == 5:
        print ("CONGRADULATIONS! YOU HAVE SAVED HUNGRY LAND, YOU WILL FOREVER BE OUR HERO! ")
      #bad guy boss automatically added after the winds
    elif choice == 1:
      Player.currLand = Player.currLand.rportal
      Player.currLand.bGuy=bGuyList[Player.wins]
      
      Encounter(Player, Player.currLand.bGuy)
    
    elif choice == 2:
      Player.currLand = Player.currLand.lportal
      Player.currLand.bGuy=bGuyList[Player.wins]
      Encounter(Player,Player.currLand.bGuy)

#the lower code has been blocked out because it is not needed, running Encounter again automatically keeps a loop
'''        if win:#second time asking for change in land
          Player.strength = Player.strength + 1
          Player.win()
          print("Where would you like to go:")
          print("Enter one for " + Player.currLand.rportal.name)
          print("Enter two for " + Player.currLand.lportal.name)
          choice = int(input())
       if choice == 1:#running battle for the third time
            Player.currLand = Player.currLand.rportal
            Player.currLand.bGuy=bGuyList[Player.wins]
            Encounter(Player, Player.currLand.bGuy)
            choice = int(input())

'''         
  
  
def makePlayer():
  #try catch exceptions
  print ("You only have a max of 25 attribute points currently to assign.")
  sweet = int(input("how much charisma or sweetness do you want?"))
  strength = int(input ("how much strength or healthiness against enemies do you want?"))
  flavor = int(input("How much intelligence or flavor do you want?"))
  luck = int(input("How much CandyGod Mother Blessings do you wish? Or be just don't put anything and be lucky!"))
  perception = int(input("How much perception or sugar do you want?"))
  TotStat = sweet+strength+flavor+luck+perception
  if TotStat == 25:
    print("Good job, you passed the first test")
  else:
    print("You have too many attribute points, try again!")
    makePlayer()
  return Player(sweet,strength,flavor,luck, perception)  #changed to return to make the player calss have the same values
  
  
  
def welcome():
  print "let the games begin"
  print "Welcome to Hungry Land! Glad you could joing me!"
  print "Well actually I don't have any friends    " , "(0): Maaah "
  print "whoops, sorry sometimes I can't control the urge... I guess it just happens sometimes"
  print "Anyways, what I was going to say is that you should leave, yup thats right I said you should leave"
  print "There is an evil monster named Mr. Trashy... he's been terrorizing us food kind for years, taking our fellow "+ "kinsman and keeping them prison in his lair!"
  print "So now, the heart of foodia runs on three main qualities, Sweetness, healthiness, flavor, and constitution"

#future plans
"""
def flee():
  coward = input("Would you like to stay and fight (press 1)or flee in cowardice(press 2)? ")
  if coward == "2":
    #end game switch
    print"good bye!"
  elif coward == "1":
    #end game switch
    print "Ok lets continue!"
  else:
    print "Only input english please"
    flee()
"""
  
def friends():
  friend = input ("You're going to need some serious upgrades though!, but first, do you want to be my friend?(y or n)")
#Do you want to be friends loop?
  if friend == "y":
    print" (0): MAAAH YAYYA  NOW I HAVE MY FIRST FRIEND"
    return ["y"]
  elif friend == "n":
    print"Oh ok, but don't worry, I like you a lot!"
    return ["n"]
  else:
    print("ALRIGHTY THEN")
    friends()


bGuyList = [bGuy("Fun-ion", 5,5,5,5,5),bGuy("Run-ion ", 6,6,5,4,4),bGuy("Gun-nion", 8,7,5,7,3), bGuy("Win-ion", 7,6,2,8,2), bGuy("Mr. Trasshyy", 10,10,10,1,10) ]


beach = None
forest = None
mountain = None
valley = None
forest = Land("Forest", None, "attribute potion", beach, mountain, "secret code", "qwertyuiop" )
beach = Land("Beach", None, " attirubte potion", valley, forest, "secret code", "qwertyuiop")
valley = Land("Valley", None, "attribute potion", beach, mountain, "secret code", "qwertyuiop")
mountain = Land("Mountain", None, "attribute potion", valley,forest, "secret code", "qwertyuiop")
bLand = Land("Waste Land", None, "Hungry Land Medal of Honor!", None, None, None, None)

forest.lportal=mountain
forest.rportal=valley

beach.lportal = valley
beach.rportal = forest

mountain.lportal = valley
mountain.rportal = forest

valley.lportal = valley
valley.rportal = forest


landList = [forest,mountain,valley, beach, bLand]


def start(bGuyList,landList):
  welcome()
  p1 = makePlayer()
  land_choice = -1
  while land_choice not in range(0,5):
    land_choice = input ("Where would you like to go? 0 for forest, 1 for mountain, 2 for valley, and 3 for beach")
    land_choice = int(land_choice)
    
  p1.currLand = landList[int(land_choice)]
  p1.currLand.bGuy=bGuyList[p1.wins]
  Encounter(p1,p1.currLand.bGuy)

start(bGuyList,landList)
'''
bad = bGuy("zubin 1", 5,5,5,5,5)
p1 = makePlayer() 
Encounter(p1,p1.currLand.bGu5y)
'''
SystemExit()


    