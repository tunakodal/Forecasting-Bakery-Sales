import pandas as pd

# Dosyayı yükleyin
bakery_sales = pd.read_csv('bakery_sales_7.csv')

# 'TransactionNo' sütunundaki her bir sayıdan 80 çıkarın
bakery_sales['TransactionNo'] = bakery_sales['TransactionNo'] - 80

# Güncellenmiş veriyi yeni bir dosyaya kaydedin
bakery_sales.to_csv('bakery_sales_8.csv', index=False)
