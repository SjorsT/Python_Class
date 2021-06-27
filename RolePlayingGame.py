import random
import os
import time

global battleNo
battleNo = 0

class Entity:
    def __init__(self, name, maxHP, damage):
        self.name = name
        self.maxHP = maxHP
        self.currentHP = self.maxHP
        self.damage = damage
        self.status = "open"

class Player(Entity):
    def __init__(self, name):
        maxHP = 100
        damage = 5
        self.gold = 50
        super().__init__(name, maxHP, damage)


class Enemy(Entity):
    def __init__(self, name, maxHP, damage, exp):
        super().__init__(name, maxHP, damage)
        self.exp = exp



def gameStart():
    
    pName = input("To begin, please enter your name: ")
    global p
    p = Player(pName, )
    print("Tip: When in battle, type 'punch' to attack or 'block' to block some damage and heal a tiny bit!")
    battleStart()

def battleStart():
    global battleNo
    battleNo += 1
    initEnemy()
    
    p.currentHP = p.maxHP
    playerTurn()

def initEnemy():
    global e
    hp = 50 + (10 * battleNo)
    damage = 5 + (1 * battleNo)
    exp = 50 + (5 * battleNo)
    e = Enemy("Verhage Clone", hp, damage, exp)
    print(f"A wild {e.name} appeared!")

def playerTurn():
    playerAction = input("Choose an action: ")
    if playerAction == 'punch':
        processHit(p, e)
        enemyTurn()
    elif playerAction == 'block':
        processBlock(p)
        enemyTurn()
    else:
        print("That is not a valid action!")
        playerTurn()

def enemyTurn():
    processHit(e, p)
    playerTurn()

def processHit(actor, target):
    damageTaken = getDamage(actor, target)
    
    target.currentHP -= damageTaken
    print(f"{actor.name} punches {target.name} for {damageTaken} damage!")

    if target.currentHP <= 0:
        target.currentHP == 0
        processDeath(actor, target)
        return

    print(f"{target.name} has {target.currentHP} HP left!")
    time.sleep(1)

def processBlock(actor):
    actor.status = "blocking"
    healAmount = getHealing(actor)
    
    actor.currentHP += healAmount
    print(f"{actor.name} blocks and heals for {healAmount}!")
    if actor.currentHP > actor.maxHP:
        actor.currentHP = actor.maxHP
    
    print(f"{actor.name} has {actor.currentHP} HP left!")
    time.sleep(1)


def processDeath(actor, target):
    print(f"{actor.name} has defeated {target.name}!")
    if isinstance(target, Player):
        print("Game over!")
        exit()
    else:
        print("Good job, but it's not over yet!")
        time.sleep(2)
        battleStart()

def getDamage(actor, target):
    damageTaken = random.randint(actor.damage, (actor.damage + 5))
    if random.randint(1, 10) == 10:
        damageTaken *= 2
        print("It's a critical hit!")
    if target.status == "blocking":
        damageTaken = int(round(damageTaken / 2))
        target.status = "open"
    return damageTaken

def getHealing(actor):
    maxHeal = int(actor.maxHP / 10)
    healAmount = random.randint(1, maxHeal)
    return healAmount


gameStart()

