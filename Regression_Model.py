import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.multioutput import MultiOutputRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder
import numpy as np

# Load the dataset
df = pd.read_csv('bakery_sales_dataset_4.0.csv')

# Convert 'Day' into numeric format (e.g., converting days of the week to numbers)
df['Day'] = pd.to_datetime(df['Day'], errors='coerce').dt.dayofweek

# Define the features (X) and the labels (y)
features = ['isHoliday', 'Avg_Oil_Price', 'tmin', 'tmax', 'tavg', 'wspd', 'pres']
labels = ['filter coffee', 'bread', 'croissant', 'angbutter', 'tea', 'cake', 'cookie', 'plain bread',
          'pastry', 'sandwich', 'hot chocolate', 'orange pound', 'latte', 'americano', 'cacao deep',
          'wiener', 'pandoro', 'brownie', 'jam', 'farm house bread', 'juice', 'muffin', 'scone', 'soup',
          'toast', 'scandinavian', 'gateau chocolat', 'truffles', 'coke', 'spanish brunch', 'fudge',
          'baguette bread', 'tiffin', 'milk tea', 'chicken stew', 'jammie dodgers', 'mineral water',
          'hearty & seasonal', 'cheesecake', 'salad', 'frittata', 'smoothies', 'the nomad', 'vegan mincepie',
          'berry ade', 'focaccia']

# Select the input features and output labels
X = df[features]
y = df[labels]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Linear Regression model wrapped in a MultiOutputRegressor
model = MultiOutputRegressor(LinearRegression())

# Train the model
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Optionally, you can predict for new data points like this:
# new_data = np.array([[Day, isHoliday, Avg_Oil_Price, tmin, tmax, tavg, wspd, pres]])
# prediction = model.predict(new_data)

# Example of new input data
new_data = np.array([[0, 44, 5, 10, 7.5, 15, 1012]])  # Example: Day=0 (Monday), Not a holiday, etc.

# Predict the sales for this new data
new_prediction = model.predict(new_data)

# Print the predicted sales for each bakery item
items = ['filter coffee', 'bread', 'croissant', 'angbutter', 'tea', 'cake', 'cookie', 'plain bread',
         'pastry', 'sandwich', 'hot chocolate', 'orange pound', 'latte', 'americano', 'cacao deep',
         'wiener', 'pandoro', 'brownie', 'jam', 'farm house bread', 'juice', 'muffin', 'scone', 'soup',
         'toast', 'scandinavian', 'gateau chocolat', 'truffles', 'coke', 'spanish brunch', 'fudge',
         'baguette bread', 'tiffin', 'milk tea', 'chicken stew', 'jammie dodgers', 'mineral water',
         'hearty & seasonal', 'cheesecake', 'salad', 'frittata', 'smoothies', 'the nomad', 'vegan mincepie',
         'berry ade', 'focaccia']

# Print each item and its predicted sales
for item, sales in zip(items, new_prediction[0]):
    print(f"{item}: {sales}")
