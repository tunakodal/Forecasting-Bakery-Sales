import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.multioutput import MultiOutputRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
import numpy as np
import statsmodels.api as sm

# Load the dataset
df = pd.read_csv('bakery_sales_dataset_4.5.csv')

# Define the features and labels
features = ['Day_Name', 'Year', 'Month', 'Day', 'isHoliday', 'tmax', 'tmin', 'tavg', 'wspd', 'pres', 'Average Price',
            'Brent Price', 'WTI Price']
labels = ['filter coffee', 'bread', 'croissant', 'angbutter', 'tea', 'cake', 'cookie', 'plain bread',
          'pastry', 'sandwich', 'hot chocolate', 'orange pound', 'latte', 'americano', 'cacao deep',
          'wiener', 'pandoro', 'brownie', 'jam', 'farm house bread', 'juice', 'muffin', 'scone', 'soup',
          'toast', 'scandinavian', 'gateau chocolat', 'truffles', 'coke', 'spanish brunch', 'fudge',
          'baguette bread', 'tiffin', 'milk tea', 'chicken stew', 'jammie dodgers', 'mineral water',
          'hearty & seasonal', 'cheesecake', 'salad', 'frittata', 'smoothies', 'the nomad', 'vegan mincepie',
          'berry ade', 'focaccia']

# Prepare the data
X = df[features].copy()
y = df[labels]

# Encode categorical column 'Day_Name'
label_encoder = LabelEncoder()
X.loc[:, 'Day_Name_encoded'] = label_encoder.fit_transform(X['Day_Name'])
X = X.drop(columns=['Day_Name'])

# Split the data into training, validation, and test sets
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.2, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Initialize the MultiOutputRegressor with LinearRegression
model = MultiOutputRegressor(LinearRegression())

# Track metrics over epochs
epochs = 50
rmse_values = []
mape_values = []
adjusted_r2_values = []
f_values = []
p_values = []

# Training the model for 50 epochs (simulated)
for epoch in range(epochs):
    model.fit(X_train, y_train)  # Fit the model

    # Predictions
    y_pred = model.predict(X_test)

    # RMSE
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    rmse_percentage = (rmse / y_test.mean()) * 100
    rmse_values.append(rmse_percentage)

    # MAPE
    mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100
    mape_values.append(mape)

    # Calculate Adjusted R², F-value, and P-value for each label
    for label in labels:
        X_train_sm = sm.add_constant(X_train)
        ols_model = sm.OLS(y_train[label], X_train_sm).fit()
        adjusted_r2_values.append(ols_model.rsquared_adj)
        f_values.append(ols_model.fvalue)
        p_values.append(ols_model.f_pvalue)

# Print the final metrics after 50 epochs
print("\nMetrics after 50 epochs:")
for i, label in enumerate(labels):
    print(f"{label}:")
    print(f"  RMSE%: {rmse_values.iloc[-1]:.2f}%")
    print(f"  MAPE: {mape_values[-1]:.2f}%")
    print(f"  Adjusted R²: {adjusted_r2_values[-1]:.4f}")
    print(f"  F-value: {f_values[-1]:.4f}")
    print(f"  P-value: {p_values[-1]:.4f}")

# Predict for new values (replace these with actual data)
new_data = {
    'Day_Name_encoded': label_encoder.transform(['Monday']),  # example day
    'Year': [2020],
    'Month': [11],
    'Day': [11],
    'isHoliday': [0],  # example for not a holiday
    'tmax': [15],
    'tmin': [5],
    'tavg': [10],
    'wspd': [3],
    'pres': [1012],
    'Average Price': [2.5],
    'Brent Price': [75],
    'WTI Price': [70]
}

new_df = pd.DataFrame(new_data)
new_pred = model.predict(new_df)

# Print predictions for the new data
print("\nPredictions for new input:")
for i, label in enumerate(labels):
    print(f"{label}: {new_pred[0][i]:.2f}")
