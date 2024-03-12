# Assignment 1 --> Question 1

import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://www.imdb.com/chart/top/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}
response = requests.get(url, headers=headers)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
movies_data = []
movies_container = soup.find('ul', class_='ipc-metadata-list ipc-metadata-list--dividers-all sc-cvbbAY cVhFZB compact ipc-metadata-list--base')
if movies_container:
    movie_items = movies_container.find_all('li', class_='ipc-metadata-list-summary-item sc-10233bc-0 iherUv cli-parent')
    for movie in movie_items:
        title = movie.find('h3', class_='ipc-title__text').text if movie.find('h3', class_='ipc-title__text') else 'N/A'
        metadata_items = movie.find_all('span', class_='cli-title-metadata-item')
        if metadata_items:
            year = metadata_items[0].text if len(metadata_items) > 0 else 'N/A'
            duration = metadata_items[1].text if len(metadata_items) > 1 else 'N/A'
        else:
            year, duration = 'N/A', 'N/A'
        rating = movie.find('span', class_='ipc-rating-star--imdb').text.strip() if movie.find('span', class_='ipc-rating-star--imdb') else 'N/A'
        movies_data.append([title, year, duration, rating])
    df_movies = pd.DataFrame(movies_data, columns=['Title', 'Year', 'Duration', 'IMDB Rating'])
    df_movies.to_csv('imdb_top_250_movies_updated.csv', index=False)
    print("Scraping completed and saved to imdb_top_250_movies_updated.csv")
else:
    print("Movies container not found.")