import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('gif/data_cross.csv')

# Plot the data
sns.lineplot(data=df, x="epoch", y="fitness_estimate")

# Customize the plot
plt.xlabel("Generation")
plt.ylabel("Fittest Individual")
plt.title("Fittest Individual (Delta_E) vs. Generation")
plt.axhline(15, ls='--')  # Asymptote line
plt.ylim(0, 70)  # Include 0 in y-axis

# Show the plot
plt.show()