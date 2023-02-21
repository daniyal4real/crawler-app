import requests
from bs4 import BeautifulSoup

class Prodcut:
    name = str
    # publication_date = str
    # link = str
    content = []
    
    def __init__(self) -> None:
        pass
    
    def __init__(self, name):
        self.name = name
        # self.publication_date = publication_date
        # self.link = link
        self.content = []

    def __repr__(self):
        return str(self.__dict__)
        

 
class Detail: 
    content = str 
    
    def __init__(self, content):
        self.content = content   
        
        
headers = {
    'authority': 'www.yeezysupply.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept-language': 'en-US,en;q=0.9',
}

def getNewsFromFirst():
    session = requests.session()


    news = []
    news_details = []
    response = session.get('https://baigenews.kz/news/', headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    # for element in soup.find_all('li', class_='finded__content__item'):
    #     name = element.find('span', class_="finded__content__item__content__title  ").text.get_text()
    #     # publication_date = element.find('span', class_="date").text.strip()
    #     # link = "https://tengrinews.kz/" + element.find('a').get('href')

    #     prodcut = Prodcut(name)
    #     news.append(prodcut)
        
    for element in soup.find_all('ul', class_="uk-list exec-news"):
        name = element.find('span', class_='finded__content__item__content__caption')
        print(name)
    # for i in news:
    #     print(i)
    # for every in news:
    #     response2 = requests.get(every.link, headers=headers)
    #     soup2 = BeautifulSoup(response2.text, 'html.parser')
    # response2 = requests.get(link, headers=headers)
    # soup2 = BeautifulSoup(response2.text, 'html.parser')
    
    # for element2 in soup2.find_all('p'):
    #     print(element2)
        # detail = Detail(content)
        # news_details.append(detail)
        
    #     for j in soup2.find_all('p'):
    #         prodcut.content = j.get_text()
    
    # for i in news:
    #     print(i)
    
    
    
    # for i in news_details:
    #     print(i)
    # for i in news_details:
    #     print(i)
        # publication_date = element.find('span', class_="date").text.strip()
        # link = "https://tengrinews.kz/" + element.find('a').get('href')

        # prodcut.setContent(text)
        # print("CONTENT", news_details)

    
        
        
    # for element2 in soup2.find_all('article', class_='tn-news-text'):
    #     news_details.append(element2.find('p').text.strip())
    # for element2 in soup2.find_all('div', class_='post-content'):
    #     news_details.append(element2.find('p').text.strip())
    #     print(element2)
        # publication_date = element.find('span', class_="date").text.strip()
        # link = "https://tengrinews.kz/" + element.find('a').get('href')

        # prodcut.setContent(text)
        # print("CONTENT", news_details)
        
    # for i in range(0, 10):
    #     news_details.append("TEST")
    # for i in range(0, len(news_details)):
    #     print("DETAILS", news_details[i])
getNewsFromFirst()
