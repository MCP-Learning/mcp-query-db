import sqlite3
import random
import os
from datetime import datetime, timedelta

# Get the directory of the current script (scripts/)
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to farming.db in the data/ folder
db_path = os.path.join(script_dir, '..', 'data', 'farming.db')

# Connect to SQLite using the absolute path
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Insert crops
crops = [
    ('Potato', 'Spring', 90),
    ('Tomato', 'Summer', 60),
    ('Carrot', 'Spring', 70),
    ('Corn', 'Summer', 120),
    ('Wheat', 'Autumn', 150)
]
cursor.executemany("INSERT INTO crops (name, planting_season, maturity_days) VALUES (?, ?, ?)", crops)

# Insert fields
fields = [
    ('Field A', 5.5, 6.2),
    ('Field B', 3.8, 5.8),
    ('Field C', 7.2, 6.5),
    ('Field D', 4.0, 7.0),
    ('Field E', 6.3, 6.0)
]
cursor.executemany("INSERT INTO fields (location, area_hectares, soil_ph) VALUES (?, ?, ?)", fields)

# Generate 100 harvest records
for _ in range(100):
    crop_id = random.randint(1, 5)
    field_id = random.randint(1, 5)
    
    # Simulate yield based on soil pH and crop type
    base_yield = {
        1: 20,  # Potato
        2: 10,  # Tomato
        3: 15,  # Carrot
        4: 30,  # Corn
        5: 40   # Wheat
    }[crop_id]
    
    # Adjust yield by soil pH (optimal pH ~6.0–7.0)
    soil_ph = cursor.execute("SELECT soil_ph FROM fields WHERE field_id=?", (field_id,)).fetchone()[0]
    yield_tons = round(base_yield * (soil_ph / 6.5) * random.uniform(0.8, 1.2), 2)
    
    harvest_date = datetime.now() - timedelta(days=random.randint(0, 30))
    cursor.execute(
        "INSERT INTO harvests (field_id, crop_id, harvest_date, yield_tons) VALUES (?, ?, ?, ?)",
        (field_id, crop_id, harvest_date.strftime('%Y-%m-%d'), yield_tons)
    )

conn.commit()
conn.close()