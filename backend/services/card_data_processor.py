# Create a dataset that contains information about one card

import pandas as pd
import json
from utils.processor import process_card

win_conditions = ["26000056", "27000002", "26000024", "26000067", "26000036", "26000021", "26000003", "26000059", "26000028", "26000058", "28000004", "27000013", "26000006", "26000060", "27000008", "26000085", "26000009", "26000032", "26000051", "28000010", "26000029"]
win_conditions_names = ['Skeleton Barrel', 'Mortar', 'Royal Giant', 'Elixir Golem', 'Battle Ram', 'Hog Rider', 'Giant', 'Royal Hogs', 'Three Musketeers', 'Wall Breakers', 'Goblin Barrel', 'Goblin Drill', 'Balloon', 'Goblin Giant', 'X-Bow', 'Electro Giant', 'Golem', 'Miner', 'Ram Rider', 'Graveyard', 'Lava Hound']

for index, target_card in enumerate(win_conditions):
    print(f"{win_conditions_names[index]} is being processed.") 
    df = process_card(target_card)
    df.to_csv(f'backend/processed_data/{win_conditions_names[index]}_data.csv', index=False)
    print(f"{win_conditions_names[index]} has been processed.") 