

import math
import os
import random
import re
import sys



#
# Complete the 'getNumDraws' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER year as parameter.
#
import requests
from concurrent.futures import ThreadPoolExecutor

def url_list(year, last_page):

    for i in range(1, last_page+1):
        yield f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&page={i}'
        
def extract(url):
    global counter
    response = requests.get(url=url)
    data = response.json()

    for lst_details in data['data']:
        if lst_details['team1goals'] == lst_details['team2goals']:
            counter += 1

    return counter
            
def getNumDraws(year):
    global counter
    print('hello')
    # Write your code here
    url = f'https://jsonmock.hackerrank.com/api/football_matches?year={year}'
    
    response = requests.get(url=url)
    data = response.json()
    
    counter = 0
    
    last_page = data['total_pages']
    urls_lst = []
    urls = url_list(year, last_page)
    for i in urls:
        urls_lst.append(i)
        
    with ThreadPoolExecutor(max_workers = 50) as executor:
        executor.map(extract, urls_lst)
        executor.shutdown(wait=True)
    return counter
            
        

if __name__ == '__main__':

    year = int(input().strip())

    result = getNumDraws(year)
    print(result)

