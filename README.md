
# Práctica guiada: primera API con FastAPI

## Objetivos

Al finalizar la práctica podrás:

- Crear una aplicación básica con FastAPI.
- Definir endpoints GET.
- Utilizar parámetros de ruta y de consulta.
- Ejecutar una API con Uvicorn.
- Probar endpoints mediante Swagger UI.

## Requisitos

- Python 3.10 o superior.
- Git.
- Un editor de código, como VS Code.

## 1. Clonar el repositorio

Copia la URL del repositorio de GitHub y ejecuta:

```bash
git clone URL_DE_TU_REPOSITORIO
cd fastapi-practica-guiada-es
```

Sustituye `URL_DE_TU_REPOSITORIO` por la URL real del repositorio.

## 2. Crear un entorno virtual

En Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

En macOS o Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Instalar las dependencias

```bash
python -m pip install -r requirements.txt
```

## 4. Ejecutar la aplicación

```bash
uvicorn main:app --reload
```

Abre en el navegador:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/docs

## 5. Seguir los pasos

Abre `main.py`.

1. Comprueba el endpoint inicial.
2. Descomenta el bloque del paso 2.
3. Guarda el archivo y prueba el endpoint en `/docs`.
4. Descomenta el bloque del paso 3.
5. Guarda el archivo y prueba las dos formas de consulta.

### Pruebas

Endpoint inicial:

`GET /`

Parámetro de ruta:

`GET /productos/7`

Parámetro de ruta y de consulta:

`GET /productos/7/buscar?buscar=teclado`

Sin parámetro de consulta:

`GET /productos/7/buscar`

## Conceptos clave

- **Endpoint:** ruta y método HTTP que permiten acceder a una operación.
- **GET:** método utilizado habitualmente para consultar información.
- **Path parameter:** valor incluido en la ruta.
- **Query parameter:** valor enviado después del símbolo `?`.
- **Swagger UI:** interfaz interactiva disponible en `/docs`.

## Referencias

- https://fastapi.tiangolo.com/
- https://github.com/fastapi/fastapi