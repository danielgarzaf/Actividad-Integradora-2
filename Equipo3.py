from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import numpy as np
import urllib
import cv2

# DRIVER_PATH = './chromedriver'
# driver = webdriver.Chrome(executable_path=DRIVER_PATH)

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Función para descargar una imagen desde su URL
def downloadImg(url):
    response = urllib.request.urlopen(url)
    img = np.asarray(bytearray(response.read()), dtype="uint8")
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    return img



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

# Selecciona el primer resultado de la búsqueda y da click
driver.find_element_by_xpath("//span[@class='result_synset']").click()


# Obtiene la lista de urls de las imágenes



# Cierra la ventana del browser
# driver.quit()


# Lista de URLs
urls = [
    "https://pyimagesearch.com/wp-content/uploads/2015/01/google_logo.png",
    "https://pyimagesearch.com/wp-content/uploads/2014/12/adrian_face_detection_sidebar.png",
]


index = 0
# Recorre la lista de URLs y descarga cada imagen
for url in urls:
    img = downloadImg(url)
    name = 'image'+str(index)+'.jpg'
    cv2.imwrite(name,img)
    cv2.destroyAllWindows()
    index = index + 1
