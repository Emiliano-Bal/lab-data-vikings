# Soldier
# Esta class nos da las características de un soldado. 
class Soldier:
    pass
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage


# Viking 
# Esta class nos da las características de un vikingo (Soldado modificado)
class Viking:
    pass
class Viking(Soldier):
  def __init__(self, name, health, strength):
        #super() nos permite heredar atributos de Soldier (Health y Strength)
    super().__init__(health, strength)
    self.name = name
#Este nos da el damage que recibe el Vikingo y si es que sigue vivo o no
  def receiveDamage(self, damage):
    self.health -= damage
    if self.health > 0:
      return f'{self.name} has recieved {damage} points of damage'
    else:
      return f'{self.name} has died'

  def battle_cry (self):
    return 'Odin owns you ALL!'
  

# Saxon
# Esta class nos da las características de un Saxon (Soldado modificado)

class Saxon:
    pass
class Saxon(Soldier):
  def __init__(self, health, strength):
    super().__init__(health, strength)

  def receiveDamage(self, damage):
    self.health -= damage
    if self.health > 0:
      return f'A Saxon has recieved {damage} points of damage'
    else:
      return f'A Saxon has died'


# War
# En esta añadiremos Vikingos y Saxons para que peleen entre si y logremos 
# En este caso necesiteremos importar un Rando
import random


class War(object):
  def __init__(self):
    self.vikingArmy = []
    self.saxonArmy = []

  def addViking(self, Viking):
    self.vikingArmy.append(Viking)

  def addSaxon(self, Saxon):
    self.saxonArmy.append(Saxon)

#Quitará a los Saxon muertos de la lista 
  def vikingAttack(self):
    rand_saxon = random.choice(self.saxonArmy)
    rand_viking = random.choice(self.vikingArmy)
    
    x = rand_saxon.receiveDamage(rand_viking.strength)
    if rand_saxon.health <= 0:
      self.saxonArmy.remove(rand_saxon) 
    return x

#Quitará los vikingos muertos de la lista 
  def saxonAttack(self):
    rand_viking = random.choice(self.vikingArmy)
    rand_saxon = random.choice(self.saxonArmy)

    x = rand_viking.receiveDamage(rand_saxon.strength)
    if rand_viking.health <= 0:
      self.vikingArmy.remove(rand_viking)
    return x
# Esta nos dirá como es que va la guerra y si es que alguien ya la ganó.
  def showStatus(self):
    if len(self.saxonArmy) == 0:
      return f'Vikings have won the war of the century!'
    elif len(self.vikingArmy) == 0:
      return f'Saxons have fought for their lives and survive another day...'
    elif len(self.vikingArmy) > 0 and len(self.saxonArmy) > 0:
      return f'Vikings and Saxons are still in the thick of battle.' 

