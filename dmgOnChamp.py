import seaborn as sns
import matplotlib.pyplot as plt

# Total Damage to Champions by Win
sns.boxplot(x='win', y='totdmgtochamp', data=data)
plt.title("Total Damage to Champions vs Win")
plt.xlabel("Win (1 = Win, 0 = Loss)")
plt.ylabel("Total Damage to Champions")
plt.show()
