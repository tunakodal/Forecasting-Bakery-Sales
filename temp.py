import pandas as pd

# İlk dosyayı yükle
df = pd.read_csv("bakery_sales_dataset_4.4.csv")

# İstediğiniz kolonları belirtin
columns_to_add = [
    'tmin', 'tmax', 'tavg', 'wspd', 'pres', 'filter coffee', 'bread', 'croissant',
    'angbutter', 'tea', 'cake', 'cookie', 'plain bread', 'pastry', 'sandwich',
    'hot chocolate', 'orange pound', 'latte', 'americano', 'cacao deep', 'wiener',
    'pandoro', 'brownie', 'jam', 'farm house bread', 'juice', 'muffin', 'scone',
    'soup', 'toast', 'scandinavian', 'gateau chocolat', 'truffles', 'coke',
    'spanish brunch', 'fudge', 'baguette bread', 'tiffin', 'milk tea', 'chicken stew',
    'jammie dodgers', 'mineral water', 'hearty & seasonal', 'cheesecake', 'salad',
    'frittata', 'smoothies', 'the nomad', 'vegan mincepie', 'berry ade', 'focaccia'
]

# Sadece bu kolonları al
columns_from_df = df[columns_to_add]

# İkinci dosyayı (modifiye edilmiş) yükle
df_modified = pd.read_csv("bakery_sales_dataset_4.4_modified.csv")

# Yeni kolonları df_modified'in sonuna ekle
df_modified = pd.concat([df_modified, columns_from_df], axis=1)

# Yeni dosyayı kaydet
df_modified.to_csv("bakery_sales_dataset_4.5.csv", index=False)

print("Yeni kolonlar başarıyla eklendi ve kaydedildi.")
