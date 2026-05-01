import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.selenium_functions_login import hacer_login


def test_login_exitoso(driver):
    """Valida que el login con credenciales válidas redirija a /inventory.html"""
    hacer_login(driver)

    # Espera explícita hasta que la URL cambie
    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )

    assert "/inventory.html" in driver.current_url
    print("Login exitoso →", driver.current_url)