import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

tr = iter(soup.find_all('tr'))
next(tr)

for movie in tr:
    name = movie.find('td', {'class': 'titleColumn'}).find('a').string
    year = movie.find('td', {'class': 'titleColumn'}).find('span').string
    rating = movie.find('td', {'class', 'ratingColumn imdbRating'}).find('strong').string

    print(f'{name} - {year} ---> {rating}')
