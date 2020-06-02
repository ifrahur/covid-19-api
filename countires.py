import requests
from bs4 import BeautifulSoup
import time


def getData():
    countryData = {
        'success': True,
        'data': []
    }
    try:
        htmlBody = requests.get(
            'https://www.worldometers.info/coronavirus/#countries')
    except requests.exceptions.RequestException as e:
        countryData['success'] = False
        countryData['error'] = str(e)
        return countryData

    soup = BeautifulSoup(htmlBody.text, 'lxml')

    table = soup.table

    table_rows = table.find_all('tr')[9:-8]

    for tr in table_rows:
        td = tr.find_all('td')[1:]
        row = [i.text for i in td]
        country = row[0]

        try:
            total_cases = row[1]
        except AttributeError:
            total_cases = None

        try:
            active_cases = row[6]
        except AttributeError:
            active_cases = None

        try:
            total_deaths = row[3]
        except AttributeError:
            total_deaths = None

        try:
            total_recovered = row[5]
        except AttributeError:
            total_recovered = None

        try:
            new_cases = row[2]
        except AttributeError:
            new_cases = None

        countriesData = {
            'country': country,
            'total_cases': total_cases,
            'active_cases': active_cases,
            'total_deaths': total_deaths,
            'total_recovered': total_recovered,
            'new_cases': new_cases
        }

        countryData['data'].append(countriesData)

    return countryData
