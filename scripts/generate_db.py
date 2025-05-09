import sqlite3
import os

# Get the directory of the current script (scripts/)
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to farming.db in the data/ folder
db_path = os.path.join(script_dir, '..', 'data', 'farming.db')

# Connect to SQLite (this creates the file if it doesn't exist)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create tables
try:
    cursor.execute('''  
    CREATE TABLE crops (
        crop_id INTEGER PRIMARY KEY,
        name TEXT UNIQUE NOT NULL,
        planting_season TEXT,
        maturity_days INTEGER
    )''')

    cursor.execute('''  
    CREATE TABLE fields (
        field_id INTEGER PRIMARY KEY,
        location TEXT,
        area_hectares REAL,
        soil_ph REAL
    )''')

    cursor.execute('''  
    CREATE TABLE harvests (
        harvest_id INTEGER PRIMARY KEY,
        field_id INTEGER,
        crop_id INTEGER,
        harvest_date DATE,
        yield_tons REAL,
        FOREIGN KEY (field_id) REFERENCES fields (field_id),
        FOREIGN KEY (crop_id) REFERENCES crops (crop_id)
    )''')

    conn.commit()
    print("Database and tables created successfully.")
except sqlite3.OperationalError as e:
    print(f"Error creating tables: {e}. They may already exist.")
finally:
    conn.close()