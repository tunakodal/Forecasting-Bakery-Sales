import pandas as pd

# CSV dosyasını yükleme
df = pd.read_csv('bakery_sales_dataset_full_revised.csv')

# Silinmesi gereken öğeler listesi
items_to_remove = [
    "bakewell", "tartine", "extra salami or feta", "lemon ade", "granola", "eggs",
    "vegan feast", "duck egg", "dulce de leche", "pick and mix bowls", "tacos/fajita",
    "mighty protein", "chocolates", "christmas common", "kids biscuit", "gingerbread syrup",
    "argentina night", "empanadas", "muesli", "coffee granules", "pintxos",
    "drinking chocolate spoons", "half slice monster", "honey", "crepes", "panatone",
    "victorian sponge", "bread pudding", "brioche and salami", "lemon and coconut",
    "cherry me dried fruit", "raspberry shortbread sandwich", "spread", "bacon",
    "olum & polenta", "polenta", "the bart", "tiramisu"
]

# 'Items' sütununda istenmeyen ürünleri içeren satırları çıkarma
df = df[~df['Items'].isin(items_to_remove)]

# Silinmesi gereken kolonlar
columns_to_remove = ['Daypart', 'Time', 'Latitude', 'Longitude', 'Brent_Price', 'WTI_Price', 'TransactionNo']

# Belirtilen kolonları kaldırma
df = df.drop(columns=columns_to_remove)

# Güncellenmiş dosyayı kaydetme
df.to_csv('bakery_sales_cleaned_2.1.csv', index=False)

print("Belirtilen öğeler ve kolonlar kaldırıldı, dosya 'bakery_sales_cleaned_2.1.csv' olarak kaydedildi.")
