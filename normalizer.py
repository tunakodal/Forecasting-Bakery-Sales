import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# CSV dosyasını yükleme
df = pd.read_csv("bakery_sales_dataset_4.2.csv")

# Normalizasyon yapılacak sayısal sütunları seçme (Day, Place, Date hariç)
columns_to_normalize = df.drop(columns=["Day", "Place", "Date"])

# Min-Max Scaler ile normalizasyon
scaler = MinMaxScaler()
df[columns_to_normalize.columns] = scaler.fit_transform(columns_to_normalize)

# Sonuçları yeni bir CSV dosyasına kaydetme
df.to_csv("bakery_sales_dataset_normalized.csv", index=False)
