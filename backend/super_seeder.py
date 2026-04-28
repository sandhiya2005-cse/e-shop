import random
from database import SessionLocal, engine
import models

# Wipe current db items
models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)
db = SessionLocal()

brands = ["Apple", "Samsung", "Sony", "Bose", "Sennheiser", "LG", "Panasonic", "Dell", "HP", "Lenovo", "Acer", "Asus", "Microsoft", "Xiaomi", "OnePlus", "Realme", "Nike", "Adidas", "Puma", "Reebok"]
categories = ["Laptop", "Smartphone", "Smart TV", "Wireless Headphones", "Earbuds", "Smartwatch", "Digital Camera", "Gaming Console", "Monitor", "Refrigerator", "Washing Machine", "Air Conditioner", "Backpack", "Running Shoes", "Desk"]
adjectives = ["Pro", "Max", "Ultra", "Lite", "Plus", "Edition", "Gaming", "Wireless", "Smart", "4K", "8K", "Mini", "Air", "Fold", "Flip", "Essential", "V2", "Elite", "Pro Max", "Plus Ultra"]
colors = ["Space Gray", "Midnight Black", "Alpine White", "Pacific Blue", "Rose Gold", "Titanium", "Graphite", "Carbon", "Emerald", "Platinum", "Ruby Red"]
images = [
    "https://images.unsplash.com/photo-1695048133142-1a20484d2569?auto=format&fit=crop&q=80&w=400",
    "https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?auto=format&fit=crop&q=80&w=400",
    "https://images.unsplash.com/photo-1593784991095-a205069470b6?auto=format&fit=crop&q=80&w=400",
    "https://images.unsplash.com/photo-1626806787426-edcc98a2fdff?auto=format&fit=crop&q=80&w=400",
    "https://images.unsplash.com/photo-1593642632823-8f785ba67e45?auto=format&fit=crop&q=80&w=400",
    "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&q=80&w=400",
    "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?auto=format&fit=crop&q=80&w=400"
]

products_list = []
generated_names = set()

for i in range(5000):
    brand = random.choice(brands)
    category = random.choice(categories)
    adjective = random.choice(adjectives)
    color = random.choice(colors)
    
    # ensure it's strictly unique!
    name = f"{brand} {category} {adjective} ({color})"
    counter = 2
    while name in generated_names:
        name = f"{brand} {category} {adjective} ({color}) Gen {counter}"
        counter += 1
        
    generated_names.add(name)
    
    price = round(random.uniform(999, 249999), 0)
    image_url = f"https://picsum.photos/seed/{i+1}/400/400"
    desc = f"Experience the incredible power of the {brand} {category}. Featuring industry-leading {adjective.lower()} performance bundled into a stunning {color} finish. Product ID: #{i+1000}"
    
    p = models.Product(name=name, description=desc, price=price, image_url=image_url)
    products_list.append(p)

chunk_size = 500
for i in range(0, 5000, chunk_size):
    db.bulk_save_objects(products_list[i:i+chunk_size])
    db.commit()

print(f"Successfully generated and inserted {len(products_list)} UNIQUE and DIFFERENT products into the database!")
db.close()
