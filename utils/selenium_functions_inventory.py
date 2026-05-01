from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
    """Devuelve el nombre de un producto dado."""
    return producto.find_element(By.CLASS_NAME, "inventory_item_name").text


def obtener_precio_producto(producto):
    """Devuelve el precio de un producto dado."""
    return producto.find_element(By.CLASS_NAME, "inventory_item_price").text


def verificar_menu(driver):
    """Verifica que el menú hamburguesa esté visible. Devuelve True/False."""
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    return menu.is_displayed()


def verificar_filtro(driver):
    """Verifica que el filtro de ordenamiento esté visible. Devuelve True/False."""
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
    return filtro.is_displayed()


def verificar_carrito_icono(driver):
    """Verifica que el ícono del carrito esté visible. Devuelve True/False."""
    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    return carrito.is_displayed()