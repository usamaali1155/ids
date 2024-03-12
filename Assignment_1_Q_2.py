# Assignment 1 --> Question 2

import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://space-facts.com/mars/'
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    mars_table = soup.find('table')    
    df_list = pd.read_html(str(mars_table))    
    mars_df = df_list[0]
    mars_df.columns = ['Description', 'Value']
    mars_df.set_index('Description', inplace=True)
    mars_df.to_excel('mars_planet_profile.xlsx', engine='openpyxl')
    print("Mars Planet Profile data has been saved to 'mars_planet_profile.xlsx'.")
else:
    print("Failed to fetch the webpage. Status code:", response.status_code)