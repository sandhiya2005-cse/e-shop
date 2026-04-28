from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models

from database import engine
from routers import users, products, orders, chatbot
# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="E-Commerce API")

# Configure CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows all origins
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods
    allow_headers=["*"], # Allows all headers
)

app.include_router(users.router)
app.include_router(products.router)
app.include_router(orders.router)
app.include_router(chatbot.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the E-Commerce API"}
