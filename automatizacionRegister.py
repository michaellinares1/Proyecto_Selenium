# Importaciones de selenium.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# Importaciones de python.
import sys
import time
# Importaciones de MongoDB.
import pymongo

# Configuración de Selenium
service = Service(executable_path="./chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


def connect():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["swmgves"]
    collection = db["clientes"]
    return collection


def check_user(collection, correo):
    user = collection.find_one({"correo_electronico": correo})
    return user


def delete_user(collection, correo):
    collection.delete_one({"correo_electronico": correo})


# Pagina de registro
driver.get("http://localhost:4200/Crear_Usuario")

"""
    Lo que se hará en este script es automatizar el registro de un usuario en la página web.
    Luego se verificará si el usuario ya existe en la base de datos
    Si existe, se eliminará el usuario y se notificará que la prueba fue exitosa.
    Si no existe, se notificará que la prueba falló.
"""

# Constantes
NOMBRE = "Sergio"
APELLIDO = "Pinga"
CORREO = "sergio.pinga@gmail.com"
TELEFONO = "985748473"
DIRECCION = "Chorriyork av. Cucardas 1493"
CONTRASENA = "123456789"
NUMERO_DOCUMENTO = "78476372"

try:
    time.sleep(3)
    # Obtener el input de nombre
    nombre = driver.find_element(
        By.XPATH, "/html/body/app-root/app-crear-usuario/section/div/form/div[2]/input")
    nombre.send_keys(NOMBRE)

    # Obtener el input de apellido
    apellido = driver.find_element(
        By.XPATH, "/html/body/app-root/app-crear-usuario/section/div/form/div[3]/input")
    apellido.send_keys(APELLIDO)
    time.sleep(2)

    # Obtener el input de correo
    correo = driver.find_element(
        By.XPATH, "/html/body/app-root/app-crear-usuario/section/div/form/div[4]/input")
    correo.send_keys(CORREO)
    time.sleep(2)

    # Obtener el input de numero de telefono
    telefono = driver.find_element(
        By.XPATH, "/html/body/app-root/app-crear-usuario/section/div/form/div[5]/input")
    telefono.send_keys(TELEFONO)
    time.sleep(2)

    # Obtener el dropdown de tipo de usuario
    tipo_usuario_dropdown = driver.find_element(
        By.XPATH, "/html/body/app-root/app-crear-usuario/section/div/form/div[6]/select")
    tipo_usuario_dropdown.click()
    time.sleep(2)

    # Seleccionar el tipo de usuario
    tipo_usuario = driver.find_element(
        By.XPATH, "/html/body/app-root/app-crear-usuario/section/div/form/div[6]/select/option[1]")
    tipo_usuario.click()
    time.sleep(2)

    # obtener el input de numero de documento
    numero_documento = driver.find_element(
        By.XPATH, "/html/body/app-root/app-crear-usuario/section/div/form/div[7]/input")
    numero_documento.send_keys(NUMERO_DOCUMENTO)

    # obtener el input de direccion
    direccion = driver.find_element(
        By.XPATH, "/html/body/app-root/app-crear-usuario/section/div/form/div[8]/input")
    direccion.send_keys(DIRECCION)
    time.sleep(2)

    # obtener el input de contraseña
    contrasena = driver.find_element(
        By.XPATH, "/html/body/app-root/app-crear-usuario/section/div/form/div[9]/input")
    contrasena.send_keys(CONTRASENA)
    time.sleep(2)

    # Presionar botón de registrarse.
    register_button = driver.find_element(
        By.XPATH, "/html/body/app-root/app-crear-usuario/section/div/form/button")
    register_button.click()
    time.sleep(3)

    driver.quit()

    print("Registro exitoso")

    # Si todo sale bien, se conecta a la base de datos y se verifica si el usuario fue registrado.
    collection = connect()
    user = check_user(collection, CORREO)
    if user:
        print("Datos del usuario: ", user)
        delete_user(collection, CORREO)
        print("Prueba exitosa")
    else:
        print("Prueba fallida")
except:
    print("Error en el registro")
    driver.quit()
    sys.exit()
