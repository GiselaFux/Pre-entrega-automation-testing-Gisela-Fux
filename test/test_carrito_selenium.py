from utils.selenium_functions_login import hacer_login
from utils.selenium_functions_carrito import (
    agregar_primer_producto,
    obtener_contador_carrito,
    navegar_al_carrito,
    obtener_productos_en_carrito,
    obtener_nombre_item_carrito
)


def test_agregar_primer_producto_al_carrito(driver):
    """Añade el primer producto y verifica que el contador del carrito muestre 1."""
    hacer_login(driver)

    nombre_producto = agregar_primer_producto(driver)
    contador = obtener_contador_carrito(driver)

    assert contador == "1"
    print(f"Producto agregado: '{nombre_producto}' | Badge del carrito: {contador} ✅")


def test_producto_aparece_en_carrito(driver):
    """Navega al carrito y verifica que el producto agregado esté presente."""
    hacer_login(driver)

    nombre_agregado = agregar_primer_producto(driver)
    navegar_al_carrito(driver)

    assert "/cart.html" in driver.current_url
    print("Navegación al carrito OK ✅")

    items = obtener_productos_en_carrito(driver)
    assert len(items) >= 1
    print(f"Productos en el carrito: {len(items)}")

    nombre_en_carrito = obtener_nombre_item_carrito(items[0])
    assert nombre_en_carrito == nombre_agregado
    print(f"Producto en carrito correcto → '{nombre_en_carrito}' ✅")