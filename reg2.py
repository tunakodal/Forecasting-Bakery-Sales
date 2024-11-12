import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.multioutput import MultiOutputRegressor
from sklearn.metrics import mean_squared_error
from sklearn.neural_network import MLPRegressor

# Load the dataset
df = pd.read_csv('bakery_sales_dataset_4.5.csv')

# Encode the 'Day_Name' column (categorical variable)
label_encoder = LabelEncoder()
df['Day_Name_encoded'] = label_encoder.fit_transform(df['Day_Name'])

# Define the features and labels
features = ['Day_Name_encoded',  'isHoliday', 'tmax', 'tmin', 'tavg', 'wspd', 'pres',
            'Average Price', 'Brent Price', 'WTI Price']

# Multiple target variables (sales for different bakery items)
labels = ['filter coffee', 'bread', 'croissant', 'angbutter', 'tea', 'cake', 'cookie', 'plain bread',
          'pastry', 'sandwich', 'hot chocolate', 'orange pound', 'latte', 'americano', 'cacao deep',
          'wiener', 'pandoro', 'brownie', 'jam', 'farm house bread', 'juice', 'muffin', 'scone',
          'soup', 'toast', 'scandinavian', 'gateau chocolat', 'truffles', 'coke', 'spanish brunch', 'fudge',
          'baguette bread', 'tiffin', 'milk tea', 'chicken stew', 'jammie dodgers', 'mineral water',
          'hearty & seasonal', 'cheesecake', 'salad', 'frittata', 'smoothies', 'the nomad', 'vegan mincepie',
          'berry ade', 'focaccia']

# Prepare the feature matrix (X) and target matrix (y)
X = df[features]
y = df[labels]

# Split the data into training (80%), testing (10%), and validation (10%) sets
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.2, random_state=42)
X_valid, X_test, y_valid, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Apply StandardScaler to scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_valid_scaled = scaler.transform(X_valid)
X_test_scaled = scaler.transform(X_test)

# Create the MultiOutputRegressor with MLPRegressor (neural network model)
model = MultiOutputRegressor(MLPRegressor(hidden_layer_sizes=(100,), max_iter=5, random_state=42))

# Train the model with the scaled training data
model.fit(X_train_scaled, y_train)

# Make predictions on the scaled test and validation sets
y_test_pred = model.predict(X_test_scaled)
y_valid_pred = model.predict(X_valid_scaled)

# Calculate MSE for the test and validation sets
test_mse = mean_squared_error(y_test, y_test_pred)
valid_mse = mean_squared_error(y_valid, y_valid_pred)

# Output the MSE values
print(f"Mean Squared Error on the Test Set: {test_mse}")
print(f"Mean Squared Error on the Validation Set: {valid_mse}")

# Make a prediction for a given input (for example, using the first row from the test set)
example_input = X_test.iloc[0].values.reshape(1, -1)  # Take the first row of the test set as an example

# Scale the example input
example_input_scaled = scaler.transform(example_input)

# Convert to DataFrame with the correct feature names
example_input_df = pd.DataFrame(example_input_scaled, columns=features)

# Predict the sales for all items in the labels list
predicted_sales = model.predict(example_input_df)

# Output the predicted sales for all items
for i, item in enumerate(labels):
    print(f"Predicted sales of '{item}': {predicted_sales[0][i]}")

# Optionally, if you want to make a custom prediction for specific input values:
custom_input = [[1, 0, 18, 12, 15, 8, 1020, 73.45, 60.5, 70.2]]  # Replace with your custom input values

# Convert custom input to DataFrame
custom_input_df = pd.DataFrame(custom_input, columns=features)

# Scale the custom input
custom_input_scaled = scaler.transform(custom_input_df)

# Make prediction for custom input
custom_prediction = model.predict(custom_input_scaled)

# Output the predicted sales for all items based on custom input
for i, item in enumerate(labels):
    print(f"Predicted sales for '{item}' based on custom input: {custom_prediction[0][i]}")
