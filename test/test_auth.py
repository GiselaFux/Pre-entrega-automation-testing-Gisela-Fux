import pytest
from utils.auth_funciones import register, login


@pytest.mark.parametrize("username, password, expected", [ 
    ("", "", "El nombre de usuario y la contraseña no pueden estar vacíos."),
    ("", "secret_sauce", "El nombre de usuario no puede estar vacío."),
    ("standard_user", "", "La contraseña no puede estar vacía."),
    ("standard_user", "short", "La contraseña debe tener al menos 6 caracteres."),
    (123, "secret_sauce", "El nombre de usuario debe ser una cadena de texto."),
])
def test_register(username, password, expected):
    assert register(username, password) == expected


@pytest.mark.parametrize("username, password, expected", [ 
    ("standard_user", "secret_sauce", "https://www.saucedemo.com/inventory.html"),
    ("standard_user", "wrong_password", "Nombre de usuario o contraseña incorrectos."),
    ("locked_out_user", "secret_sauce", "Usuario bloqueado"),
    ("performance_glitch_user", "secret_sauce", "Usuario con problemas de rendimiento"),
    ("problem_user", "secret_sauce", "Usuario con problemas"),
    ("visual_user", "secret_sauce", "Usuario con problemas visuales"),
    ("error_user", "secret_sauce", "Usuario con problemas de error"),
])
def test_login(username, password, expected):
    # Register a user first (si test_login se ejecuta antes que test_register, el usuario no estará registrado, por lo que se registra aquí)
    register("standard_user", "secret_sauce")

    # Test login
    assert login(username, password) == expected