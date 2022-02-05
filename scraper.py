from typing import final
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
    a_tag = results.find_all('a')
    citations = [a for a in a_tag if 'citation needed' in a.text]
    parent = [a.find_parent('p') for a in citations]
    final_string = ""
    for a in parent:
        final_string += a.text
    return final_string

# URL = 'https://en.wikipedia.org/wiki/Beer'
# print(get_citations_needed_report(URL))