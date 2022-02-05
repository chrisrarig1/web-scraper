import requests
from bs4 import BeautifulSoup


def get_citations_needed_count(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(class_="vector-body")
    a_tag = results.find_all('a')
    citations = [a for a in a_tag if 'citation needed' in a.text]
    return len(citations)

def get_citations_needed_report(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(class_="vector-body")
    p_tag = results.find_all('p')
    citations = [a for a in p_tag if 'citation needed' in a.text]
    for a in citations:
        return str(a.text)

URL = 'https://en.wikipedia.org/wiki/Beer'

print(get_citations_needed_report(URL))