import pandas as pd

# CSV dosyasını oku
df = pd.read_csv('bakery_sales_dataset_4.1.csv')

# Fonksiyon: Date kolonundaki her değeri kontrol et ve uygun şekilde dönüştür
def fix_date_format(date_value):
    try:
        # Eğer tarih zaten 'YY-MM-DD' formatında ise
        return pd.to_datetime(date_value, format='%Y-%m-%d').strftime('%Y-%m-%d')
    except:
        # Eğer tarih 'YY-DD-MM' formatında ise
        return pd.to_datetime(date_value, format='%Y-%d-%m').strftime('%Y-%m-%d')

# 'Date' kolonundaki tüm tarihleri düzelterek yeni formata çevir
df['Date'] = df['Date'].apply(fix_date_format)

# Yeni dosyayı kaydet
df.to_csv('bakery_sales_dataset_4.2.csv', index=False)
