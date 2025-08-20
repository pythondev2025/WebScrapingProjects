import os
import requests
import bs4

i = 1
os.makedirs("xkcd", exist_ok=True)
url = "https://xkcd.com/"
while not url.endswith("#"):
    print(f"Downloading {url}...")
    res = requests.get(url)
    res.raise_for_status()

    # using bs4
    soup = bs4.BeautifulSoup(res.text, "lxml")
    url_list = soup.select("#comic img")
    image_url = "https:" + url_list[0].get("src")
    image = requests.get(image_url)
    with open(f"xkcd/image{i}.png","wb") as imagefile:
        for chunk in image.iter_content(100000):
            imagefile.write(chunk)
    i += 1
    prev_url_list = soup.select("a[rel='prev']")
    url = "https://xkcd.com" + prev_url_list[0].get("href")

