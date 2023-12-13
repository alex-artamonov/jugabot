from bs4 import BeautifulSoup
import requests


def read_conj(verb):

    """Returns the table of conjugation of a given Spanish verb"""

    query_string = f"https://www.wordreference.com/conj/esverbs.aspx?v={verb}"
    print(query_string)
    html = requests.get(query_string).content
    soup = BeautifulSoup(html, "lxml")
    resultset1 = soup.find_all("table", class_="neoConj")
    soup = BeautifulSoup(html, "lxml").find(id="conjtable")

    # <b> tag gets in the way:
    try:
        soup.b.unwrap()
    except AttributeError:
        pass  # in case there's no <b> tag

    # because some footprint of unwrapping <b> stays anyway
    markup = str(soup)
    resultset2 = BeautifulSoup(markup, "lxml").find(id="conjtable")

    return resultset1, resultset2

