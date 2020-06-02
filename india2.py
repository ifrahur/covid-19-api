import requests
from bs4 import BeautifulSoup
import time


def getIndiaData():
    indiaData = {
        'success': True,
        'data': []
    }
    try:
        htmlBody = requests.get('https://www.mygov.in/covid-19')
    except requests.exceptions.RequestException as e:
        indiaData['success'] = False
        indiaData['error'] = str(e)
        return indiaData

    soup = BeautifulSoup(htmlBody.text, 'lxml')

    table = soup.table

    table_rows = table.find_all('tr')[1:]

    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        state_name = row[0]
        print(state_name)
        try:
            confirmed = row[1]
        except AttributeError:
            confirmed = None

        print(confirmed)

        try:
            active = row[2]
        except AttributeError:
            active = None

        print(active)

        try:
            recovered = row[3]
        except AttributeError:
            recovered = None
        print(recovered)

        try:
            deaths = row[4]
        except AttributeError:
            deaths = None
        print(deaths)

        indianData = {
            'state': state_name,
            'active': active,
            'recovered': recovered,
            'deaths': deaths
        }

        indiaData['data'].append(indianData)

    return indiaData
