from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def hacer_login(driver, usuario="standard_user", password="secret_sauce") -> None:
    """Función auxiliar: hace login en saucedemo y deja el driver en /inventory.html"""
    # Navega primero para poder borrar las cookies del dominio
    driver.get("https://www.saucedemo.com")
    # Limpia cookies y localStorage para garantizar sesión y carrito frescos
    driver.delete_all_cookies()
    driver.execute_script("window.localStorage.clear();")
    # Recarga la página limpia
    driver.get("https://www.saucedemo.com")

    # Escribe usuario y contraseña
    driver.find_element(By.ID, "user-name").send_keys(usuario)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

    # Espera a que el login termine y la página de inventario cargue completamente
    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )


def hacer_login_invalido(driver, usuario="standard_user", password="wrong_password"):
    # Hace login con contraseña incorrecta para probar mensaje de error
    driver.get("https://www.saucedemo.com")
    driver.delete_all_cookies()
    driver.execute_script("window.localStorage.clear();")
    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys(usuario)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
    # No se espera URL porque el login falla y quedamos en la misma página


# -> None → la función no devuelve nada, solo realiza acciones (guardar un screenshot en este caso)
def falla_intencional_screenshot(driver) -> None:
    """
    Función auxiliar: navega a la página de login y falla a propósito
    para verificar que el hook captura la screenshot automáticamente.
    """
    driver.get("https://www.saucedemo.com")

    # Esto va a fallar porque el título real es "Swag Labs"
    assert driver.title == "Prueba de captura de pantalla por no entregar el titulo swagLabs,sino este msj"
