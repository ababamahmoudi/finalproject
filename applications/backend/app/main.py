from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .db import SessionLocal, engine
from . import models, crud
from .redis_client import get_cached_json, set_cached_json

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Seed products
@app.on_event("startup")
def on_startup():
    db = SessionLocal()
    crud.seed_products_if_empty(db)
    db.close()

# Products endpoint with Redis caching
@app.get("/products")
def list_products(db: Session = Depends(get_db)):
    cache_key = "products"

    cached = get_cached_json(cache_key)
    if cached:
        return cached

    products = crud.get_products(db)
    products_json = [p.__dict__ for p in products]

    for p in products_json:
        p.pop("_sa_instance_state", None)

    set_cached_json(cache_key, products_json, ttl_seconds=30)

    return products_json


@app.get("/products/{product_id}")
def get_product_detail(product_id: int, db: Session = Depends(get_db)):
    cache_key = f"product:{product_id}"

    cached = get_cached_json(cache_key)
    if cached:
        return cached

    product = crud.get_product(db, product_id)
    if not product:
        return {"error": "Product not found"}

    product_json = product.__dict__
    product_json.pop("_sa_instance_state", None)

    set_cached_json(cache_key, product_json, ttl_seconds=30)

    return product_json
