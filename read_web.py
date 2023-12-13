from bs4 import BeautifulSoup
import requests


def read_conj(verb):

    """Returns the table of conjugation of a given Spanish verb"""

    query_string = f"https://www.wordreference.com/conj/esverbs.aspx?v={verb}"
    # print(query_string)
    html = requests.get(query_string).content
    soup = BeautifulSoup(html, "lxml")
    return soup.find_all("table", class_="neoConj")

