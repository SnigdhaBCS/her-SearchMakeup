import sqlite3
import os

def init_database():
    db_path = 'makeup.db'
    
    # Connect to SQLite database (creates the file if it doesn't exist)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create companies table
    #AUTOINCREMENT- auto. generate IDs, we dont do it manually.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS companies (
                   
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT NOT NULL UNIQUE
        )
    ''')
    
    # Create products table
    #relationship between two tables, id (from companies table) 
    # and companies_id (foreign key)
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
        ("MARS",),
        ("HUDA",),
        ("SWISS BEAUTY",),
        ("LAKME",)
    ]
    
    cursor.executemany('INSERT INTO companies (name) VALUES (?)', companies)
    
    # Get the inserted company IDs
    cursor.execute('SELECT id, name FROM companies')
    company_rows = cursor.fetchall()
    company_map = {name: id for id, name in company_rows}
    
    # Sample products linked to companies
    products = [
        # MARS
        ("lipstick", company_map["MARS"]),
        ("eyeshadow", company_map["MARS"]),
        ("mascara", company_map["MARS"]),
        ("foundation", company_map["MARS"]),
        
        # Ethereal Bloom
        ("blush", company_map["HUDA"]),
        ("foundation", company_map["HUDA"]),
        ("concealer", company_map["HUDA"]),
        ("lipgloss", company_map["HUDA"]),
        
        # Astro Glaze
        ("lip gloss", company_map["SWISS BEAUTY"]),
        ("highlighter", company_map["SWISS BEAUTY"]),
        ("eyeshadow", company_map["SWISS BEAUTY"]),
        ("shades", company_map["SWISS BEAUTY"]),
        
        # Chroma Core
        ("eyeliner", company_map["LAKME"]),
        ("mascara", company_map["LAKME"]),
        ("lipstick", company_map["LAKME"]),
        ("shades", company_map["LAKME"])
    ]
    
    cursor.executemany('INSERT INTO products (name, company_id) VALUES (?, ?)', products)
    
    # Commit changes and close
    conn.commit()
    conn.close()
    print("Database initialized successfully with data!")

if __name__ == '__main__':
    init_database()