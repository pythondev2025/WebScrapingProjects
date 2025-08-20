from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Firefox()
print(type(browser))
browser.get('https://inventwithpython.com')

# SEVERAL METHODS FOR SELECTING THE ELEMENTS OF THE BROWSED PAGE (usable for both element and elements)
# from selenium.webdriver.common.by import By
# browser.find_elements(By.CLASS_NAME, name)
# browser.find_element(By.ID, id_name)
# browser.find_element(By.CSS_SELECTOR, name)
# browser.find_element(By.LINK_TEXT, text_under_<a>_tag)
# browser.find_elements(By.PARTIAL_LINK_TEXT, text)
# browser.find_elements(By.TAG_NAME, tag_Name)
# paragraph = browser.find_element(By.CLASS_NAME, "col-md-8 col-lg-9")
para_elem = browser.find_element(By.CSS_SELECTOR, "div.row:nth-child(5) > div:nth-child(2) > p:nth-child(1)")
para = para_elem.text
print(para)
link_elem = browser.find_element(By.LINK_TEXT, "Read Online for Free")
link_elem.click()
