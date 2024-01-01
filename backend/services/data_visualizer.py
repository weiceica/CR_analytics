import pandas as pd
import matplotlib.pyplot as plt

# Load your data
data = pd.read_csv('backend/processed_data/Card_Data/Electro Giant_data.csv')
plt.style.use("ggplot")

data['Date'] = pd.to_datetime(data['Date'], format='%Y%m%d')

# Sort the DataFrame based on the date
df = data.sort_values(by='Date')

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Pick Rate'], marker='o')  # 'o' adds dots at each data point
plt.title('Pick Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Pick Rate')
plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability
plt.grid(True)
plt.show()