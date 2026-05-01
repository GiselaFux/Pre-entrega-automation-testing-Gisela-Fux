from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

def hacer_login(driver: WebDriver, usuario="standard_user", password="secret_sauce") -> None:
    """Función auxiliar: hace login en saucedemo y deja el driver en /inventory.html"""
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys(usuario)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()