import math
import os
import random
import re
import sys



#
# Complete the 'getWinnerTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING competition
#  2. INTEGER year
#
import requests

def getWinnerTotalGoals(competition, year):
    # Write your code here
    url = f'https://jsonmock.hackerrank.com/api/football_competitions?name={competition}&year={year}'
    response = requests.get(url)
    data = response.json()
    runnerup = data['data'][0]['runnerup']
    winner = data['data'][0]['winner']
    
    url = f'https://jsonmock.hackerrank.com/api/football_matches?competition={competition}&year={year}&team1={winner}'
    response = requests.get(url)
    data = response.json()
    pages = data['total_pages']
    count = 0
    for i in range(1,pages+1):
        print('hello')
        url = f'https://jsonmock.hackerrank.com/api/football_matches?competition={competition}&year={year}&team1={winner}&page={i}'
        response = requests.get(url)
        data = response.json()
        print(data)
        for lst in data['data']:
                won = lst['team1goals']
                count += int(won)
            
    url = f'https://jsonmock.hackerrank.com/api/football_matches?competition={competition}&year={year}&team2={winner}'
    response = requests.get(url)
    data = response.json()
    pages = data['total_pages']
    print()
    print()
    for i in range(1,pages+1):
        url = f'https://jsonmock.hackerrank.com/api/football_matches?competition={competition}&year={year}&team2={winner}&page={i}'
        response = requests.get(url)
        data = response.json()
        print(data)
        for lst in data['data']:
            won = lst['team2goals']
            count += int(won)

    return count
        

if __name__ == '__main__':
    name = input('Enter the name of the competition: ')
    year = int(input('Enter the year of competition: '))
    print(getWinnerTotalGoals(name, year))