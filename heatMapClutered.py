import seaborn as sns
import matplotlib.pyplot as plt

# Calculate correlations
correlation = data.corr()

# Plot: Correlation Heatmap
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.show()
