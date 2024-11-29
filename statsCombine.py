import os
import pandas as pd

# Folder containing the files
folder_path = "C:/Users/elgol/Documents/school work/Machinelearning/archiveLeagueofLegends-20241128T223101Z-001/archiveLeagueofLegends"

# Load primary datasets
stats1_path = os.path.join(folder_path, "stats1.csv")
stats2_path = os.path.join(folder_path, "stats2.csv")

# Load match data
stats1 = pd.read_csv(stats1_path, low_memory=False)
stats2 = pd.read_csv(stats2_path, low_memory=False)

# Combine stats1 and stats2
combined_stats = pd.concat([stats1, stats2], ignore_index=True)

# Load auxiliary datasets
champs_path = os.path.join(folder_path, "champs.csv")
champs = pd.read_csv(champs_path)

# Example: Merge champion data into combined_stats
if 'championId' in combined_stats.columns and 'championId' in champs.columns:
    combined_stats = combined_stats.merge(champs, on='championId', how='left')

# Check the combined data
print(combined_stats.head())

# Save the combined stats for later use
combined_stats_path = os.path.join(folder_path, "combined_stats.csv")
combined_stats.to_csv(combined_stats_path, index=False)
print(f"Combined stats saved to {combined_stats_path}")
