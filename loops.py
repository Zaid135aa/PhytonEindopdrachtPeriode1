monster_health = 150
player_damage = 25
attacks = 0

while monster_health > 0:
    monster_health = monster_health - player_damage
    monster_health = max(0, monster_health)

    attacks += 1

    print("Monster health:", monster_health)

print("Monster verslagen!")
print("Aantal aanvallen:", attacks)