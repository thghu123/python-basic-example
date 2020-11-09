import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="


for page in range(1,5):
    res = requests.get(url+str(page))
    res.raise_for_status()
    
