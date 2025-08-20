from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def filling_the_form():
    browser = webdriver.Firefox()
    browser.get("https://login.metafilter.com/")
    user_elem = browser.find_element(By.XPATH, "//input[@id='user_name']")
    user_elem.send_keys("my_username")

    user_pass = browser.find_element(By.ID, "user_pass")
    user_pass.send_keys("my_password")
    user_pass.submit()


browser = webdriver.Firefox()
browser.get("https://nostarch.com")
elem = browser.find_element(By.TAG_NAME, "html")
elem.send_keys(Keys.END)
elem.send_keys(Keys.PAGE_UP)
elem.send_keys(Keys.PAGE_UP)
elem.send_keys(Keys.PAGE_UP)
elem.send_keys(Keys.PAGE_UP)
elem.send_keys(Keys.PAGE_UP)
elem.send_keys(Keys.PAGE_UP)
browser.refresh()
browser.quit()

# elem.send_keys(Keys.HOME)


'''
Clicking Browser Buttons
The selenium module can simulate clicks on various browser buttons as well
through the following methods:
browser.back() Clicks the Back button.
browser.forward() Clicks the Forward button.
browser.refresh() Clicks the Refresh/Reload button.
browser.quit() Clicks the Close Window button
'''
