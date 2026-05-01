import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.selenium_functions_inventory import obtener_titulo_inventario, obtener_productos, obtener_nombre_producto, obtener_precio_producto, verificar_menu, verificar_filtro, verificar_carrito_icono
from utils.selenium_functions_login import hacer_login

def test_titulo_pagina_inventario(driver):
    """Verifica que el título de la sección sea 'Products'"""
    hacer_login(driver)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )

    titulo = driver.find_element(By.CLASS_NAME, "title").text
    assert titulo == "Products"
    print("Título OK →", titulo)


def test_presencia_de_productos(driver):
    """Comprueba que haya al menos un producto visible en el catálogo"""
    hacer_login(driver)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
    )

    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) >= 1
    print(f"Productos encontrados: {len(productos)}")


def test_nombre_y_precio_primer_producto(driver):
    """Lista el nombre y precio del primer producto del catálogo"""
    hacer_login(driver)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
    )

    primer_producto = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]

    nombre = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text

    assert nombre != ""
    assert precio != ""
    print(f"Primer producto → Nombre: {nombre} | Precio: {precio}")


def test_elementos_interfaz_presentes(driver):
    """Valida que el menú y los filtros estén presentes en la página"""
    hacer_login(driver)

    # Menú hamburguesa
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    assert menu.is_displayed()

    # Filtro de ordenamiento
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert filtro.is_displayed()

    # Ícono del carrito
    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    assert carrito.is_displayed()

    print("Menú, filtros y carrito presentes ✅")