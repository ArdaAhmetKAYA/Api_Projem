import requests
import pandas as pd

def dizi_api(api_key=None):
    if not api_key:
        api_key = input("Lütfen API anahtarınızı giriniz: ")

    url = "https://imdb-top-100-movies.p.rapidapi.com/series/"
    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "imdb-top-100-movies.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        series_data = response.json()
        if series_data:
            df = pd.DataFrame(series_data)
            csv_file_name = 'top_100_Series.csv'
            df.to_csv(csv_file_name, index=False, encoding='utf-8')
            print(f"veriler başarıyla '{csv_file_name}' dosyasına kaydedildi!")
        else:
            print("API'den herhangi bir veri alınamadı.")
    except requests.exceptions.RequestException as e:
        print(f"Bir hata oluştu: {e}")
dizi_api()