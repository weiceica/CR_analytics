import pandas as pd
import os
import csv

P1CROWNS = 4
P1CARD1 = 5
P1CARD8 = 12
P2CROWNS = 15
P2CARD1 = 16
P2CARD8 = 23

def process_card(target_card: str) -> pd.DataFrame:
    aggregate_data = []

    # Loop through each CSV file
    for directory in os.listdir('backend/raw_data'):
        if os.path.isdir(f'backend/raw_data/{directory}'):
            for file in os.listdir(f'backend/raw_data/{directory}'):
                if file.endswith('.csv'):
                    total_wins = 0
                    total_losses = 0
                    total_games = 0
                    total_crowns_taken = 0
                    total_crowns_lost = 0
                    games_played = 0
                    total_picked = 0

                    with open(f'backend/raw_data/{directory}/{file}', mode='r', encoding='utf-8') as csvfile:
                        reader = csv.reader(csvfile)

                        for row in reader:
                            games_played += 1
                            if target_card in row:
                                total_games += 1
                                if target_card in row[P1CARD1: P1CARD8 + 1]:
                                    total_picked += 1
                                    total_crowns_taken += 3 - int(row[P2CROWNS])
                                    total_crowns_lost += 3 - int(row[P1CROWNS])
                                    if row[P1CROWNS] > row[P2CROWNS]:
                                        total_wins += 1
                                    else:
                                        total_losses += 1
                                if target_card in row[P2CARD1: P2CARD8 + 1]:
                                    total_picked += 1
                                    total_crowns_taken += 3 - int(row[P1CROWNS])
                                    total_crowns_lost += 3 - int(row[P2CROWNS])
                                    if row[P2CROWNS] > row[P1CROWNS]:
                                        total_wins += 1
                                    else:
                                        total_losses += 1

                    # Calculate aggregate stats
                    win_rate = total_wins / total_games if total_games > 0 else 0
                    avg_crowns_taken = total_crowns_taken / total_games if total_games > 0 else 0
                    avg_crowns_lost = total_crowns_lost / total_games if total_games > 0 else 0
                    pick_rate = total_picked / (games_played * 2)if games_played > 0 else 0

                    # Append day's stats to aggregate data
                    date = file.replace('.csv', '')
                    aggregate_data.append([date, total_wins, total_losses, total_games, win_rate, pick_rate, avg_crowns_taken, avg_crowns_lost])
                    # Add additional stats to append if needed

    # Convert to DataFrame and save to CSV
    df = pd.DataFrame(aggregate_data, columns=['Date', 'Total Wins', 'Total Losses', 'Total Games', 'Win Rate', 'Pick Rate', 'Average Crowns Taken', 'Average Crowns Lost'])