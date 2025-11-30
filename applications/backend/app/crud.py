from sqlalchemy.orm import Session
from . import models, schemas

def get_products(db: Session, skip: int = 0, limit: int = 50):
    return db.query(models.Product).offset(skip).limit(limit).all()

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(
        name=product.name,
        description=product.description,
        price=product.price,
        sku=product.sku,
        category=product.category,
    )


    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def seed_products_if_empty(db: Session):
    count = db.query(models.Product).count()
    if count > 0:
        return

    sample_products = [
        schemas.ProductCreate(
            name="CloudMart Basic VM",
            description="Entry-level virtual machine for small workloads.",
            price=9.99,
            sku="VM-BASIC-001",
            category="Compute",
        ),
        schemas.ProductCreate(
            name="CloudMart Storage Pack",
            description="100 GB redundant cloud storage.",
            price=4.99,
            sku="STORAGE-100GB",
            category="Storage",
        ),
        schemas.ProductCreate(
            name="CloudMart Premium Support",
            description="24/7 support add-on.",
            price=19.99,
            sku="SUPPORT-24x7",
            category="Support",
        ),
    ]

    for p in sample_products:
        create_product(db, p)
