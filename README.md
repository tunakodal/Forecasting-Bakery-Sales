# Forecasting Bakery Sales

YAP470 course project (Fall 2024) by Ebrar Sude Doğan and Tuna Kodal.

Forecasts bakery sales with multi-output linear regression, using weather and oil price data as supporting features (forecasted separately with LSTM and GRU models).

## Structure

```
.
├── data/
│   ├── raw/              # bakery sales, oil price, weather, Edinburgh weather
│   ├── processed/        # monthly-merged sales, unique item list
│   └── normalized/       # normalized datasets used by the LSTM/GRU models
├── src/
│   ├── models/           # bakery regression (daily, monthly), oil price GRU, weather LSTM
│   └── preprocessing/    # normalization script
├── additional_scripts/   # dataset creation, API fetching, ARIMA/SARIMA and other experiments
├── reports/              # final report (PDF) and interim report (notebooks)
└── docs/                 # references
```

## Usage

Run scripts from the repository root, e.g.:

```bash
python src/models/bakery_linear_regression_daily.py
```
