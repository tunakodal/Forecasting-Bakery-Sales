import pandas as pd

# Load the dataset
file_path = 'bakery_sales_dataset_3.1_cleaned.csv'
df = pd.read_csv(file_path)

# Find rows containing NaN values
nan_rows = df[df.isna().any(axis=1)]

# Get the row numbers (index) of rows containing NaN values
nan_row_numbers = nan_rows.index.tolist()

# Print the row numbers with NaN values
print("Rows with NaN values:", nan_row_numbers)
