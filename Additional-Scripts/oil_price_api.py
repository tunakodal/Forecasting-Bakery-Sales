import requests

# API anahtarınızı buraya ekleyin
API_KEY = 'REMOVED'
BASE_URL = 'https://api.oilpriceapi.com/v1/prices'

# Sorgulamak istediğiniz tarih
date_to_check = '2023-11-06'

# Ülkeleri belirleyin
countries = ['Turkey', 'United Kingdom']  # Edinburgh Birleşik Krallık'ta yer aldığından

# API isteği gönderin
response = requests.get(
    BASE_URL,
    headers={'Authorization': f'Token {API_KEY}'},
    params={
        'country': countries,
        'date': date_to_check  # Belirli bir tarih
    }
)

# Yanıtı kontrol edin
if response.status_code == 200:
    data = response.json()
    print(f"Petrol fiyatları ({date_to_check}):")
    print(data)
else:
    print(f'Hata: {response.status_code} - {response.text}')
