# Forecasting Bakery Sales Model
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.multioutput import MultiOutputRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
import numpy as np
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('bakery_sales_dataset_4.5.csv')

label_encoder = LabelEncoder()
df['Day_Name_encoded'] = label_encoder.fit_transform(df['Day_Name'])

scaler = StandardScaler()
df['Day_Name_encoded'] = scaler.fit_transform(df[['Day_Name_encoded']])

features = ['Day_Name_encoded', 'isHoliday', 'tmax', 'tmin', 'tavg', 'wspd', 'pres', 'Average Price', 'Brent Price',
            'WTI Price']
labels = ['filter coffee', 'bread', 'croissant', 'angbutter', 'tea', 'cake', 'cookie', 'plain bread',
          'pastry', 'sandwich', 'hot chocolate', 'orange pound', 'latte', 'americano', 'cacao deep',
          'wiener', 'pandoro', 'brownie', 'jam', 'farm house bread', 'juice', 'muffin', 'scone', 'soup',
          'toast', 'scandinavian', 'gateau chocolat', 'truffles', 'coke', 'spanish brunch', 'fudge',
          'baguette bread', 'tiffin', 'milk tea', 'chicken stew', 'jammie dodgers', 'mineral water',
          'hearty & seasonal', 'cheesecake', 'salad', 'frittata', 'smoothies', 'the nomad', 'vegan mincepie',
          'berry ade', 'focaccia']

X = df[features]
y = df[labels]

X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.2, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

model = MultiOutputRegressor(LinearRegression())
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
rmse_percentage = (rmse / y_test.mean().mean()) * 100

mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100

adjusted_r2_values = []
f_values = []
p_values = []

for label in labels:
    X_train_sm = sm.add_constant(X_train)
    ols_model = sm.OLS(y_train[label], X_train_sm).fit()
    adjusted_r2_values.append(ols_model.rsquared_adj)
    f_values.append(ols_model.fvalue)
    p_values.append(ols_model.f_pvalue)


# Function to make predictions based on an array input
def predict_sales(input_array):
    """
    Predicts sales based on an input array.

    Parameters:
    - input_array: A list or 1D numpy array with values for [Day_Name_encoded, Year, Month, Day, isHoliday, tmax, tmin, tavg, wspd, pres, Average Price, Brent Price, WTI Price]

    Returns:
    - Dictionary with predicted sales for each product.
    """
    # Convert the input array to a DataFrame with the same column names as `X_train`
    input_df = pd.DataFrame([input_array], columns=features)

    # Make prediction
    prediction = model.predict(input_df)

    # Create a dictionary for readability
    prediction_dict = {labels[i]: prediction[0][i] for i in range(len(labels))}

    print("\nPredicted sales for each product:")
    for label, pred in prediction_dict.items():
        print(f"{label}: {pred:.2f}")

    return prediction_dict


# Example usage with input array
# [Day_Name_encoded, Year, Month, Day, isHoliday, tmax, tmin, tavg, wspd, pres, Average Price, Brent Price, WTI Price]
input_array = [2, 0, 15.2, 7.1, 11.1, 12.3, 1012, 85.0, 79.5, 80.3]
predicted_sales = predict_sales(input_array)
print(df[features].describe())
