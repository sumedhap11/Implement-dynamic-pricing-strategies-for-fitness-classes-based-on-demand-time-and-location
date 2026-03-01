import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data, parsing dates and setting the date column as the index
# Replace 'your_data.csv' with your actual data file
df = pd.read_csv('C:/fitness_classes_project/Classes April-May 2018.csv', parse_dates=['Date'], index_col='Date')

# Plot the time series
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Value']) # 'Value' is the name of the column you want to plot
plt.title('Time Series Plot of Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()
