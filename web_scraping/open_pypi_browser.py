import sys
import webbrowser
import bs4
import requests


# get the text using requests
print("Searching...")
res = requests.get("https://docs.python.org/3/search.html?q=" + "+".join(sys.argv[1:]))
res.raise_for_status()

print(res.text)
soup = bs4.BeautifulSoup(res.text, "html.parser")
req_links_list = soup.select("a[href^='library/']")
no_of_links = min(10, len(req_links_list))
print(no_of_links)
for i in range(no_of_links):
    search_result = f"https://pypi.org{req_links_list[i].get('href')}"
    webbrowser.open(search_result)

