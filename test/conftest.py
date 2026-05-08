import pytest
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def driver():
    """Un solo Chrome para toda la sesión de tests."""
    options = Options()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")  # activa esto si querés más velocidad y nada de ventana
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Desactiva el gestor de contraseñas de Chrome para evitar un pop-up, lo tomma como amenaza y me bloquea los tests en el login, por eso lo desactivo.
    # "Cambia la contraseña / contraseña encontrada en filtración de datos"
    prefs = {
        "credentials_enable_service": False,    # Desactiva el servicio de gestión de contraseñas.Evita que Chrome intente ofrecerte guardar contraseña.
        "profile.password_manager_enabled": False,   # Deshabilita el gestor de contraseñas del perfil actual de Chrome.Evita el pop-up que pregunta si quieres guardar la contraseña.
        "profile.password_manager_leak_detection": False # Desactiva la función de detección de fugas de contraseñas.Evita que aparezca el pop-up que me frena los tests.
    }
    options.add_experimental_option("prefs", prefs) # Le dice a Chrome: “arrancá con estas preferencias (prefs) ya configuradas”, por ejemplo desactivar el gestor de contraseñas y sus avisos.

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    yield driver

    driver.quit()


# Hook: captura screenshot si el test falla
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook que captura una screenshot automáticamente si un test falla.
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
