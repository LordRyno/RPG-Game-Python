import random
import math

pLvl = 1
pHp = 5
pHpMax = 5
pDmg = 1
hPot = 1
pGold = 10
pXp = 0


def Battle(mName, mHp, mDmg):

    global pHp
    global hPot
    global battleLose
    global pGold
    global pXp
    global pHpMax
    global pDmg
    global pLvl
    
    LootHp = mHp
    LootDmg = mDmg
    print("A", mName, "approaches!")
    while True:
        cmd = int(input("1. Attack\n2. Heal\n3. Flee\n4. Check\n"))
        if cmd == 1:
            print("You Attacked And Did", pDmg, "Damage!")
            mHp = (mHp - pDmg)
            if mHp < 1:
                pGold = pGold + LootHp
                pXp = pXp + LootHp + LootDmg
                print("The", mName, "Is Defeated!\nYou Gained", LootHp + LootDmg, "XP and", LootHp, "Gold")
                break
            print(mName, "HP:", mHp)
            print("The", mName, "Attacks!\nYou Took", mDmg, "Damage!")
            pHp = (pHp - mDmg)
            if pHp < 1:
                print("You Are Defeated!")
                battleLose = True
                break
            print("Player HP:", pHp)
            continue
        elif cmd == 2:
            if hPot >= 1:
                print("You Healed")
                hAmmount = (pHpMax - pHp)
                pHp = hAmmount + pHp
                hPot = (hPot - 1)
                print("The", mName, "Attacks!\nYou Took", mDmg, "Damage!")
                pHp = (pHp - mDmg)
                if pHp < 1:
                    print("You Are Defeated!")
                    battleLose = True
                    break
                print("Player HP:", pHp)
                continue
            else:
                print("You're Out Of Health Potions!")
                print("The", mName, "Attacks!\nYou Took", mDmg, "Damage!")
                pHp = (pHp - mDmg)
                print("Player HP:", pHp)
                if pHp < 1:
                    print("You Are Defeated!")
                    battleLose = True
                    break
                else:
                    continue
        elif cmd == 3:
            fleeChance = random.randint(1,2)
            if fleeChance == 1:
                print("You Fled!")
                break
            else:
                print("You Failed To Flee!")
                print("The", mName, "Attacks!\nYou Took",(2 * mDmg), "Damage!")
                pHp = (pHp - (2 * mDmg))
                if pHp < 1:
                    print("You Are Defeated!")
                    battleLose = True
                    break
                print("Player HP:", pHp)
                continue
        elif cmd == 4:
            print(str(mName) + ":", "\nHealth:" + str(mHp),"\nDamage:" + str(mDmg))
        else:
            continue

def PlayerXPDONTUSE(pXp, pHpMax, pDmg, pLvl): #Scrapped xp function
    if pXp >= 1:
        print("You've Leveled Up!\n You Are Now Level 2!")
        pLvl = pLvl + 1
        pHpMax = pHpMax + 5
        pDmg = pDmg + 1

def PlayerXP():
    global pXp, pHpMax, pDmg, pLvl, pHp
    
    requiredXp = pLvl * 10  # XP required to level up increases with each level
    while pXp >= requiredXp:  # Allows for multiple level-ups if XP exceeds requirement
        print(f"You've Leveled Up! You Are Now Level {pLvl + 1}!")
        pLvl += 1
        pHpMax += 5  # Increase HP by 5 each level
        pDmg += 1    # Increase Damage by 1 each level
        pHp = pHpMax  # Restore HP to the new maximum
        pXp -= requiredXp  # Subtract the required XP from current XP
        requiredXp = pLvl * 10  # Update required XP for next level

def Shop():
    global pGold, hPot
    while True:
        try:
            ShopChoice = int(input("--Shop--\n1. Health Potion: 5 Gold\n2. Leave\n"))
            if ShopChoice == 1:
                if pGold >= 5:
                    pGold = pGold - 5
                    hPot = hPot + 1
                    print("You Now Have", hPot, "Health Potions")
                    break
                else:
                    print("You Don't Have Enough Gold!")
                    break
            else:
                break
        except:
            print("PLease Enter Valid Inputs")

def Fights():
    global pHp
    global hPot
    global battleLose
    global pGold
    global pXp
    global pHpMax
    global pDmg
    global pLvl
    global battleLose
    while True:
        if pLvl < 3:
            encounter = random.choice(Encounterslvl1)
            Battle(encounter["name"], encounter["hp"], encounter["dmg"])
            if battleLose == True:
                break
            else:
                continue
        else:
            encounter = random.choice(Encounterslvl3)
            Battle(encounter["name"], encounter["hp"], encounter["dmg"])
            if battleLose == True:
                break
            else:
                continue    
    
    
    
        

    


Encounterslvl1 = [
    {"name": "Goblin", "hp": 10, "dmg": 2},
    {"name": "Imp", "hp": 5, "dmg": 1},
    {"name": "Chicken", "hp": 1, "dmg": 0},
    {"name": "Rat", "hp": 7, "dmg": 1} 
]

Encounterslvl3 = [
	{"name": "Bandit", "hp": 18, "dmg": 4},
	{"name": "Brandon", "hp": 15, "dmg": 5},
        {"name": "Rat", "hp": 7, "dmg": 1},
        {"name": "Goblin", "hp": 10, "dmg": 2}    
]	

print("Welcome!")
while True:
    PlayerXP()
    try:
        Choice1 = int(input("Would you like to:\n1. Visit Shop\n2. Fight Monsters\n3. Check Stats\n4. Quit Game\n"))
        if Choice1 == 1:
            Shop()
            continue
        elif Choice1 == 2:
            Fights()
            if battleLose == True:
                break
            else:
                continue
        elif Choice1 == 3:
            print("--Player Stats--\nLevel:", pLvl, "\nMax HP:", pHpMax, "\nCurrent HP:", pHp, "\nDamage:", pDmg, "\nGold:", pGold, "\nXP:", pXp)
        elif Choice1 == 4:
            break
        else:
            print("Enter 1, 2, or 3")
            continue
    except:
        print("Enter 1, 2, or 3")
        continue
        
    

print("--Game Over--") 
    
