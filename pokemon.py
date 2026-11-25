class Stats(): #capital letter at start
    def __init__(self, HP, Attack, Defence, Speed):
        self.__HP = HP #encapsulation - private attribute - can only be accessed in this class
        self.__Attack = Attack
        self.__Defence = Defence
        self.__Speed = Speed
        
    def GetHP(self):
        return self.__HP
           
    def Increase(self,Amount):
        if Amount > 0:
            self.__HP += Amount
            self.__Attack += Amount
            self.__Defence += Amount
            self.__Speed += Amount

class Move():
    def __init__(self, Name, Element, Power):
        self.__Name = Name
        self.__Element = Element
        self.__Power = Power
    def GetDescription(self):
        return f"{self.Name}({self.__Element}, {self.__Power})"
    
## SUPERCLASS
class Creature(): #includes items that every single creature has regardless of type
    def __init__(self, Name, Level, Element, HP, Attack, Defence, Speed):
        self.__Name = Name
        self.__Level = Level
        self._Element = Element #protected attribute as subclasses will override
        self._Stats = Stats(HP, Attack, Defence, Speed) #composition: the stats object is inside creature
        self._Moves = []

  def GetName(self):
    return self.__Name

  def GetLevel(self):
    return self.__Level

  def GetElement(self):
    return self._Element

  def SetLevel(self, NewLevel):
    if 1 <= NewLevel <= 100:
      self.__Level = Newlevel
    else:
      print(f" {NewLevel} is not a valid level for {self.__Name}")

  def LevelUp(self):
    if self.__Level < 100:
      self.__Level += 1
      self._Stats.Increase(2)

  def LearnMove(self, Name, Power):
    self._Moves.append(Move(Name, self._Element, Power)) # Composition

  def GetStrongAgainst(self):
    return "Nothing"

  def GetWeakAtgainst(self):
    return "Nothing"

  def GetSpecialAbility(self):
    return "None"

class FireCreature(Creature): #Inheritance: a second subclass of the same subclass
  def __init__(self, Name, Level, Element, HP, Attack, Defence, Speed, FlameTemperature):
    super().__init__(Name, Level, Element, HP, Attack, Defence, Speed)
    self.__FlameTemperature = FlameTemperature
  def GetStrongAgainst(self):
    return "Grass"

  def GetWeakAgainst(self):
    return "Water"

  def GetSpecialAbility(self):
    return f"Burns at {self.__FlameTemperature}C"

Emberpup = FireCreature("Emberpup", 12, 39, 52, 43, 65, FlameTemperature=800)
Blazewing = FireCreature("Blazewing", 30, 78, 84, 78, 100, FlameTemperature=1500)
Emberpup.LearnMove("Ember", 40)
Emberpup.LearnMove("Flame Tail", 60)
Emberpup.SetLevel(150)
Emberpup.LevelUp()

class WaterCreature(Creature):
  def __init__(self, Name, Level, Element, HP, Attack, Defence, Speed):
    super().__init__(Name, Level, Element, HP, Attack, Defence, Speed)

  def GetStrongAgainst(self):
    return "Fire"

  def GetWeakAgainst(self):
    return "Electric"


Anchoir = WaterCreature("Anchoir", 13, 42, 50, 40, 67)
Anchoir.LearnMove("Anchor Smash", 50)
Anchoir.LearnMove("Tsunami", 70)
Anchoir.SetLevel(83)
Anchoir.LevelUp()

class GrassCreature(Creature):
  def __init__(self, Name, Level, Element, HP, Attack, Defence, Speed):
    super().__init__(Name, Level, Element, HP, Attack, Defence, Speed)

  def GetStrongAgainst(self):
    return "Water"

  def GetWeakAgainst(self):
    return "Fire"

Sproutlet = GrassCreature("Sproutlet", 14, 50, 51, 42, 60)
Sproutlet.LearnMove("Bramble Bash", 30)
Sproutlet.LearnMove("Splinter Jab", 20)
Sproutlet.SetLevel(30)
Anchoir.LevelUp()
    
  

  

  

