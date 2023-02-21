import requests
from bs4 import BeautifulSoup


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

    response = session.get('https://tengrinews.kz', headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    listt = []
    # for element in soup.find_all('div', class_='tn-main-news-item'):
    #     name = element.find('span')
    #     name.replace('<span>', '').strip()
    #     # price = element.find('span', class_="product-card__price").text.strip()
    #     # link = "https://kith.com/" + element.find('a').get('href')

    #     listt.append(name)
    
    # spans = soup.find_all('span', {'class': 'tn-main-news-title'})
    # for span in spans:
    #     print(span.text.replace('<span>', '').strip())

    list_links = []
    
    
    # links = soup.find_all('a', {'class': 'tn-link'})
    # for link in links:
    #     list_links.append('https://tengrinews.kz' + link.get('href'))
    
    for element in soup.find_all('div', class_='tn-main-news-container tn-sub-container'):
        for i in element:
            link = 'https://tengrinews.kz' + i.find('a', class_='tn-link').get('href')

            list_links.append(link)
    
    print(list_links)
getNewsFromFirst()
