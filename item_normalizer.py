import pandas as pd
from sklearn.preprocessing import StandardScaler

# Dosyayı okuma
data = pd.read_csv("unique_items_ip.txt", sep=" ", header=None, names=["Product", "Count"])

# StandardScaler kullanarak sayıları normalize etme
scaler = StandardScaler()
data["Normalized_Count"] = scaler.fit_transform(data[["Count"]])

# Normalized datayi yeni dosyaya yazma
data[["Product", "Normalized_Count"]].to_csv("unique_items_normalized.txt", sep=" ", header=False, index=False)
