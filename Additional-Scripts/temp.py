import pandas as pd

# CSV dosyasını yükleme
df = pd.read_csv('bakery_sales_dataset_full_revised.csv')

# Her bir ürünün kaç kez tekrarlandığını hesaplama
item_counts = df['Items'].value_counts().dropna()

# Sonuçları bir .txt dosyasına yazma
with open('unique_items_with_counts.txt', 'w') as file:
    for item, count in item_counts.items():
        file.write(f"{item}: {count}\n")

print("Benzersiz ürünler ve tekrar sayıları 'unique_items_with_counts.txt' dosyasına kaydedildi.")
