import requests
from bs4 import BeautifulSoup
def request():
    r = requests.get("https://www.tgju.org")
    return r


def dollar_price(r):
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    
    row = soup.find("tr", attrs={"data-market-row": "price_dollar_rl"})

    dl_price = row.find("td", class_="nf").text.strip()
    return dl_price

def gold24(r):
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    
    row = soup.find("tr", attrs={"data-market-row": "geram24"})

    gold_24 = row.find("td", class_="nf").text.strip()
    return gold_24

def gold18(r):
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    
    row = soup.find("tr", attrs={"data-market-row": "geram18"})

    gold_18 = row.find("td", class_="nf").text.strip()
    return gold_18

def silver_999(r):
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    
    row = soup.find("tr", attrs={"data-market-row": "silver_999"})

    silver999 = row.find("td", class_="nf").text.strip()
    return silver999

def sekee_emami(r):
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    
    row = soup.find("tr", attrs={"data-market-row": "sekee"})

    sekee = row.find("td", class_="nf").text.strip()
    return sekee

def geram_sekee(r):
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    
    row = soup.find("tr", attrs={"data-market-row": "gerami"})

    sekee_gerami = row.find("td").text.strip()

    return sekee_gerami

def tether(r):
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    
    row = soup.find("tr", attrs={"data-market-row": "crypto-tether"})

    tether = row.find("td", class_="market-price-irr").text.strip()

    return tether


# سکه امامی تتر بیتکوین سکه گرمی


