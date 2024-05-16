def potion(selected_potion_name, selected_user_monster, login_id, potion_inventory,monster_data):
    for potion in potion_inventory:
        if potion['user_id'] == login_id and potion['type'] == selected_potion_name:
            if int(potion['quantity']) > 0:
                if selected_potion_name.lower() == 'strength':
                    selected_user_monster['atk_power'] = str(int(int(selected_user_monster['atk_power']) * 1.05))
                    potion['quantity'] = str(int(potion['quantity']) - 1)
                elif selected_potion_name.lower() == 'resilience':
                    selected_user_monster['def_power'] = str(int(int(selected_user_monster['def_power']) * 1.05))
                    potion['quantity'] = str(int(potion['quantity']) - 1)
                elif selected_potion_name.lower() == 'healing':
                    level = int(selected_user_monster['level'])
                    factor = 1 + (int(level) - 1) * 0.1
                    monster = [m for m in monster_data if selected_user_monster['type'] == m['type']][0]
                    selected_user_monster['hp'] = str(int(int(selected_user_monster['hp']) * 1.25))
                    potion['quantity'] = str(int(potion['quantity']) - 1)
            else:
                print("Potion habis")
    return selected_user_monster, potion_inventory