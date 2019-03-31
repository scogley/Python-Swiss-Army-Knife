from random import randint

def attack(weapon, hero, enemy):
	damage = randint(weapon[0], weapon[1])
	print("you rolled")
	print(damage)
	print()
	print("your hero's hit points: '")
	
	print(hero[0])
	winPhrases = ["critical hit! Your foe is crushed with your might","you blade slices the enemy in half","you smight your foe with a powerful strike to the heart","your opponent is knocked unconcious"]
	
	lossPhrases = ["you swing and miss. The enemy laughs and strikes you down with a crushing blow","your opponent dodges your attack and counters with a dagger in your heart","your attack is blocked by the enemy's shield. He counters with a penetrating jab into your ribs","your attack lands but deals minimal damage. The enemy counters with a fireball and burns you to ashes"]

	randPhraseIndex = randint(0,3)
	if damage >= enemy:
		#print("you win!")
		print(winPhrases[randPhraseIndex])
	else:
		#print("you lose!")
		print(lossPhrases[randPhraseIndex])
	return
	

def getWeapons():
	#stores the weapon and its damage range
	#key:weaponName:[minDmg,maxDmg]
	weapons = {
		"short sword": [5,9],
		"axe": [4,12],
		"broad sword": [6,10],
		"dagger": [1,12],
		"staff": [3,7]
	}
	return weapons

def getEnemies():
	#store the enemy and its hit points
	enemies = {
		"troll": 4,
		"goblin": 6,
		"orc": 8
	}
	return enemies

# [stength, defense, magic attack]
# todo: replace this list with a dict so each ability can be accessed by key instead of index
def getHeroes():
	heroes = {
		"knight": [7,7,3],
		"wizard": [2,5,10],
		"barbarian": [10,5,1],
		"ranger": [5,5,5]
	}
	return heroes

def promptForHero():
	print("Choose your hero!")
	print("1: knight    (str:7  def:7 magic:3)")
	print("2: wizard    (str:5  def:5 magic:10)")
	print("3: barbarian (str:10 def:5 magic:1)")
	print("4: ranger    (str:5  def:5 magic:5)")
	choice = input()
	if choice == "1":
		hero = "knight"
	elif choice == "2":
		hero = "wizard"
	elif choice == "3":
		hero = "barbarian"
	elif choice == "4":
		hero = "ranger"
	print("you chose the " + hero)
	return hero
	
def promptForWeapon():
	
	print("Hero, choose your weapon!")
	print("1: short sword (5-9)")
	print("2: axe (4-12)")
	print("3: broad sword (6-10)")
	print("4: dagger (1-12)")
	print("5: staff (3-7)")
	choice = input()
	
	if choice == "1":
		weapon = "short sword"
	elif choice == "2":
		weapon = "axe"
	elif choice == "3":
		weapon = "broad sword"
	elif choice == "4":
		weapon = "dagger"
	elif choice == "5":
		weapon = "staff"
	print("you chose the " + weapon)
	return weapon

def promptForEnemy():
	print("Choose your opponent!")
	print("1: troll HP 4 ")
	print("2: goblin HP 6")
	print("3: orc HP 8")
	choice = input()
	
	if choice == "1":
		enemy = "troll"
	elif choice == "2":
		enemy = "goblin"
	elif choice == "3":
		enemy = "orc"
	print("you chose the " + enemy)
	return enemy

def main():
	i = True
	while i == True:		
		weapons = getWeapons()
		heroes = getHeroes()
		enemies = getEnemies()
		heroChoice = promptForHero()
		print()
		enemyChoice = promptForEnemy()
		print()
		weaponChoice = promptForWeapon()
		attack(weapons[weaponChoice],heroes[heroChoice],enemies[enemyChoice])
		print()

#start the program
main()
