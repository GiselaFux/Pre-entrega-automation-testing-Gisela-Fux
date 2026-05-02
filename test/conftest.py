import pytest
import os      # ← sin esto no puede crear la carpeta
import time    # ← sin esto no puede hacer el timestamp

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

      
# prueba de ejemplo para mostrar el hook de captura de pantalla
  

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook que captura una screenshot automaticamente si un test falla.
    La imagen se guarda en reports/screenshots/ con nombre y timestamp.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            carpeta = os.path.join("reports", "screenshots")
            os.makedirs(carpeta, exist_ok=True)
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            nombre = item.name.replace(" ", "_")
            ruta = os.path.join(carpeta, f"FALLO_{nombre}_{timestamp}.png")
            driver.save_screenshot(ruta)
            print(f"\n Screenshot guardada: {ruta}")


""" explicacion:   ¿Qué es un hook?Es una función especial que pytest ejecuta automáticamente en momentos específicos — vos no la llamás, pytest la llama solo.
@pytest.hookimpl(tryfirst=True, hookwrapper=True)   tryfirst → este hook corre antes que cualquier otro  ---hookwrapper → permite ejecutar código ANTES y DESPUÉS del test
pythondef pytest_runtest_makereport(item, call): --pytest la llama automáticamente después de cada test----item → el test que acaba de correcall → la fase del test (setup, call, teardown)
pythonoutcome = yield    -----yield → acá corre el test
report = outcome.get_result()    -----después del yield tenés el resultado del test
pythonif report.when == "call" and report.failed:      ----when == "call" → solo cuando corre el cuerpo del test (no el setup)  ---report.failed → solo si falló
pythondriver = item.funcargs.get("driver")
if driver:
    driver.save_screenshot(ruta)-----agarra el fixture driver del test que falla saca una captura de pantalla automática
Flujo completo simplificado:
test corre
    ↓
¿falló?
    ↓ sí
¿tiene driver?
    ↓ sí
📸 screenshot automática en reports/screenshots/"""