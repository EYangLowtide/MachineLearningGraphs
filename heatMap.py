import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define columns to keep
columns_to_keep = [
    'kills', 'deaths', 'assists', 'goldearned', 'goldspent', 'totminionskilled',
    'totdmgtochamp', 'firstblood', 'turretkills', 'visionscore', 'champlvl', 'totdmgtaken'
]

# Filter the dataset to include only the relevant columns
filtered_data = data[columns_to_keep]

# Calculate correlations
correlation = filtered_data.corr()

# Plot the heatmap
plt.figure(figsize=(10, 8))  # Adjust figure size for readability
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f", cbar=True)
plt.title("Simplified Feature Correlation Heatmap")
plt.show()
