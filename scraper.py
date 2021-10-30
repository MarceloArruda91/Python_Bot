from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


website = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"  # website
path = Service(r"C:\Chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service = path)  # create driver
driver.get(website)  # go to website
note_brand = "lenovo"


def notebook_links():
    links_list = []
    notebook_list = driver.find_elements(By.CLASS_NAME, "caption")
    for notebook in notebook_list:
        if note_brand in notebook.text.lower():
            link = notebook.find_element(By.CLASS_NAME, "title").get_attribute("href")
            links_list.append(link)
    return links_list



notebook_links()
print(notebook_links())