import pytest
#By es una clase de Selenium que define las formas de localizar elementos en la página.
from selenium.webdriver.common.by import By
#WebDriverWait permite hacer esperas explícitas hasta que se cumpla una condición.
from selenium.webdriver.support.ui import WebDriverWait
#expected_conditions (alias EC) contiene muchas funciones que describen condiciones que esperamos que se cumplan en la página, como que un elemento sea visible o que la URL cambie.
from selenium.webdriver.support import expected_conditions as EC
from utils.selenium_functions_login import hacer_login, falla_intencional_screenshot, hacer_login_invalido


def test_login_exitoso(driver):
    """Valida que el login con credenciales válidas redirija a /inventory.html"""
    hacer_login(driver)

    # Espera explícita hasta que la URL cambie hasta 10 segundos
    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )

    assert "/inventory.html" in driver.current_url
    print("Login exitoso →", driver.current_url)
    
def test_login_invalido(driver):
        """Valida que el login con credenciales inválidas muestre mensaje de error"""
        hacer_login_invalido(driver)

        # Espera explícita hasta que aparezca el mensaje de error
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
        )

        error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
        assert "Epic sadface" in error
        print("Epic sadface: Username and password do not match any user in this service") 
  

def test_falla_intencional_screenshot(driver):
    """
    Test que falla a propósito para verificar que el hook
    captura la screenshot automáticamente.
    """
    falla_intencional_screenshot(driver)  # ← llama a la función, no repite la lógica