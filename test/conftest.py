import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.auth_funciones import register

@pytest.fixture
def driver():
    """Fixture que abre Chrome antes del test y lo cierra al terminar."""
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver          # acá corre el test
    driver.quit()         # esto se ejecuta siempre al terminar
    
@pytest.fixture
def carrito_vacio():
    return []

@pytest.fixture
def producto():
    return {"nombre": "Producto1", "precio": 10.0}

@pytest.fixture
def usuario_registrado():
    register("standard_user", "secret_sauce")
    return "standard_user"

      
   




