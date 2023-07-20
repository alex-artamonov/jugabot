from bs4 import BeautifulSoup, element
import requests


def read_conj(verb):

    """Returns the table of conjugation of a given Spanish verb"""

    query_string = f"https://www.wordreference.com/conj/esverbs.aspx?v={verb}"
    print(query_string)
    html = requests.get(query_string).content
    soup = BeautifulSoup(html, "lxml")
    return soup.find_all("table", class_="neoConj")


# print(soup.head.title.contents)
# print(soup.body.a.text)
# print(soup.find_all('h3')[0].next)
# print(soup.find_all('h4'))

# for ele in sp:
#     print(ele.text)


# result = []

# with open("./result.html", "w") as file:
#     for ele in h4:
#         # print(ele.text)
#         file.write(str(ele))

# print(result, len(result))
