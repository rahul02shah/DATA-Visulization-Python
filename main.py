import matplotlib.pyplot as plt
import pandas as pd
data = {
    'Date': ['2023-01-01', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-07', '2023-01-08', '2023-01-09'],
    'Wi-Fi Usage (GB)': [15.2, 4.3, 12.8, 9.7, 14.5, 8.9, 4.1],
    'Lab Access Count': [10, 5, 12, 7, 9, 8, 6],
    'Online Platform Access (Hours)': [2.5, 1.0, 2.2, 1.5, 2.4, 1.7, 1.1]
}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(10, 8))
df['Wi-Fi Usage (GB)'].plot(ax=axes[0], marker='o')
axes[0].set_ylabel('Wi-Fi Usage (GB)')
axes[0].set_title('Wi-Fi Usage Over Time')
df['Lab Access Count'].plot(ax=axes[1], marker='o', color='green')
axes[1].set_ylabel('Lab Access Count')
axes[1].set_title('Lab Access Count Over Time')
df['Online Platform Access (Hours)'].plot(ax=axes[2], marker='o', color='orange')
axes[2].set_ylabel('Online Platform Access (Hours)')
axes[2].set_title('Online Platform Access Over Time')
plt.tight_layout()
plt.show()
