import pandas as pd
import numpy as np
import os

# Helper function for writing
def create_sample(file_path, output_name, sample_size):
    # Load the data
    data = pd.read_csv(file_path)

    # Defining Column Names
    new_column_names = ['Time', 'Gamemode', 'P1Tag', 'P1Trophies', 'P1Crowns', 'P1Card1', 'P1Card2', 'P1Card3', 'P1Card4', 'P1Card5', 'P1Card6', 'P1Card7', 'P1Card8', 'P2Tag', 'P2Trophies', 'P2Crowns', 'P2Card1', 'P2Card2', 'P2Card3', 'P2Card4', 'P2Card5', 'P2Card6', 'P2Card7', 'P2Card8']

    # Assign new column names
    data.columns = new_column_names

    # Check if the file has at least sample_size rows
    if len(data) >= sample_size:
        sample = data.sample(n=sample_size, random_state=np.random.RandomState())
        sample.to_csv(output_name, index=False)
    else:
        print(f"The file only has {len(data)} rows, less than {sample_size}.")
        sample = data.sample(n=len(data), random_state=np.random.RandomState())
        sample.to_csv(output_name, index=False)

    print(f"Sampled data written to {output_name}")