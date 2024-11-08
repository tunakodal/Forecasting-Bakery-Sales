import yfinance as yf
import pandas as pd

# Tarih aralığı
start_date = '2016-01-01'
end_date = '2020-12-31'

# Brent ve WTI petrol fiyatları
brent = yf.Ticker('BZ=F')
wti = yf.Ticker('CL=F')

# Fiyat verilerini al
brent_data = brent.history(start=start_date, end=end_date)
wti_data = wti.history(start=start_date, end=end_date)

# Ortalama fiyat hesaplama (Brent ve WTI'nin ortalaması)
avg_price = (brent_data['Close'] + wti_data['Close']) / 2

# Verileri birleştirme
oil_prices = pd.DataFrame({
    'Date': brent_data.index,
    'Brent Price': brent_data['Close'],
    'WTI Price': wti_data['Close'],
    'Avg Price': avg_price
})

# Date kolonunu YY-MM-DD formatına dönüştürme
oil_prices['Date'] = oil_prices['Date'].dt.strftime('%y-%m-%d')

# Verileri CSV dosyasına yazma
oil_prices.to_csv('oil-price-dataset.csv', index=False)

print("Veriler başarıyla kaydedildi: oil-price-dataset.csv")
