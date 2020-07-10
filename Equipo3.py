from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

image_net = "http://image-net.org"
shutterstock = "https://www.shutterstock.com"

# Va a la dirección especificada
driver.get(image_net)

# Encuentra el elemento para poder hacer la búsqueda
# search = driver.find_element_by_name("searchterm") # Si se está usando shutterstock
search = driver.find_element_by_id("searchbox") # Si se está usando image-net

# Solicita el input del usuario, lo escribe y hace enter
search.send_keys(input("Buscar: "))
search.send_keys(Keys.RETURN)

# Cierra la ventana del browser
# driver.quit()
