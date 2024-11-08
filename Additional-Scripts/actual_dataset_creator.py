import pandas as pd

# Veriyi yükle
df = pd.read_csv("bakery_sales_cleaned_2.1.csv")

# İlgili item listesi
items = [
    "coffee", "bread", "croissant", "angbutter", "tea", "cake", "cookie",
    "plain bread", "pastry", "sandwich", "hot chocolate", "orange pound",
    "latte", "americano", "cacao deep", "wiener", "pandoro", "brownie",
    "jam", "farm house bread", "juice", "muffin", "scone", "soup", "toast",
    "scandinavian", "gateau chocolat", "truffles", "coke", "spanish brunch",
    "fudge", "baguette bread", "tiffin", "milk tea", "chicken stew",
    "jammie dodgers", "mineral water", "hearty & seasonal", "cheesecake",
    "salad", "frittata", "smoothies", "the nomad", "vegan mincepie",
    "berry ade", "focaccia"
]

# 'Items' kolonu ile 'Date' ve 'Place' kolonlarına göre sayımı yap
item_counts = pd.crosstab([df['Date'], df['Place']], df['Items']).reindex(columns=items, fill_value=0)

# Asıl veri ile birleştir ve istenmeyen kolonları sil
df = df.drop(columns=["Items"])
df = df.drop_duplicates(subset=['Date', 'Place']).merge(item_counts, on=['Date', 'Place'], how='left')

# Sonucu kaydet
df.to_csv("bakery_sales_dataset_4.0.csv", index=False)
