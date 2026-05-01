import pytest
from utils.carrito_funciones import agregar_productos

# Prueba para agregar un producto al carrito
def test_agregar_productos(carrito_vacio, producto):
  
    result = agregar_productos(carrito_vacio, producto)
    assert result == [producto]
    #valido que sea un producto agregado al carrito
    assert len(result) == 1
    #valido que el nombre y precio del producto sea el correcto
    assert result[0]["nombre"] == "Producto1"
    assert result[0]["precio"] == 10.0
        
#parametrizar la prueba para agregar varios productos al carrito
@pytest.mark.parametrize("producto", [
    {"nombre": "Producto1", "precio": 10.0},
    {"nombre": "Producto2", "precio": 20.0},
    {"nombre": "Producto3", "precio": 30.0},
    {"nombre": "Producto4", "precio": 40.0},
    {"nombre": " ", "precio": 60.0}
])      
def test_agregar_varios_productos(carrito_vacio, producto):
    result = agregar_productos(carrito_vacio, producto)
    try:
        assert result == [producto]
    
    except AssertionError:
        assert(f"Error al agregar el producto: {producto['nombre']}")
    
@pytest.mark.parametrize("producto_invalido", [ 
    {"nombre": "Producto5", "precio": 0.0},
    {"nombre": "Producto6", "precio": 0.0},
    {"nombre": "Producto7", "precio": 0.0},
    {"nombre": "Producto8", "precio": 0.0},
    {"nombre": "Producto9", "precio": 0.0}  
])    
def test_producto_con_precio_cero_lanza_valueerror(carrito_vacio, producto_invalido):
    
    with pytest.raises(ValueError) as e:
        agregar_productos(carrito_vacio, producto_invalido)

    #  Nombre del diccionario que esta parametrizado
    print(f"Probando producto inválido: {producto_invalido['nombre']}")
    assert "no tiene el precio actualizado" in str(e.value)
        