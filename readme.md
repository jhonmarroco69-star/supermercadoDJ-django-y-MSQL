# supermercadoDJ

## Sistema de gestión de supermercado

**Fecha de creación:** 10 de noviembre de 2026.

### 1. Descripción del proyecto

supermercadoDJ es un proyecto de software desarrollado con Django y Python, conectado a una base de datos MySQL.

Su propósito es implementar un sistema para administrar información de un supermercado mediante una API REST, facilitando la gestión y consulta de productos, clientes, empleados y órdenes.

### 2. Tecnologías utilizadas

- Python.
- Django.
- Django REST Framework.
- MySQL.
- Git y GitHub.
- Visual Studio Code.

### 3. Funcionalidades implementadas

El proyecto cuenta con operaciones CRUD (crear, consultar, actualizar y eliminar) para los siguientes recursos:

- **Productos:** registro y administración de productos, precios, categorías y existencias.
- **Clientes:** registro y administración de información de clientes.
- **Empleados:** administración de empleados, cargos y estado de actividad.
- **Órdenes:** creación, consulta, actualización y eliminación de órdenes, con cálculo automático del total.

### 4. Requisitos previos

Para ejecutar el proyecto se necesita:

- Python instalado.
- MySQL instalado o disponible mediante Laragon.
- Git.
- Un editor de código, preferiblemente Visual Studio Code.

### 5. Descargar el proyecto

Clonar el repositorio desde GitHub:

```bash
git clone https://github.com/jhonmarroco69-star/supermercadoDJ-django-y-MSQL.git
```

Ingresar a la carpeta:

```bash
cd supermercadoDJ-django-y-MSQL
```

### 6. Crear el entorno virtual

En Windows:

```bash
python -m venv .venv
```

Activarlo:

```powershell
.venv\Scripts\Activate.ps1
```

### 7. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 8. Configurar la base de datos

Iniciar MySQL y crear una base de datos llamada:

```sql
CREATE DATABASE supermercado;
```

Crear un archivo `.env` en la carpeta principal del proyecto y configurar las siguientes variables con los datos del entorno local:

```env
DJANGO_SECRET_KEY=generar_una_clave_secreta_propia
DJANGO_DEBUG=True
DJANGO_DB_NAME=supermercado
DJANGO_DB_USER=root
DJANGO_DB_PASSWORD=
DJANGO_DB_HOST=127.0.0.1
DJANGO_DB_PORT=3306
```

**Importante:** cada usuario debe utilizar sus propias credenciales de MySQL. El archivo `.env` contiene información privada y no debe publicarse en GitHub.

### 9. Ejecutar las migraciones

Crear las tablas de la base de datos:

```bash
python manage.py migrate
```

### 10. Iniciar el servidor

```bash
python manage.py runserver
```

Abrir el navegador en:

http://127.0.0.1:8000/

### 11. Endpoints de la API REST

| Recurso | Endpoint |
|---|---|
| Productos | `/api/productos/` |
| Clientes | `/api/clientes/` |
| Empleados | `/api/empleados/` |
| Órdenes | `/api/ordenes/` |

Cada recurso permite operaciones de consulta, creación, actualización y eliminación mediante los métodos HTTP correspondientes.

### 12. Repositorio

Código fuente disponible en GitHub:

https://github.com/jhonmarroco69-star/supermercadoDJ-django-y-MSQL

---

**Proyecto académico desarrollado como parte del programa de formación Tecnólogo en Análisis y Desarrollo de Software (ADSO) del SENA.**