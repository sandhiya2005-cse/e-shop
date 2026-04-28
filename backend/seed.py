import os
import random
from database import SessionLocal, engine
import models

# Recreate tables to apply fresh seed
models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)
db = SessionLocal()

print("Seeding database with 5000 perfectly matched realistic products...")

# To fix the image-name mismatch, we strictly map the noun to the exact matching Unsplash image.
product_types = [
    {"noun": "Headphones", "category": "Electronics", "price": (2000, 25000), "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&q=80&w=500"},
    {"noun": "Watch", "category": "Accessories", "price": (3000, 50000), "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&q=80&w=500"},
    {"noun": "Sneakers", "category": "Apparel", "price": (1500, 12000), "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&q=80&w=500"},
    {"noun": "Camera", "category": "Electronics", "price": (15000, 150000), "image": "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?auto=format&fit=crop&q=80&w=500"},
    {"noun": "Stool", "category": "Home", "price": (500, 3000), "image": "https://images.unsplash.com/photo-1503602642458-232111445657?auto=format&fit=crop&q=80&w=500"},
    {"noun": "Earbuds", "category": "Electronics", "price": (1000, 15000), "image": "https://images.unsplash.com/photo-1583394838336-acd977736f90?auto=format&fit=crop&q=80&w=500"},
    {"noun": "Wireless Headphones", "category": "Electronics", "price": (4000, 30000), "image": "https://images.unsplash.com/photo-1484704849700-f032a568e944?auto=format&fit=crop&q=80&w=500"},
    {"noun": "Reading Glasses", "category": "Accessories", "price": (500, 3000), "image": "https://images.unsplash.com/photo-1505739998589-00fc191ce01d?auto=format&fit=crop&q=80&w=500"},
    {"noun": "Sunglasses", "category": "Accessories", "price": (1000, 8000), "image": "https://images.unsplash.com/photo-1572635196237-14b3f281503f?auto=format&fit=crop&q=80&w=500"},
    {"noun": "Running Shoes", "category": "Apparel", "price": (2000, 15000), "image": "https://images.unsplash.com/photo-1608231387042-66d1773070a5?auto=format&fit=crop&q=80&w=500"},
    {"noun": "Classic Sneakers", "category": "Apparel", "price": (1000, 8000), "image": "https://images.unsplash.com/photo-1460353581641-37baddab0fa2?auto=format&fit=crop&q=80&w=500"},
    {"noun": "Smart Watch", "category": "Accessories", "price": (5000, 40000), "image": "https://images.unsplash.com/photo-1546868871-7041f2a55e12?auto=format&fit=crop&q=80&w=500"},
    {"noun": "Water Bottle", "category": "Outdoors", "price": (200, 1500), "image": "https://images.unsplash.com/photo-1602143407151-7111542de6e8?auto=format&fit=crop&q=80&w=500"},
    {"noun": "Perfume", "category": "Beauty", "price": (2000, 10000), "image": "https://images.unsplash.com/photo-1584916201218-f4242ceb4809?auto=format&fit=crop&q=80&w=500"},
    {"noun": "Sweater", "category": "Apparel", "price": (1000, 5000), "image": "https://images.unsplash.com/photo-1610824352934-c10d87b700cc?auto=format&fit=crop&q=80&w=500"},
    {"noun": "Backpack", "category": "Accessories", "price": (800, 4000), "image": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?auto=format&fit=crop&q=80&w=500"},
    {"noun": "Coffee Mug", "category": "Home", "price": (200, 1000), "image": "https://images.unsplash.com/photo-1514228742587-6b1558fcca3d?auto=format&fit=crop&q=80&w=500"},
    {"noun": "Denim Jeans", "category": "Apparel", "price": (1200, 6000), "image": "https://images.unsplash.com/photo-1542272604-787c3835535d?auto=format&fit=crop&q=80&w=500"},
    {"noun": "Winter Jacket", "category": "Apparel", "price": (3000, 12000), "image": "https://images.unsplash.com/photo-1551028719-00167b16eac5?auto=format&fit=crop&q=80&w=500"},
    {"noun": "Office Desk", "category": "Home", "price": (5000, 25000), "image": "https://images.unsplash.com/photo-1518455027359-f3f8164ba6bd?auto=format&fit=crop&q=80&w=500"},
]

adjectives = ["Awesome", "Sleek", "Ergonomic", "Rustic", "Intelligent", "Gorgeous", "Incredible", "Practical", "Modern", "Vintage", "Minimalist", "Elegant", "Premium", "Comfortable", "Stylish", "Breathable", "Waterproof", "Designer", "Classic", "Trendy", "Luxury", "Handcrafted", "Casual", "Formal", "Durable", "Lightweight", "Heavy-Duty", "Professional", "Adjustable", "Compact", "High-Performance", "Ultra-HD", "Noise-Cancelling", "Wireless", "Smart", "Bluetooth", "Portable"]
brands = ["Sony", "Samsung", "Apple", "Nike", "Adidas", "Puma", "IKEA", "Bose", "LG", "HP", "Dell", "Lenovo", "Asus", "Garmin", "Under Armour", "Reebok", "North Face", "Columbia", "Logitech", "Razer", "Generic", "Evergreen", "Urban", "TechPro", "StyleMax"]

# Generate exactly 5000 unique products
generated_names = set()
products_to_insert = []
target_count = 5000

while len(products_to_insert) < target_count:
    p_type = random.choice(product_types)
    brand = random.choice(brands)
    adj = random.choice(adjectives)
    
    # E.g. "Sony Sleek Headphones"
    product_name = f"{brand} {adj} {p_type['noun']}"
    
    if product_name not in generated_names:
        generated_names.add(product_name)
        
        # Add a random variant or model number to ensure uniqueness if we run out of pure combinations
        if len(generated_names) > 3500:
            product_name += f" - Model {random.randint(10, 9999)}"
            generated_names.add(product_name)
        
        # Calculate realistic price based on category limits
        price = round(random.uniform(p_type["price"][0], p_type["price"][1]), 2)
        
        description = f"Experience the best with the {product_name}. This {p_type['category'].lower()} item features top-tier {adj.lower()} design. Perfect for your daily needs."
        
        prod = models.Product(
            name=product_name,
            description=description,
            price=price,
            image_url=p_type['image']
        )
        products_to_insert.append(prod)

# Batch insert for speed
print(f"Executing batch insert for {len(products_to_insert)} perfectly matched products...")
db.add_all(products_to_insert)
db.commit()

print(f"Successfully generated and inserted 5,000 realistic and matched products into the database!")
db.close()
