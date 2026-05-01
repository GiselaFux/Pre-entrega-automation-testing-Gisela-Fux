# 🧪 Pre-Entrega Automation Testing

Proyecto de automatización de pruebas sobre el sitio **[saucedemo.com](https://www.saucedemo.com)**, desarrollado con Python, Pytest y Selenium WebDriver.

---

## 📌 Propósito

El objetivo de este proyecto es demostrar el uso de herramientas de automatización de pruebas para validar flujos críticos de una aplicación web real. Se automatizan los siguientes escenarios:

- ✅ Login de usuario con credenciales válidas e inválidas
- ✅ Validación del catálogo de productos
- ✅ Interacción con el carrito de compras
- ✅ Casos de borde: usuario bloqueado, contraseña vacía, precio inválido, etc.

> ⚠️ **Nota:** Los tests de Selenium WebDriver (navegación real en browser) se agregarán en la entrega final, una vez cubiertos esos contenidos en el curso.

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Versión | Uso |
|---|---|---|
| Python | 3.10+ | Lenguaje principal |
| Pytest | Latest | Framework de testing |
| pytest-html | Latest | Generación de reportes HTML |
| Selenium WebDriver | Latest | Automatización de browser *(próximamente)* |
| Git / GitHub | — | Control de versiones |

---

## Estructura del Proyecto

```
pre-entrega-automation-testing-Fux Gisela/
│
├── utils/                        # Funciones auxiliares reutilizables
│   ├── __init__.py
│   ├── auth_funciones.py         # Lógica de registro y login
│   └── carrito_funciones.py      # Lógica del carrito de compras
│
├── tests/                        # Casos de prueba
│   ├── __init__.py
│   ├── conftest.py               # Fixtures compartidos entre tests
│   ├── test_auth.py              # Tests de autenticación
│   └── test_carrito.py          # Tests del carrito
│
├── reports/                      # Reportes generados automáticamente
│   └── reporte.html              # Reporte HTML de la última ejecución
│
├── assets/                       # Recursos estáticos (estilos del reporte)
│   └── style.css
│
├── .gitignore                    # Archivos ignorados por Git
├── requirements.txt              # Dependencias del proyecto
└── README.md                     # Este archivo
```

---

##  Instalación de Dependencias

### 1. Clonar el repositorio

```bash
git clone https://github.com/[tu-usuario]/pre-entrega-automation-testing-1-GiselaFux.git
cd pre-entrega-automation-testing-1-GiselaFux
```

### 2. Crear y activar el entorno virtual

```bash
# Crear entorno virtual
python -m venv venv

# Activar en Windows
venv\Scripts\activate

# Activar en Mac/Linux
source venv/bin/activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

---

## ▶️ Cómo Ejecutar las Pruebas

### Ejecutar todos los tests

```bash
pytest tests/ -v
```

### Ejecutar un archivo de tests específico

```bash
pytest tests/test_auth.py -v
pytest tests/test_carrito.py -v
```

### Ejecutar y generar reporte HTML

```bash
pytest tests/ -v --html=reports/reporte.html
```

### Ejecutar un test específico por nombre

```bash
pytest tests/test_auth.py::test_login -v
```



##  Casos de Prueba — Autenticación (`test_auth.py`)

### `test_register` — Validaciones de registro

| Caso | Usuario | Contraseña | Resultado Esperado |
|
| Ambos vacíos | `""` | `""` | Error: usuario y contraseña vacíos |
| Usuario vacío | `""` | `secret_sauce` | Error: usuario vacío |
| Contraseña vacía | `standard_user` | `""` | Error: contraseña vacía |
| Contraseña corta | `standard_user` | `short` | Error: mínimo 6 caracteres |
| Usuario no string | `123` | `secret_sauce` | Error: debe ser texto |

### `test_login` — Validaciones de inicio de sesión

| Caso | Usuario | Resultado Esperado |
|
| Login exitoso | `standard_user` | Redirige a `/inventory.html` |
| Contraseña incorrecta | `standard_user` | Error: credenciales inválidas |
| Usuario bloqueado | `locked_out_user` | "Usuario bloqueado" |
| Usuario con glitch | `performance_glitch_user` | "Usuario con problemas de rendimiento" |
| Usuario con errores | `problem_user` | "Usuario con problemas" |



##  Casos de Prueba — Carrito (`test_carrito.py`)

| Test | Descripción |
|---|---|
| `test_agregar_productos` | Agrega un producto y valida nombre, precio y largo del carrito |
| `test_agregar_varios_productos` | Parametrizado con 5 productos distintos |
| `test_producto_con_precio_cero_lanza_valueerror` | Valida que precio `0.0` lance `ValueError` |



##  Tests con Selenium *(Próximamente)*

Los siguientes tests se agregarán en la entrega final una vez cubiertos los contenidos de Selenium en el curso:

- [ ] `test_login_selenium.py` — Login real en browser, validación de URL `/inventory.html`
- [ ] `test_catalogo_selenium.py` — Verificación de título, productos visibles, menú y filtros
- [ ] `test_carrito_selenium.py` — Agregar producto, verificar contador y contenido del carrito



##  Reporte de Ejecución

Después de correr el comando con `--html`, el reporte queda guardado en:


   reports/reporte.html
   

 Abrilo directamente en tu navegador para ver los resultados detallados de cada test.



## Autor

Gisela Fux
 Curso de Automation Testing  
 2026



