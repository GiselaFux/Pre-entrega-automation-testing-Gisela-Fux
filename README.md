# Pre-Entrega Automation Testing

Proyecto de automatización de pruebas sobre el sitio **[saucedemo.com](https://www.saucedemo.com)**, desarrollado con Python, Pytest y Selenium WebDriver.

---

## Propósito

El objetivo de este proyecto es demostrar el uso de herramientas de automatización de pruebas para validar flujos críticos de una aplicación web real. Se automatizan los siguientes escenarios:

- ✅ Login de usuario con credenciales 
- ✅ Validación del catálogo de productos
- ✅ Interacción con el carrito de compras
- ✅ Casos de borde: usuario bloqueado, contraseña vacía, precio inválido, etc.


##  Tecnologías Utilizadas

| Tecnología | Versión | Uso |
|---|---|---|
| Python | 3.12 | Lenguaje principal |
| Pytest | 8.1.1 | Framework de testing |
| pytest-html | 4.1.1 | Generación de reportes HTML |
| Selenium WebDriver | 4.43.0 | Automatización de browser|
| Git / GitHub | — | Control de versiones |

---

## Estructura del Proyecto

```
pre-entrega-automation-testing-Fux Gisela/
│
├── utils/                               # Funciones auxiliares reutilizables
│   ├── __init__.py
    ├── selenium_functions_inventory.py  # Lógica de inventario con Selenium
    ├── selenium_functions_carrito.py    # Lógica de carrito con Selenium
    └── selenium_functions_login.py      # Lógica de login con Selenium

│
├── tests/                               # Casos de prueba
│   ├── __init__.py
│   ├── conftest.py                      # Fixtures compartidos entre tests
    ├──   test_login_selenium.py         # Tests de login Selenium
    ├──   test_carrito_selenium          # Tests de carrito Selenium
    └──   test_selenium_inventory        # Tests de inventory Selenium
│
├── reports/                      # Reportes generados automáticamente
│   └── reporte.html              # Reporte HTML de la última ejecución
├── assets/                       # Recursos estáticos (estilos del reporte)
│   └── style.css

│
├── .gitignore                    # Archivos ignorados por Git
├── venv                          # Entorno virtual 
├── requirements.txt              # Dependencias del proyecto
└── README.md                     # Este archivo
```


##  Instalación de Dependencias

### 1. Clonar el repositorio

```bash
git clone https://github.com/GiselaFux/Pre-entrega-automation-testing-Gisela-Fux/
cd Pre-entrega-automation-testing-Gisela-Fux
```

### 2. Crear y activar el entorno virtual

```bash
# Crear entorno virtual
python -m venv venv

# Activar en Windows
venv\Scripts\activate

```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
pip install selenium
pip install webdriver-manager
pip install pytest
pip install pytest-html
```

---

##  Cómo Ejecutar las Pruebas

### Ejecutar todos los tests

```bash
pytest test/ -v
```

### Ejecutar un archivo de tests específico

```bash
pytest test/test_login_selenium.py -v
pytest test/test_carrito_selenium.py -v
```

### Ejecutar y generar reporte HTML

```bash
pytest test/ -v --html=reports/reporte.html
```

### Ejecutar un test específico por nombre

```bash
pytest test/test_login_selenium.py::test_login_exitoso -v
```



##  Casos de Prueba — 

- selenium_functions_login.py --hacer_login, hacer_login_invalido, falla_intencional_screenshot
- selenium_functions_inventory.py --obtener_titulo_inventario, obtener_productos, obtener_nombre_producto, obtener_precio_producto, verificar_menu,
                                  verificar_filtro, verificar_carrito_icono
- selenium_functions_carrito.py  -- agregar_primer_producto, obtener_contador_carrito, navegar_al _carrito, obtener_productos_en _carrito,  
                                  obtener_nombre_item_carrito        
##  Tests con Selenium 

- [ ] `test_login_selenium.py` — Login real en browser, validación de URL `/inventory.html`
- [ ] `test_selenium_inventory.py` — Verificación de título, productos visibles, menú y filtros
- [ ] `test_carrito_selenium.py` — Agregar primer producto, verificar contador , navegar al carrito y contenido del carrito



##  Reporte de Ejecución

Después de correr el comando con `--html`, el reporte queda guardado en:


   reports/reporte.html
   

 Abrilo directamente en tu navegador para ver los resultados detallados de cada test.

 # En el archivo conftest.py he tenido que colocar el código que está a continuación ya que no podía hacer los test porque el gestor de contraseöas de Chrome lo toma como amenaza. El código desactiva el gestor de contraseñas de Chrome para evitar un pop-up, que me bloqueaba la pantalla.
    # "Cambia la contraseña / contraseña encontrada en filtración de datos"
    prefs = {
        "credentials_enable_service": False,    # Desactiva el servicio de gestión de contraseñas.Evita que Chrome intente ofrecerte guardar contraseña.
        "profile.password_manager_enabled": False,   # Deshabilita el gestor de contraseñas del perfil actual de Chrome.Evita el pop-up que pregunta si quieres guardar la contraseña.
        "profile.password_manager_leak_detection": False # Desactiva la función de detección de fugas de contraseñas.Evita que aparezca el pop-up que me frena los tests.
    }
    options.add_experimental_option("prefs", prefs) # Le dice a Chrome: “arrancá con estas preferencias (prefs) ya configuradas”, por ejemplo desactivar el gestor de contraseñas y sus avisos.


# Busque cómo hacer para capturar los errores y leí sobre los Hooks.Este Hook: captura screenshot si el test falla. A contimuacion la explicación: 

rgb(31, 123, 214) pytest_runtest_makereport(item, call):    # Define el hook que pytest ejecuta al generar el reporte de cada test (item = el test,
                                                                 call = la ejecución del test)
    outcome = yield                                           #  Usa el patrón “hookwrapper”: permite que se ejecute el resto de la lógica de   
                                                                pytest primero y luego continua aquí con el resultado.       
    report = outcome.get_result()                             # Obtiene el objeto de reporte del test (con info: setup, call, teardown, y si pasó o
                                                                 falló)
    if report.when == "call" and report.failed:               # Se ejecuta solo en la fase de call (cuando se está ejecutando el cuerpo del test) y 
                                                                solo si el test falló.      
    driver = item.funcargs.get("driver")                      # Obtiene el driver de Selenium que se inyectó al 
                                                                test (del fixture)
    if driver:                                                # Si lo encuentra    
    carpeta = os.path.join("reports", "screenshots")          # Arma la ruta de la carpeta donde se guardarán las 
                                                                screenshots        
    os.makedirs(carpeta, exist_ok=True)                       # Crea la carpeta reports/screenshots si no existe, sin dar error si ya 
                                                                existe 
    timestamp = time.strftime               ("%Y%m%d_%H%M%S") # Genera una marca de tiempo tipo 20260508_235959                                                                          nombre = item.name.replace(" ", "_")                      #Toma el nombre del test y reemplaza los espacios por _ para que sirva como parte del nombre del archivo.               ruta = os.path.join(carpeta, f"FALLO_{nombre}_{timestamp}.png")  # Define la ruta completa del archivo: reports/screenshots/FALLO_nombre_del_test_HHMMSS.png.                                driver.save_screenshot(ruta)                              # Guarda una captura de pantalla del estado actual del navegador cuando el test falló.                                                                                                                                                                                        


## Autor

Gisela Fux
Curso de Automation Testing  
2026



