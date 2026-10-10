import pandas as pd
import yfinance as yf

# Orijinal dosyanızı yükleyin
bakery_sales = pd.read_csv("bakery_sales_6.csv")

# Date kolonunu datetime formatına çevirin
bakery_sales['Date'] = pd.to_datetime(bakery_sales['Date'])

# Tarih aralığını belirle
start_date = bakery_sales['Date'].min().strftime('%Y-%m-%d')
end_date = bakery_sales['Date'].max().strftime('%Y-%m-%d')

# Brent ve WTI petrol verileri için Ticker
brent_oil_ticker = yf.Ticker("BZ=F")
wti_oil_ticker = yf.Ticker("CL=F")

# Tarihlere göre Brent ve WTI fiyatlarını çek
brent_data = brent_oil_ticker.history(start=start_date, end=end_date)['Close']
wti_data = wti_oil_ticker.history(start=start_date, end=end_date)['Close']

# Fiyat verilerini birleştirip ortalamasını alın (Brent ve WTI ortalaması)
oil_data = pd.DataFrame({
    'Brent_Price': brent_data,
    'WTI_Price': wti_data
})

# Zaman dilimini kaldırarak tz-naive hale getirin
oil_data.index = oil_data.index.tz_localize(None)

# Petrol fiyatlarının ortalamasını hesaplayın
oil_data['Avg_Oil_Price'] = oil_data.mean(axis=1)

# Tarihe göre petrol fiyatlarını eşleştirip yeni sütunu ekleyin
bakery_sales = bakery_sales.set_index('Date').join(oil_data[['Avg_Oil_Price']], how='left').reset_index()

# Yeni dosyayı kaydedin
bakery_sales.to_csv("bakery_sales_7.csv", index=False)
