import yfinance as yf

# Brent petrolü için Ticker
brent_oil_ticker = yf.Ticker("BZ=F")
# WTI petrolü için Ticker
wti_oil_ticker = yf.Ticker("CL=F")

# Brent ve WTI petrolü için tarih aralığında verileri çek
brent_data = brent_oil_ticker.history(start="2016-10-16", end="2023-10-17")
wti_data = wti_oil_ticker.history(start="2016-10-16", end="2023-10-17")

# Sonuçları yazdır
print("Brent Petrol Fiyatları:")
print(brent_data)
print("\nWTI Petrol Fiyatları:")
print(wti_data)
