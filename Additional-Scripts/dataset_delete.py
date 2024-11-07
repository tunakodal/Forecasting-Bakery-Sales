import pandas as pd

# Load the dataset
df = pd.read_csv('bakery_sales_dataset_3.1.csv')

# List of columns to remove
columns_to_remove = ['Day.1', 'isHoliday.1', 'Avg_Oil_Price.1', 'tmin.1', 'tmax.1', 'tavg.1', 'wspd.1', 'pres.1']

# Remove the specified columns
df = df.drop(columns=columns_to_remove, errors='ignore')  # errors='ignore' avoids errors if any columns are missing

# Save the updated dataframe back to a CSV file
df.to_csv('bakery_sales_dataset_3.1_cleaned.csv', index=False)
