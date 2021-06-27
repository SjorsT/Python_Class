import random
import os
import time

class RolePlayingGame: 

    def __init__(self):
        self.battleNo = 0
        self.playing = True
    

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
            damage = 10
            self.gold = 50
            super().__init__(name, maxHP, damage)


    class Enemy(Entity):
        def __init__(self, name, maxHP, damage, exp):
            super().__init__(name, maxHP, damage)
            self.exp = exp



    def gameStart(self):
        
        pName = input("To begin, please enter your name: ")
        global p
        p = RolePlayingGame.Player(pName)
        print("Tip: When in battle, type 'punch' to attack or 'block' to block some damage and heal a tiny bit!")
        self.battleStart()

    def battleStart(self):
        self.battleNo += 1
        self.initEnemy()
        
        p.currentHP = p.maxHP
        self.playerTurn()

    def initEnemy(self):
        global e
        hp = 50 + (10 * self.battleNo)
        damage = 5 + (1 * self.battleNo)
        exp = 50 + (5 * self.battleNo)
        e = RolePlayingGame.Enemy("Verhage Clone", hp, damage, exp)
        print(f"A wild {e.name} appeared!")

    def playerTurn(self):
        if self.playing:
            playerAction = input("Choose an action: ")
            if playerAction == 'punch':
                self.processHit(p, e)
                self.enemyTurn()
            elif playerAction == 'block':
                self.processBlock(p)
                self.enemyTurn()
            else:
                print("That is not a valid action!")
                self.playerTurn()

    def enemyTurn(self):
        self.processHit(e, p)
        self.playerTurn()

    def processHit(self, actor, target):
        damageTaken = self.getDamage(actor, target)
        
        target.currentHP -= damageTaken
        print(f"{actor.name} punches {target.name} for {damageTaken} damage!")

        if target.currentHP <= 0:
            target.currentHP == 0
            self.processDeath(actor, target)
            return

        print(f"{target.name} has {target.currentHP} HP left!")
        time.sleep(1)

    def processBlock(self, actor):
        actor.status = "blocking"
        healAmount = self.getHealing(actor)
        
        actor.currentHP += healAmount
        print(f"{actor.name} blocks and heals for {healAmount}!")
        if actor.currentHP > actor.maxHP:
            actor.currentHP = actor.maxHP
        
        print(f"{actor.name} has {actor.currentHP} HP left!")
        time.sleep(1)


    def processDeath(self, actor, target):
        print(f"{actor.name} has defeated {target.name}!")
        if isinstance(target, self.Player):
            print("Game over!")
            self.playing = False
        else:
            print("Good job, but it's not over yet!")
            time.sleep(2)
            self.battleStart()

    def getDamage(self, actor, target):
        damageTaken = random.randint(actor.damage, (actor.damage + 5))
        if random.randint(1, 10) == 10:
            damageTaken *= 2
            print("It's a critical hit!")
        if target.status == "blocking":
            damageTaken = int(round(damageTaken / 2))
            target.status = "open"
        return damageTaken

    def getHealing(self, actor):
        maxHeal = int(actor.maxHP / 10)
        healAmount = random.randint(1, maxHeal)
        return healAmount

if __name__ == "__main__":
    RolePlayingGame().gameStart()

    
