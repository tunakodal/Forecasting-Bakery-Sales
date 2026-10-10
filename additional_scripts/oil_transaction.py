import pandas as pd

# Dosyayı yükleyin
bakery_sales = pd.read_csv('bakery_sales_8.csv')

# Avg_Oil_Price sütununda NaN olan satırları silin
bakery_sales = bakery_sales.dropna(subset=['Avg_Oil_Price'])

# TransactionNo değerlerinden 80 çıkarın
bakery_sales['TransactionNo'] = bakery_sales['TransactionNo'] - 80

# Güncellenmiş veriyi yeni bir dosyaya kaydedin
bakery_sales.to_csv('bakery_sales_9.csv', index=False)
