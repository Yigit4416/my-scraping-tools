from bs4 import BeautifulSoup
import requests

sentence = ""
our_input = input("enter a sentence: ")

for x in our_input:
    if x != " ":
        sentence += x
    else:
        sentence += "%20"

url = "https://www.deepl.com/tr/translator#tr/en-us/" + sentence

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# TODO: find the translation part

table = soup.find_all('section')

print(table[1])