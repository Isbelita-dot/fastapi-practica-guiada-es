
from fastapi import FastAPI

# Create the FastAPI application.
app = FastAPI(
    title="My First API",
    description="Guided practice: FastAPI endpoints",
    version="1.0.0",
)


# ==================================================
# PASO 1: Endpoint GET inicial
# Este bloque ya está activo.
# ==================================================

@app.get("/")
def read_root():
    """Return a welcome message."""
    return {"message": "My first API is working!"}


# ==================================================
# PASO 2: Parámetro de ruta (path parameter)
#
# Descomenta todas las líneas de este bloque.
# Después guarda el archivo y prueba /docs.
# ==================================================

# @app.get("/products/{product_id}")
# def get_product(product_id: int):
#     """Return the requested product identifier."""
#     return {
#         "product_id": product_id,
#         "message": "You requested a product",
#     }


# ==================================================
# PASO 3: Parámetro de consulta (query parameter)
#
# Descomenta todas las líneas de este bloque
# después de completar el paso 2.
# ==================================================

# @app.get("/products/{product_id}/search")
# def search_product(
#     product_id: int,
#     query: str | None = None
# ):
#     """Receive an optional search query."""
#     return {
#         "product_id": product_id,
#         "query": query,
#         "message": "Search received",
#     }