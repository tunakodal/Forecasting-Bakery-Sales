import yfinance as yf
import pandas as pd

# Tarih aralığı
start_date = '1990-01-01'
end_date = '2024-07-30'

# WTI fiyatlarını al
wti = yf.Ticker('CL=F')
wti_data = wti.history(start=start_date, end=end_date)

# Tarih formatını YY-MM-DD olarak ayarla
wti_data.index = wti_data.index.strftime('%y-%m-%d')
wti_data = wti_data[['Close']]
wti_data.columns = ['WTI Price']

# CSV dosyasına yazma
wti_data.to_csv('wti-price-dataset.csv', index_label='Date')

print("WTI fiyatları başarıyla kaydedildi: wti-price-dataset.csv")
