import seaborn as sns
import matplotlib.pyplot as plt

# Champion Level Distribution by Win
sns.boxplot(x='win', y='champlvl', data=data)
plt.title("Champion Level Distribution by Win")
plt.xlabel("Win (1 = Win, 0 = Loss)")
plt.ylabel("Champion Level")
plt.show()
