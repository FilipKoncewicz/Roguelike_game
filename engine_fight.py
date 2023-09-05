def fight_boss(boss, player, cell):
    if cell in "👾👹":
        boss["lives"] -= player["strength"]
        boss["attacks_in_cycle"] += 1

        if boss["condition"] == 1:
            player["lives"] -= 5
            boss["condition"] = 0
        
        if boss["attacks_in_cycle"] == 2:
            boss["attacks_in_cycle"] = 0
            boss["condition"] = 1
        
        return boss, player