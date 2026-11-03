player_class = "Warrior"

health = 0
damage = 0

match player_class:
    case "Warrior":
        health = 150
        damage = 20

    case "Mage":
        health = 80
        damage = 35

    case "Archer":
        health = 100
        damage = 25

    case "Rogue":
        health = 90
        damage = 30

    case _:
        print("Onbekende class!")

if player_class in ["Warrior", "Mage", "Archer", "Rogue"]:
    print("Gekozen class:", player_class)
    print("Health:", health)
    print("Damage:", damage)