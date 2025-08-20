from bs4 import BeautifulSoup
import requests
import csv


def example_1():
    res = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7889712&lon=-122.3954798")
    # res.raise_for_status()
    if res.status_code == requests.codes.ok:
        no_starch = BeautifulSoup(res.text, "lxml")
        forecast = no_starch.select("div.row-odd:nth-child(1) > div:nth-child(2)")
        print(forecast[0].getText())


file = open("example.html")
data = BeautifulSoup(file.read(), "html.parser")
elem = data.getText("#author")
# text = elem[0]
print(elem)
p_elem = data.select("p")
print(len(p_elem))
site_data = []
for elem in p_elem:
    with open("site_data.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow(elem.getText())

