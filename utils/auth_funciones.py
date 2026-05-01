
usuarios = []

def register (username, password):
    
    #Usuario vacio contraseña vacia
    if not username and not password:
       return "El nombre de usuario y la contraseña no pueden estar vacíos."
   
   #usuario vacio contraseña correctaa
    if not username and password:
        return "El nombre de usuario no puede estar vacío."
    
    #el usuario es correcto contraseña vacia
    if username and not password:
        return "La contraseña no puede estar vacía."
   
    #usuario correcto contraseña corta
    if len(password) < 6:
        return "La contraseña debe tener al menos 6 caracteres."
    
    #usuario no es str
    if not isinstance(username, str):
        return "El nombre de usuario debe ser una cadena de texto."
  
  
#agregar usuario a la lista de usuarios 
    usuarios.append({"username": username, "password": password})
    print(f"Usuario registrado: {username} , {password}" )
    return "Usuario registrado exitosamente."

# --- Constantes del sitio ---
URL_BASE       = "https://www.saucedemo.com"
URL_INVENTARIO = "https://www.saucedemo.com/inventory.html"
URL_CARRITO    = "https://www.saucedemo.com/cart.html"

#login de usuario
def login(username, password):
    for usuario in usuarios:
        if usuario["username"] == username and usuario["password"] == password:
            return "https://www.saucedemo.com/inventory.html" # "Inicio de sesión exitoso."  
         # Usuario bloqueado
    if username == "locked_out_user" and password == "secret_sauce":
        return "Usuario bloqueado"

    # Usuario con problemas de rendimiento
    if username == "performance_glitch_user" and password == "secret_sauce":
        return "Usuario con problemas de rendimiento"

    # Usuario con problemas
    if username == "problem_user" and password == "secret_sauce":
        return "Usuario con problemas"

    # Usuario con problemas visuales
    if username == "visual_user" and password == "secret_sauce":
        return "Usuario con problemas visuales"

    # Usuario con problemas de error
    if username == "error_user" and password == "secret_sauce":
        return "Usuario con problemas de error"

    # Cualquier otra combinación
    return "Nombre de usuario o contraseña incorrectos."
   