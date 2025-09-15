import requests
import pandas as pd

def film_api(api_key=None):
    if not api_key:
        api_key = input("Lütfen API anahtarınızı giriniz: ")
        
    url = "https://imdb-top-100-movies.p.rapidapi.com/"
    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "imdb-top-100-movies.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        movies_data = response.json()
        if movies_data:
            df = pd.DataFrame(movies_data)
            csv_file_name = 'top_100_Movie.csv'
            df.to_csv(csv_file_name, index=False, encoding='utf-8')
            print(f"Veriler başarıyla '{csv_file_name}' dosyasına kaydedildi!")
        else:
            print("API'den herhangi bir veri alınamadı.")
    except requests.exceptions.RequestException as e:
        print(f"Bir hata oluştu: {e}")
film_api()
