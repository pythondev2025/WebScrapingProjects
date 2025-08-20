import pyperclip, sys, webbrowser, requests


if len(sys.argv) > 1:
    address = "+".join(sys.argv[1:])
else:
    address = pyperclip.paste()
webbrowser.open("https://www.google.com/maps/place/" + address)
webbrowser.open_new("https://en.wikipedia.org/wiki/List_of_HTTP_status_codes")
response = requests.get("https://automatetheboringstuff.com/files/rj.txt")
if response.status_code == requests.codes.ok:
    print(response.text[:300])
with open("play.txt", "wb") as file:
    for chunk in response.iter_content(100000):
        file.write(chunk)
