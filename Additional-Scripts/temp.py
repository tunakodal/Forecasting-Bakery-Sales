import pandas as pd

# Load the dataset
df = pd.read_csv('bakery_sales_dataset_3.1.csv')

# Check for the 'filter' column and make sure it exists in the dataframe
columns_to_move = ['Day', 'isHoliday', 'Avg_Oil_Price', 'tmin', 'tmax', 'tavg', 'wspd', 'pres']
other_columns = [col for col in df.columns if col not in columns_to_move]

# Check if 'filter' exists
if 'filter' in other_columns:
    # If 'filter' exists, reorder the columns accordingly
    new_order = ['Date'] + columns_to_move + ['filter'] + [col for col in other_columns if col != 'filter']
else:
    # If 'filter' doesn't exist, reorder without it
    new_order = ['Date'] + columns_to_move + other_columns

# Reorder the columns
df = df[new_order]

# Save the updated dataframe back to a CSV file
df.to_csv('bakery_sales_dataset_3.1_reordered.csv', index=False)
