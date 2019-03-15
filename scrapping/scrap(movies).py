"""
@author : CK =>ckrajadurai7@gmail.com
@github : https://github.com/ck2605
@date : 13/03/2019

============================================Web Scraping with Python and BeautifulSoup===============================================

scraping the movies from 2000-2018 with movie name , year, ratings, metascores and votes....
and storing those scraped content in a CSV format file(in the form of dataset)...

tools used:
        Beautiful Soup
        pandas
        requests


"""


from requests import get
from bs4 import BeautifulSoup
import pandas as pd
from time import time
from time import sleep
from random import randint
from IPython.core.display import clear_output
from warnings import warn
names = []
years = []
imdb_ratings = []
metascores = []
votes = []
pages = [str(i) for i in range(1, 5)]
years_url = [str(i) for i in range(2000, 2018)]
start_time = time()
requests = 0

for year_url in years_url:
    for page in pages:

        response = get('http://www.imdb.com/search/title?release_date='+year_url+'&sort=num_votes,desc&page='+page)
        sleep(randint(8, 15))
        requests += 1
        elapsed_time = time() - start_time
        print('Request:{}; Frequency: {} requests/s'.format(requests, requests / elapsed_time))
        clear_output(wait=True)

        # Throw a warning for non-200 status codes
        if response.status_code != 200:
            warn('Request: {}; Status code: {}'.format(requests, response.status_code))

        # Break the loop if the number of requests is greater than expected
        if requests > 72:
            warn('Number of requests was greater than expected.')
            break

        page_html = BeautifulSoup(response.text, 'html.parser')
        movie_container = page_html.find_all('div', class_='lister-item mode-advanced')
        for container in movie_container:
            if container.find('div', class_='ratings-metascore') is not None:
                name = container.h3.a.text
                names.append(name)

                year = container.h3.find('span', class_='lister-item-year text-muted unbold').text
                years.append(year)

                imdb = float(container.strong.text)
                imdb_ratings.append(imdb)

                m_score = container.find('span', class_='metascore').text
                metascores.append(int(m_score))

                vote = container.find('span', attrs={'name': 'nv'})
                votes.append(int(vote['data-value']))

mv_ratings = pd.DataFrame({'movie': names,
                          'year': years,
                           'imdb': imdb_ratings,
                           'metascore': metascores,
                           'votes': votes})
print(mv_ratings.info())
mv_ratings.head(10)
mv_ratings.to_csv('movie_ratings.csv')

