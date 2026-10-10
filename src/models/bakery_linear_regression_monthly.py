#Forecasting Bakery Sales Model for Months
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.multioutput import MultiOutputRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
import numpy as np
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler
import tensorflow as tf

df = pd.read_csv('data/raw/bakery_sales.csv')

df.drop(columns=['Day'])

avg_columns = ['isHoliday', 'Brent Price', 'Average Price', 'WTI Price', 'tmax', 'tmin', 'tavg', 'wspd', 'pres']
sum_columns = ['filter coffee', 'bread', 'croissant', 'angbutter', 'tea', 'cake', 'cookie', 'plain bread',
              'pastry', 'sandwich', 'hot chocolate', 'orange pound', 'latte', 'americano', 'cacao deep',
              'wiener', 'pandoro', 'brownie', 'jam', 'farm house bread', 'juice', 'muffin', 'scone', 'soup',
              'toast', 'scandinavian', 'gateau chocolat', 'truffles', 'coke', 'spanish brunch', 'fudge',
              'baguette bread', 'tiffin', 'milk tea', 'chicken stew', 'jammie dodgers', 'mineral water',
              'hearty & seasonal', 'cheesecake', 'salad', 'frittata', 'smoothies', 'the nomad', 'vegan mincepie',
              'berry ade', 'focaccia']


df = df.groupby(['Year', 'Month']).agg({**{col: 'mean' for col in avg_columns},
                                            **{col: 'sum' for col in sum_columns}}).reset_index()

features = ['Month', 'isHoliday', 'tmax', 'tmin', 'tavg', 'wspd', 'pres', 'Average Price', 'Brent Price', 'WTI Price' ]
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
model.fit(X_train, y_train )

y_pred = model.predict(X_test)

rmse = []
for label in labels:
    rmse.append(np.sqrt(mean_squared_error(y_test[label], y_pred[:, labels.index(label)])))

rmse_percentage = []
for i in range(len(labels)):
    rmse_percentage.append((rmse[i] / y_test[labels[i]].mean()) * 100)

mape_values = []
for i, label in enumerate(labels):
    y_test_label = y_test[label]
    non_zero_indices = y_test_label != 0
    mape_label = np.mean(np.abs((y_test_label[non_zero_indices] - y_pred[non_zero_indices, i]) / y_test_label[non_zero_indices])) * 100
    mape_values.append(mape_label)

adjusted_r2_values = []
f_values = []
p_values = []

for label in labels:
    X_train_sm = sm.add_constant(X_train)
    ols_model = sm.OLS(y_train[label], X_train_sm).fit()
    adjusted_r2_values.append(ols_model.rsquared_adj)
    f_values.append(ols_model.fvalue)
    p_values.append(ols_model.f_pvalue)



print("\nAdjusted R², F-value, and p-value for each product:")
for i, label in enumerate(labels):
    print(f"{label}:")
    print(f"  Adjusted R²: {adjusted_r2_values[i]:.4f}")
    print(f"  F-value: {f_values[i]:.4f}")
    print(f"  P-value: {p_values[i]:.4f}")
    print(f"  RMSE: {rmse[i]:.4f}")
    print(f"  RMSE Percentage: {rmse_percentage[i]:.2f}%")
    print(f"  MAPE: {mape_values[i]:.2f}%")
    print()