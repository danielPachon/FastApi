from fastapi import FastAPI
from models import Base, engine
from routes.author_routes import router as author_router
from routes.book_routes import router as book_router
from routes.client_routes import router as client_router
from routes.rental_routes import router as rental_router
from routes.publisher_routes import router as publisher_router

# Crear todas las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(author_router, prefix="/api")
app.include_router(book_router, prefix="/api")
app.include_router(client_router, prefix="/api")
app.include_router(rental_router, prefix="/api")
app.include_router(publisher_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
