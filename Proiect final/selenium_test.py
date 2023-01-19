from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.python.org")  # cu metoda get incarcam un url
assert "Python" in driver.title  # confirmam ca am ajuns pe pagina buna
elem = driver.find_element(By.NAME, "q")  # cautam casuta de search in pagina
elem.clear()  # curatam continutul casutei
elem.send_keys("pycon")  # scriem textul pyton
elem.send_keys(Keys.RETURN)  # apasam ENTER pe casuta
assert "No results found." not in driver.page_source  # confirmam ca avem rezultate
driver.close()  # inchidem fereastra de browser