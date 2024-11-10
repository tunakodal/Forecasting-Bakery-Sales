import pandas as pd

# Datasetinizi yükleyin
df = pd.read_csv('combined_price_dataset_normalized.csv')

# Date kolonunu YY-mm-dd formatına çevirin
df['Date'] = '20' + df['Date'].astype(str)

# Güncellenmiş dosyayı kaydedin
df.to_csv('combined_price_dataset_normalized.csv', index=False)
