import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
""" from test.conftest import driver """
from utils.selenium_functions_inventory import obtener_titulo_inventario, obtener_productos, obtener_nombre_producto, obtener_nombres_productos, obtener_precio_producto, verificar_menu, verificar_filtro, verificar_carrito_icono
from utils.selenium_functions_login import hacer_login

def test_titulo_pagina_inventario(driver):
    """Verifica que el título de la sección sea 'Products'."""
    hacer_login(driver)

    titulo = obtener_titulo_inventario(driver)

    assert titulo == "Products"
    

def test_presencia_de_productos(driver):
    """Comprueba que haya al menos un producto visible en el catálogo"""
    hacer_login(driver)

    productos = obtener_productos(driver)
    assert len(productos) >= 1
    print(f"Productos encontrados: {len(productos)}")

def test_obtener_nombres_productos(driver):
    """Obtiene y lista los nombres de todos los productos visibles"""
    hacer_login(driver)

    nombres = obtener_nombres_productos(driver)

    assert len(nombres) >= 1
    print("Nombres de productos:")
    for nombre in nombres:
        print("-", nombre)
    
def test_obtener_nombres_productos_vacios(driver):
    """Verifica que los nombres de productos no estén vacíos."""
    hacer_login(driver)

    nombres = obtener_nombres_productos(driver)

    assert len(nombres) > 0

    for nombre in nombres:
        assert nombre != ""



def test_nombre_y_precio_primer_producto(driver):
    """Lista el nombre y precio del primer producto del catálogo"""
    hacer_login(driver)

    productos = obtener_productos(driver)

    primer_producto = productos[0]  #  el primer producto de la lista

    nombre = obtener_nombre_producto(primer_producto)
    precio = obtener_precio_producto(primer_producto)
    assert nombre != ""
    assert precio != ""
    print(f"Primer producto → Nombre: {nombre} | Precio: {precio}")


def test_elementos_interfaz_presentes(driver):
    """Valida que el menú y los filtros estén presentes en la página"""
    hacer_login(driver)

    # Menú hamburguesa
    
    assert verificar_menu(driver)

    # Filtro de ordenamiento
    assert verificar_filtro(driver)
    

    # Ícono del carrito
    assert verificar_carrito_icono(driver)

    print("Menú, filtros y carrito presentes ✅")