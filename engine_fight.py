import random

def deal_damage(player, damage):
    if player["armor"] >= damage:
        player["armor"] -= damage
    elif player["armor"] < damage:
        dif = damage - player["armor"] 
        player["armor"] = 0
        if "🥼" in player["inventory"]:
            player["inventory"].remove("🥼")
            player["used inventory"].append("🥼")
        player["lives"] -= dif

def fight_boss(boss, player, cell):
    damage = 5

    if cell in "👾👹":
        boss["lives"] -= player["strength"]
        boss["attacks_in_cycle"] += 1

        if boss["condition"] == 1:
            boss["condition"] = 0
            deal_damage(player, damage)

        if boss["attacks_in_cycle"] == 2:
            boss["attacks_in_cycle"] = 0
            boss["condition"] = 1
        
        return boss, player
    

def fight_monsters(monsters, player, player_new_x, player_new_y):
    for monster in monsters:
        if [player["board"], player_new_y, player_new_x] == [monster["board"], monster["position y"], monster["position x"]] and monster["lives"] > 0:
            monster["lives"] -= player["strength"]
            damage = random.randint(monster["strength"][0], monster["strength"][1])
            deal_damage(player, damage)    
    return monsters, player
