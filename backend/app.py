from flask import Flask, request, jsonify       
#Request--- Allows Flask to read data sent by React.
#Jsonify---Python objects into JSON for react
from flask_cors import CORS
#CORS is used for letting react and flask talk.
#FLASK AND REACT has different servers Bbrowser can blovk them... this is called SAME ORIGIN POLICY
import sqlite3
import os


app = Flask(__name__)
# Enable CORS for requests from the React application
CORS(app)

DB_PATH = os.path.join(os.path.dirname(__file__), 'makeup.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/search', methods=['GET'])
def search_companies():
    query = request.args.get('q', '').strip().lower()
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if not query:
        # If no query is provided, return all companies
        cursor.execute('SELECT name FROM companies')
        rows = cursor.fetchall()
    else:
        # Search for companies that have products matching the query, or matching company name
        # Using a JOIN and LIKE to filter dynamically
        sql_query = """
            SELECT DISTINCT c.name 
            FROM companies c
            LEFT JOIN products p ON c.id = p.company_id
            WHERE LOWER(c.name) LIKE ? OR LOWER(p.name) LIKE ?
        """
        search_pattern = f"%{query}%"
        cursor.execute(sql_query, (search_pattern, search_pattern))
        rows = cursor.fetchall()
        
    conn.close()
    
    # Extract names from the query results
    companies_list = [row['name'] for row in rows]
    return jsonify(companies_list)

if __name__ == '__main__':
    # Run the server on port 5000
    app.run(debug=True, port=5000)
