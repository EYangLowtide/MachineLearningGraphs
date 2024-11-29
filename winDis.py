import seaborn as sns
import matplotlib.pyplot as plt

# Ensure 'win' is treated as a categorical variable
data['win'] = data['win'].astype('category')

# Set a color palette for the bars
custom_palette = ["skyblue", "salmon"]  # Colors for '0' (Loss) and '1' (Win)

# Win Distribution with hue
sns.countplot(data=data, x='win', hue='win', palette=custom_palette, dodge=False)
plt.title("Win Distribution")
plt.xlabel("Win (1 = Win, 0 = Loss)")
plt.ylabel("Count")
plt.legend([],[], frameon=False)  # Removes the legend since it's redundant
plt.show()
