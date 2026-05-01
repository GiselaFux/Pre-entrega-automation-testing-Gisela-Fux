from selenium.webdriver.common.by import By  # type: ignore
from selenium.webdriver.support.ui import WebDriverWait  # type: ignore
from selenium.webdriver.support import expected_conditions as EC  # type: ignore

print("Imports OK")


def agregar_primer_producto(driver):
    """Hace clic en el botón 'Add to cart' del primer producto del catálogo."""
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
    )
    primer_producto = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]
    nombre = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    primer_producto.find_element(By.TAG_NAME, "button").click()
    return nombre  # devuelve el nombre para validarlo después


def obtener_contador_carrito(driver):
    """Espera y devuelve el número del badge del carrito."""
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    return driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text


def navegar_al_carrito(driver):
    """Hace clic en el ícono del carrito y espera a que cargue /cart.html."""
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    WebDriverWait(driver, 10).until(
        EC.url_contains("/cart.html")
    )


def obtener_productos_en_carrito(driver):
    """Devuelve la lista de productos que están dentro del carrito."""
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "cart_item"))
    )
    return driver.find_elements(By.CLASS_NAME, "cart_item")


def obtener_nombre_item_carrito(item):
    """Devuelve el nombre de un producto dentro del carrito."""
    return item.find_element(By.CLASS_NAME, "inventory_item_name").text
