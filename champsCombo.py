import matplotlib.pyplot as plt
import pandas as pd

# Combine champion pairs to remove duplicates (e.g., treat (A, B) and (B, A) as the same)
pair_counts_df['Champion Pair'] = pair_counts_df['Champion Pair'].apply(lambda pair: tuple(sorted(pair)))
unique_pairs = pair_counts_df.groupby('Champion Pair')['Count'].sum().reset_index()
unique_pairs = unique_pairs.sort_values(by='Count', ascending=False).head(10)

# Plot the data with color-coding
colors = plt.cm.viridis(range(len(unique_pairs)))  # Generate distinct colors for each bar

plt.figure(figsize=(10, 6))
plt.barh(
    [f"{pair[0]} & {pair[1]}" for pair in unique_pairs['Champion Pair']],
    unique_pairs['Count'],
    color=colors
)
plt.xlabel('Number of Matches')
plt.ylabel('Champion Pair')
plt.title('Top 10 Most Frequent Champion Pairs (Unique)')
plt.gca().invert_yaxis()  # Invert the y-axis for better readability
plt.show()
