from bs4 import BeautifulSoup
import requests

tefas_codes = ['IOO', 'YKT']

everything = {}

everything["Fon Kodu"] = []
everything["Son Fiyat (TL)"] = []
everything["Günlük Getiri (%)"] = []
everything["Pay (Adet)"] = []
everything["Fon Toplam Değer (TL)"] = []
everything["Kategorisi"] = []
everything["Son Fiyat (TL)"]

for fon in tefas_codes:
    url = f"https://www.tefas.gov.tr/FonAnaliz.aspx?FonKod={fon}"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    table = soup.find('ul', class_="top-list")
    elements = table.find_all('li')

    for element in elements:
        for span in element.find_all("span"):
            temp_span = span.get_text(strip=True)
            span.decompose()
        text = element.get_text(strip=True)
        everything[text].append(temp_span)
    everything["Fon Kodu"].append(fon)

for temp in range(len(everything["Fon Kodu"])):
    individual_values = {key: values[temp] for key, values in everything.items()}
    print(individual_values)