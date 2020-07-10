from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Va a la dirección especificada
driver.get("https://www.shutterstock.com")

# Encuentra el elemento para poder hacer la búsqueda
search = driver.find_element_by_name("searchterm")

# Solicita el input del usuario, lo escribe y hace enter
search.send_keys(input("Buscar: "))
search.send_keys(Keys.RETURN)

# Cierra la ventana del browser
# driver.quit()
