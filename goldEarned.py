import seaborn as sns
import matplotlib.pyplot as plt

# Gold Earned Distribution by Win
sns.boxplot(x='win', y='goldearned', data=data)
plt.title("Gold Earned Distribution by Win")
plt.xlabel("Win (1 = Win, 0 = Loss)")
plt.ylabel("Gold Earned")
plt.show()
