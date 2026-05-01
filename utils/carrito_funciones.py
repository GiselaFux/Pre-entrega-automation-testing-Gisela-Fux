
def agregar_productos(carrito,producto):
    precio = producto.get("precio")

    if precio == 0.0:
        
        raise ValueError(
            f"El producto '{producto.get('nombre')}' no tiene el precio actualizado (0.0)"
        )
    carrito.append(producto)
    return carrito

""" carrito = []
carrito= agregar_productos(carrito,{"nombre": "Producto1", "precio": 10.0})
carrito= agregar_productos(carrito,{"nombre": "Producto2", "precio": 20.0})
print(carrito)  """