import pandas as pd
import re

# CSV formatındaki veriyi yükleyin
df = pd.read_csv('bakery_sales.csv')

# Items sütunundaki ürünleri küçük harfe çeviriyoruz
df['Items'] = df['Items'].str.lower()


# Benzer ürünleri birleştirme fonksiyonu
def normalize_item(item):
    # Kahve çeşitleri (americano, latte, espresso vb.)
    if re.search(r'coffee|americano|latte|espresso|cappuccino|mocha|macchiato|cacao deep|coffee granules', item):
        return 'coffee'

    # Latte çeşitleri (vanilla latte, caffe latte vb.)
    if re.search(r'latte', item):
        return 'latte'

    # Diğer ürünler için orijinal değeri döndür
    return item


# Her item'ı normalize ediyoruz
df['Items'] = df['Items'].apply(normalize_item)

# Aynı ürünleri sayarak birleştiriyoruz
item_counts = df['Items'].value_counts()

# Sonuçları yazdırıyoruz
print(item_counts)
print(len(item_counts))

# Eğer istersen, normalize edilmiş veriyi yeni bir CSV dosyasına kaydedebiliriz
df.to_csv('bakery_sales_normalized.csv', index=False)
