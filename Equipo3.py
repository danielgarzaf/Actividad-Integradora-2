import os
import time
import urllib.request
import numpy as np
import pandas as pd
from cv2 import cv2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# PATH a Chromedrive
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

iIndex = 0

def downloadImg(imgURL):
    """
    Función para descargar una imagen dado un URL como parametro
    """
    global iIndex
    # Actualizar estado para el usuario
    if(iIndex%10 == 0):
        print("Se han revisado {} urls.".format(iIndex))
    iIndex += 1

    try: # Intentara hacer el request para descargar la imagen
        httpResponse = urllib.request.urlopen(imgURL)
        imgTemp = np.asarray(bytearray(httpResponse.read()), dtype="uint8")
        imgTemp = cv2.imdecode(imgTemp, cv2.IMREAD_COLOR)
        return imgTemp
    
    # En caso de que el URL ya no exista o algo más, se regresa vació
    except Exception:
        return float('NaN')
    

def makeDirectories(keyWord):
    """
    Función para crear los directorios donde guardar los datasets
    """
    # Obtiene el directorio padre
    parentDir = os.path.abspath('.')

    # Crea los directorios de Train
    trainDir = os.path.join(parentDir, 'train')
    if (not os.path.exists(trainDir)):
        os.mkdir(trainDir)
    trainDir = os.path.join(trainDir, keyWord)
    if (not os.path.exists(trainDir)):
        os.mkdir(trainDir)
        
    # Crea los directorios de Test
    testDir = os.path.join(parentDir, 'test')
    if (not os.path.exists(testDir)):
        os.mkdir(testDir)
    testDir = os.path.join(testDir, keyWord)
    if (not os.path.exists(testDir)):
        os.mkdir(testDir)
    
    return (trainDir, testDir)


# Databases 
image_net = "http://image-net.org"
shutterstock = "https://www.shutterstock.com"

# Va a la dirección especificada
driver.get(image_net)

# Encuentra el elemento para poder hacer la búsqueda
# search = driver.find_element_by_name("searchterm") # Si se está usando shutterstock
search = driver.find_element_by_id("searchbox") # Si se está usando image-net

# Solicita el input del usuario, lo escribe y hace enter
keyWord = input("Keyword a buscar: ")
search.send_keys(keyWord)
search.send_keys(Keys.RETURN)

# Selecciona el primer resultado de la búsqueda y da click
driver.find_element_by_xpath("//span[@class='result_synset']").click()

# Espera 10 segundos para que cargue toda la pagina
time.sleep(10)

# Busca y abre la pestaña de Downloads
driver.find_element_by_link_text('Downloads').click()

# Busca y abre la pestaña de Downloads
driver.find_element_by_link_text('URLs').click()

# Buscar la tag llamada Pre que contiene el string de los urls
imagesURLs = driver.find_element_by_tag_name('pre').text

# Pasa los URLS de un string grade a una lista de strings
imagesURLs = imagesURLs.split('\n')

# Cierra la ventana del browser
driver.quit()

# From Python list to Pandas Series 
imagesURLs = pd.Series(imagesURLs)

print("\nIniciando a descargar de {} URLs.".format(len(imagesURLs)))

# Obtner las imagenes o valores nulos de aquellas 
# imagenes que no estan disponibles
imgList = imagesURLs.map(lambda url: downloadImg(url))

# Borrar los valores nulos
imgList = imgList[~imgList.isnull()]

print("De {} imagenes realmente se pudieron descargar {}.".format(len(imagesURLs), len(imgList)))

# Calcular la cantidad de imagenes correspondientes al 80%
porcentajeImg = int(len(imgList)*0.8)

# Dividir el dataset
Train = imgList[:porcentajeImg]
Test = imgList[porcentajeImg:]

# Obtener las rutas a los directorios
trainDir, testDir = makeDirectories(keyWord)

# Guardar las imagenes
iIndex = 0
for imgTemp in Train:
    cv2.imwrite(os.path.join(trainDir, str(iIndex) + '.jpg'), imgTemp)
    iIndex += 1
    
for imgTemp in Test:
    cv2.imwrite(os.path.join(testDir, str(iIndex) + '.jpg'), imgTemp)
    iIndex += 1
    
print('\nLos datasets fueron guardados\n\tTrain: {}\n\tTest: {}'.format(len(Train), len(Test)))
