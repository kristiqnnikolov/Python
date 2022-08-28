# You got your hands on the most recent update on the best MMORPG of all time – Heroes of Code and Logic.
# You want to play it all day long! So cancel all other arrangements and create your party!
# On the first line of the standard input, you will receive an integer n – the number of heroes that you can choose
# for your party. On the next n lines, the heroes themselves will follow with their hit points and mana points
# separated by a single space in the following format:
# "{hero name} {HP} {MP}"
# -	HP stands for hit points and MP for mana points
# -	a hero can have a maximum of 100 HP and 200 MP
# After you have successfully picked your heroes, you can start playing the game.
# You will be receiving different commands, each on a new line, separated by " – ", until the "End" command is given.
# There are several actions that the heroes can perform:
# "CastSpell – {hero name} – {MP needed} – {spell name}"
# •	If the hero has the required MP, he casts the spell, thus reducing his MP. Print this message:
# o	"{hero name} has successfully cast {spell name} and now has {mana points left} MP!"
# •	If the hero is unable to cast the spell print:
# o	"{hero name} does not have enough MP to cast {spell name}!"
# "TakeDamage – {hero name} – {damage} – {attacker}"
# •	Reduce the hero HP by the given damage amount. If the hero is still alive (his HP is greater than 0) print:
# o	"{hero name} was hit for {damage} HP by {attacker} and now has {current HP} HP left!"
# •	If the hero has died, remove him from your party and print:
# o	"{hero name} has been killed by {attacker}!"
# "Recharge – {hero name} – {amount}"
# •	The hero increases his MP. If it brings the MP of the hero above the maximum value (200), MP is increased to 200.
# (the MP can't go over the maximum value).
# •	 Print the following message:
# o	"{hero name} recharged for {amount recovered} MP!"
# "Heal – {hero name} – {amount}"
# •	The hero increases his HP. If a command is given that would bring the HP of the hero above the maximum value (100),
# HP is increased to 100 (the HP can't go over the maximum value).
# •	 Print the following message:
# o	"{hero name} healed for {amount recovered} HP!"

hero = int(input())
heroes = {}
for x in range(hero):
    name_hp_mana = input().split()
    name = name_hp_mana[0]
    hp = int(name_hp_mana[1])
    if hp > 100:
        hp = 100
    mana = int(name_hp_mana[2])
    if mana > 200:
        mana = 200
    if name not in heroes and hp > 0:
        heroes[name] = {"hp": hp, "mana": mana}
current_command = input()
while not current_command == 'End':
    command = current_command.split(" - ")
    action = command[0]
    hero = command[1]
    if action == "CastSpell":
        mana = int(command[2])
        spell = command[3]
        if hero in heroes:
            if heroes[hero]["mana"] >= mana:
                heroes[hero]["mana"] -= mana
                left = heroes[hero]["mana"]
                print(f"{hero} has successfully cast {spell} and now has {left} MP!")
            else:
                print(f"{hero} does not have enough MP to cast {spell}!")
    elif action == "TakeDamage":
        damage = int(command[2])
        attacker = command[3]
        if hero in heroes:
            if heroes[hero]["hp"] > damage:
                heroes[hero]["hp"] -= damage
                left = heroes[hero]["hp"]
                print(f"{hero} was hit for {damage} HP by {attacker} and now has {left} HP left!")
            else:
                del heroes[hero]
                print(f"{hero} has been killed by {attacker}!")
    elif action == "Recharge":
        amount = int(command[2])
        if hero in heroes:
            current = heroes[hero]["mana"]
            heroes[hero]["mana"] += amount
            if heroes[hero]["mana"] > 200:
                heroes[hero]["mana"] = 200
                print(f"{hero} recharged for {200 - current} MP!")
            else:
                print(f"{hero} recharged for {amount} MP!")
    elif action == "Heal":
        amount = int(command[2])
        if hero in heroes:
            current = heroes[hero]["hp"]
            heroes[hero]["hp"] += amount
            if heroes[hero]["hp"] > 100:
                heroes[hero]["hp"] = 100
                print(f"{hero} healed for {100 - current} HP!")
            else:
                print(f"{hero} healed for {amount} HP!")
    current_command = input()
for hero, stats in heroes.items():
    hp = stats["hp"]
    mana = stats["mana"]
    print(f"{hero}")
    print(f"  HP: {hp}")
    print(f"  MP: {mana}")
