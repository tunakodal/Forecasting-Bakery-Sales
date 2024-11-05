import pandas as pd
import yfinance as yf

# Brent ve WTI petrol verileri için Ticker
brent_oil_ticker = yf.Ticker("BZ=F")
wti_oil_ticker = yf.Ticker("CL=F")

# İlk tarih aralığı için Brent ve WTI fiyatlarını çek
brent_data_1 = brent_oil_ticker.history(start="2016-10-30", end="2017-09-04")['Close']
wti_data_1 = wti_oil_ticker.history(start="2016-10-30", end="2017-09-04")['Close']

# İkinci tarih aralığı için Brent ve WTI fiyatlarını çek
brent_data_2 = brent_oil_ticker.history(start="2019-08-12", end="2020-05-02")['Close']
wti_data_2 = wti_oil_ticker.history(start="2019-08-12", end="2020-05-02")['Close']

# Her iki tarih aralığını birleştir
brent_data = pd.concat([brent_data_1, brent_data_2])
wti_data = pd.concat([wti_data_1, wti_data_2])

# Fiyatları bir DataFrame olarak birleştir ve ortalama sütununu oluştur
oil_data = pd.DataFrame({
    'Brent_Price': brent_data,
    'WTI_Price': wti_data
})
oil_data['Avg_Oil_Price'] = oil_data.mean(axis=1)

# Dosyayı CSV formatında kaydet
oil_data.to_csv("oil_prices_doc.csv", index=True)
