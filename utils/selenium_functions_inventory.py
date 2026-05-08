from selenium.webdriver.common.by import By  #Importa la clase By de Selenium, que se utiliza para localizar elementos en la página web.
from selenium.webdriver.support.ui import WebDriverWait #Importa la clase WebDriverWait de Selenium, que se utiliza para hacer esperas explícitas hasta que se cumpla una condición.
from selenium.webdriver.support import expected_conditions as EC #Importa el módulo expected_conditions de Selenium, que contiene funciones para describir condiciones que esperamos que se cumplan.


def obtener_titulo_inventario(driver):
    """Espera y devuelve el título de la sección de inventario."""
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )
    return driver.find_element(By.CLASS_NAME, "title").text


def obtener_productos(driver):
    """Espera y devuelve la lista de todos los productos visibles."""
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
    )
    return driver.find_elements(By.CLASS_NAME, "inventory_item") 
    

def obtener_nombre_producto(producto):
    """Devuelve el nombre de un producto."""
    return producto.find_element(By.CLASS_NAME, "inventory_item_name").text

def obtener_nombres_productos(driver):
    """Devuelve una lista con los nombres de todos los productos visibles."""
    productos = obtener_productos(driver)
    nombres = [obtener_nombre_producto(producto) for producto in productos]
    return nombres

def obtener_precio_producto(producto):
    """Devuelve el precio de un producto dado."""
    return producto.find_element(By.CLASS_NAME, "inventory_item_price").text


""" def verificar_menu(driver):
    
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    return menu.is_displayed() """
def verificar_menu(driver, timeout=10):
    wait = WebDriverWait(driver, timeout)
    wait.until(EC.visibility_of_element_located((By.ID, "react-burger-menu-btn")))
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    return menu.is_displayed()    


def verificar_filtro(driver,timeout=10):
    """Verifica que el filtro de ordenamiento esté visible. Devuelve True/False."""
    wait = WebDriverWait(driver, timeout)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product_sort_container")))
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
    return filtro.is_displayed()


def verificar_carrito_icono(driver, timeout=10):
    """Verifica que el ícono del carrito esté visible. Devuelve True/False."""
    wait = WebDriverWait(driver, timeout)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_link")))
    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    return carrito.is_displayed()