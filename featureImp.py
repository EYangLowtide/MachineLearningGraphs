import pandas as pd
import matplotlib.pyplot as plt

# Example feature importance (replace with actual values from your model)
feature_importances = {
    'totdmgtochamp': 0.35,
    'turretkills': 0.25,
    'goldearned': 0.20,
    'kills': 0.10,
    'assists': 0.10
}

# Convert to DataFrame for easier plotting
feature_importance_df = pd.DataFrame(
    list(feature_importances.items()),
    columns=['Feature', 'Importance']
).sort_values(by='Importance', ascending=False)

# Create the bar chart
plt.figure(figsize=(8, 5))
plt.barh(feature_importance_df['Feature'], feature_importance_df['Importance'], color='skyblue')
plt.title("Feature Importance (Random Forest/XGBoost)")
plt.xlabel("Importance Score")
plt.ylabel("Features")
plt.gca().invert_yaxis()  # Invert y-axis for descending order
plt.show()
