from bs4 import BeautifulSoup
import requests
import pandas as pd

url='https://www.coingecko.com/en'

response = requests.get(url)


soup = BeautifulSoup(response.content, 'html.parser')
results= soup.find('table',  {'class':'table-scrollable'}).find('tbody').find_all('tr')
len(results)

nom = []
prix = []
change_1h = []
change_24h = []
change_7d = []
volume_24h = []
market_cap = []

for result in results :
        nom.append(result.find('a',{'class':'tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between'}).get_text().strip())
    
        prix.append(result.find('td',{'class':'td-price'}).get_text().strip())
        
        change_1h.append(result.find('td',{'class':'td-change1h'}).get_text().strip())
    
        change_24h.append(result.find('td',{'class':'td-change24h'}).get_text().strip())

        change_7d.append(result.find('td',{'class':'td-change7d'}).get_text().strip())
        
        volume_24h.append(result.find('td',{'class':'td-liquidity_score'}).get_text().strip())
        
        market_cap.append(result.find('td',{'class':'td-market_cap'}).get_text().strip())
        
données_crypto=pd.DataFrame({'Coin':nom,'Price':prix,'Change_1h':change_1h,'Change_24h':change_24h,'Change_7d':change_7d,'Volume_24h':volume_24h,'Market Cap':market_cap})
