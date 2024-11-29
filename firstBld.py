import seaborn as sns
import matplotlib.pyplot as plt

# Set a color palette for the bars
custom_palette = ["salmon", "skyblue"]  # Colors for '0' (No First Blood) and '1' (First Blood)

# Ensure 'firstblood' is treated as categorical
data['firstblood'] = data['firstblood'].astype('category')

# First Blood Impact on Win
sns.barplot(data=data, x='firstblood', y='win', hue='firstblood', palette=custom_palette, dodge=False, errorbar=None)
plt.title("Impact of First Blood on Win")
plt.xlabel("First Blood (1 = Yes, 0 = No)")
plt.ylabel("Win Rate")
plt.legend([], [], frameon=False)  # Remove redundant legend
plt.show()
