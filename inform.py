import requests
from bs4 import BeautifulSoup
from time import sleep
import psycopg2
from psycopg2 import sql

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.73', 'accept':'*/*'}


        
def bulkInsert(title, description):
    try:
        #connect to the existing database
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='2747',
            database='news'
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
            "INSERT INTO news(title, description) VALUES"
            "(%s, %s)", (title, description)
            )
        print("[INFO] data was inserted succesfully")
    
    except Exception as _ex:
        print("[INFO] Error while working with Postgres", _ex)

    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")


            
            
def get_url():
    sleep(1)
    URL = f'https://informburo.kz'
    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='uk-width-1-4@m uk-width-1-2@s uk-width-1-1 uk-margin-medium-bottom')

    for item in items:
        link = item.find('a').get('href')
        yield link

def start():
    for link in get_url():
        try:
            response = requests.get(link, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')

            data = soup.find('div', class_= 'uk-width-2-3@m uk-width-1-1')
            if data == None:
                continue
            article = data.find('h3', class_='article-excerpt').text
            if article == None:
                continue
            text = data.find('div', class_='article').get_text()
            if text == None:
                continue
            print(article + text)
            bulkInsert(article, text)
            
        except:
            print('error')
        
        
start()