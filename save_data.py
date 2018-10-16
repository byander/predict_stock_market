import requests
import datetime
from db import connect

file = open("API_KEY.txt","r")
API_KEY = file.read()

SYMBOL = 'VALE3'
OUTPUTSIZE = 'compact'  # compact: last 100 data points; full: last 20 years

def get_result():
    r = requests.get(
        'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + SYMBOL +
        '.SA&outputsize=' + OUTPUTSIZE + '&apikey={}'.format(API_KEY))

    if r.status_code == 200:
        data = r.json()
        data = data['Time Series (Daily)']

        result = []
        for d, p in data.items():
            if float(p['4. close']) == 0:
                continue

            date = datetime.datetime.strptime(d, '%Y-%m-%d')
            data_row = [date, float(p['1. open']), float(p['2. high']), float(p['3. low']), float(p['4. close']),
                        int(p['5. volume'])]
            result.append(data_row)

        return result

def import_data():
    con = connect()
    cursor = con.cursor()

    for item in get_result():
        sql = "INSERT INTO time_series_daily (symbol, date, open, high, low, close, volume) VALUES " \
              "(%s, %s, %s, %s, %s, %s, %s)"
        values = (SYMBOL, item[0], item[1], item[2], item[3], item[4], item[5])
        cursor.execute(sql, values)
        con.commit()
    con.close()


import_data()

file.close()
print("Dados importados com sucesso!")
