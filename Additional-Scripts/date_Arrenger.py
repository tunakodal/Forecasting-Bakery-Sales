import pandas as pd
from pandas._libs import OutOfBoundsDatetime

# Dosyayı yükleyin
bakery_sales = pd.read_csv('bakery_sales_6.csv')

# 'Date' sütununu datetime formatına çevirin
bakery_sales['Date'] = pd.to_datetime(bakery_sales['Date'])

# Belirli tarih aralığını filtreleyin
mask = (bakery_sales['Date'] >= '2016-01-11') & (bakery_sales['Date'] <= '2016-12-11')


# Gün ve ay değerlerini değiştirin, geçerli tarih olup olmadığını kontrol edin
def swap_day_month(date):
    day = date.day
    month = date.month
    year = date.year

    # Yeni tarih oluştur
    try:
        new_date = pd.Timestamp(year, day, month)
        return new_date
    except (ValueError, OutOfBoundsDatetime):
        return date  # Geçersiz tarih durumunda orijinal tarihi döndür


bakery_sales.loc[mask, 'Date'] = bakery_sales.loc[mask, 'Date'].apply(swap_day_month)

# Güncellenmiş veriyi yeni bir dosyaya kaydedin
bakery_sales.to_csv('bakery_sales_7.csv', index=False)
