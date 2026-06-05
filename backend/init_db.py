import sqlite3
import os

def init_database():
    db_path = 'makeup.db'
    
    # Connect to SQLite database (creates the file if it doesn't exist)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create companies table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS companies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    ''')
    
    # Create products table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            company_id INTEGER,
            FOREIGN KEY (company_id) REFERENCES companies (id)
        )
    ''')
    
    # Clear existing data to avoid duplicates
    cursor.execute('DELETE FROM products')
    cursor.execute('DELETE FROM companies')
    
    # Sample companies
    companies = [
        ("Velvet Nebula",),
        ("Ethereal Bloom",),
        ("Astro Glaze",),
        ("Chroma Core",)
    ]
    
    cursor.executemany('INSERT INTO companies (name) VALUES (?)', companies)
    
    # Get the inserted company IDs
    cursor.execute('SELECT id, name FROM companies')
    company_rows = cursor.fetchall()
    company_map = {name: id for id, name in company_rows}
    
    # Sample products linked to companies
    products = [
        # Velvet Nebula
        ("lipstick", company_map["Velvet Nebula"]),
        ("eyeshadow", company_map["Velvet Nebula"]),
        ("mascara", company_map["Velvet Nebula"]),
        ("shades", company_map["Velvet Nebula"]),
        
        # Ethereal Bloom
        ("blush", company_map["Ethereal Bloom"]),
        ("foundation", company_map["Ethereal Bloom"]),
        ("concealer", company_map["Ethereal Bloom"]),
        ("shades", company_map["Ethereal Bloom"]),
        
        # Astro Glaze
        ("lip gloss", company_map["Astro Glaze"]),
        ("highlighter", company_map["Astro Glaze"]),
        ("eyeshadow", company_map["Astro Glaze"]),
        ("shades", company_map["Astro Glaze"]),
        
        # Chroma Core
        ("eyeliner", company_map["Chroma Core"]),
        ("mascara", company_map["Chroma Core"]),
        ("lipstick", company_map["Chroma Core"]),
        ("shades", company_map["Chroma Core"])
    ]
    
    cursor.executemany('INSERT INTO products (name, company_id) VALUES (?, ?)', products)
    
    # Commit changes and close
    conn.commit()
    conn.close()
    print("Database initialized successfully with sample data!")

if __name__ == '__main__':
    init_database()
