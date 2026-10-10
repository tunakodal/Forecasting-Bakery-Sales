import yfinance as yf
import pandas as pd

# Tarih aralığı
start_date = '2006-01-01'
end_date = '2024-07-30'

# Brent fiyatlarını al
brent = yf.Ticker('BZ=F')
brent_data = brent.history(start=start_date, end=end_date)

# Tarih formatını YY-MM-DD olarak ayarla
brent_data.index = brent_data.index.strftime('%y-%m-%d')
brent_data = brent_data[['Close']]
brent_data.columns = ['Brent Price']

# CSV dosyasına yazma
brent_data.to_csv('brent-price-dataset.csv', index_label='Date')

print("Brent fiyatları başarıyla kaydedildi: brent-price-dataset.csv")
