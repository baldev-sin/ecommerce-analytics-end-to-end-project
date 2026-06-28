import psycopg2
from faker import Faker
import random
from datetime import datetime, timedelta
import pandas as pd

fake = Faker('en_IN')
random.seed(42)

# ---- DB Connection ----
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="ecommerce_analytics",
    user="postgres",
    password="postgres123"
)
cur = conn.cursor()

# ---- Config ----
REGIONS = {
    'North': ['Delhi', 'Chandigarh', 'Lucknow', 'Jaipur'],
    'South': ['Bangalore', 'Chennai', 'Hyderabad', 'Kochi'],
    'East':  ['Kolkata', 'Bhubaneswar', 'Patna', 'Guwahati'],
    'West':  ['Mumbai', 'Pune', 'Ahmedabad', 'Surat']
}

PRODUCTS = [
    ("iPhone 14", "Electronics", "Mobiles", 79999),
    ("Samsung Galaxy S23", "Electronics", "Mobiles", 69999),
    ("Sony WH-1000XM5", "Electronics", "Headphones", 29999),
    ("Dell Inspiron Laptop", "Electronics", "Laptops", 55000),
    ("HP Pavilion Laptop", "Electronics", "Laptops", 48000),
    ("Nike Air Max", "Footwear", "Sports Shoes", 8999),
    ("Adidas Ultraboost", "Footwear", "Sports Shoes", 12999),
    ("Levi's 511 Jeans", "Clothing", "Bottomwear", 3999),
    ("Allen Solly Shirt", "Clothing", "Topwear", 1999),
    ("Zara Summer Dress", "Clothing", "Dresses", 4500),
    ("Prestige Cooker", "Kitchen", "Cookware", 2499),
    ("Philips Air Fryer", "Kitchen", "Appliances", 7999),
    ("Godrej Refrigerator", "Kitchen", "Appliances", 32000),
    ("Ikea Study Table", "Furniture", "Tables", 8999),
    ("Wooden Bookshelf", "Furniture", "Storage", 5999),
    ("Yoga Mat", "Sports", "Fitness", 999),
    ("Dumbbells Set 10kg", "Sports", "Fitness", 2499),
    ("Cricket Bat SG", "Sports", "Cricket", 1800),
    ("Boat Airdopes", "Electronics", "Earbuds", 2999),
    ("Kindle Paperwhite", "Electronics", "E-Readers", 13999),
]

SHIPPING_MODES = ['Standard', 'Express', 'Same Day', 'Economy']

# ---- Insert Customers ----
print("Inserting customers...")
customer_ids = []
for i in range(500):
    region = random.choice(list(REGIONS.keys()))
    city = random.choice(REGIONS[region])
    signup = fake.date_between(start_date='-3y', end_date='-6m')
    cur.execute("""
        INSERT INTO customers (customer_name, email, city, state, region, signup_date)
        VALUES (%s, %s, %s, %s, %s, %s) RETURNING customer_id
    """, (fake.name(), fake.email(), city, region + " State", region, signup))
    customer_ids.append(cur.fetchone()[0])

# ---- Insert Products ----
print("Inserting products...")
product_ids = []
for name, cat, sub, price in PRODUCTS:
    cur.execute("""
        INSERT INTO products (product_name, category, sub_category, unit_price)
        VALUES (%s, %s, %s, %s) RETURNING product_id
    """, (name, cat, sub, price))
    product_ids.append(cur.fetchone()[0])

# ---- Insert Orders + Order Items ----
print("Inserting orders and items...")
order_counter = 1
for _ in range(2000):
    order_id = f"ORD-{order_counter:05d}"
    order_counter += 1
    customer_id = random.choice(customer_ids)
    order_date = fake.date_between(start_date='-2y', end_date='today')
    ship_date = order_date + timedelta(days=random.randint(1, 7))
    shipping_mode = random.choice(SHIPPING_MODES)

    cur.execute("""
        INSERT INTO orders (order_id, customer_id, order_date, ship_date, shipping_mode)
        VALUES (%s, %s, %s, %s, %s)
    """, (order_id, customer_id, order_date, ship_date, shipping_mode))

    # 1 to 3 items per order
    num_items = random.randint(1, 3)
    selected_products = random.sample(product_ids, num_items)
    for product_id in selected_products:
        quantity = random.randint(1, 4)
        discount = random.choice([0, 0.05, 0.10, 0.15, 0.20])
        
        cur.execute("SELECT unit_price FROM products WHERE product_id = %s", (product_id,))
        unit_price = cur.fetchone()[0]
        sale_price = round(float(unit_price) * quantity * (1 - discount), 2)

        cur.execute("""
            INSERT INTO order_items (order_id, product_id, quantity, discount, sale_price)
            VALUES (%s, %s, %s, %s, %s)
        """, (order_id, product_id, quantity, discount, sale_price))

conn.commit()
cur.close()
conn.close()
print("✅ Done! Data loaded successfully.")