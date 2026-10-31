# app.py
from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the AppSec Sandbox!"

# SAST Test: SQL Injection vulnerability via raw string formatting
@app.route('/search')
def search():
    query = request.args.get('q', '')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Insecure query construction
    sql = f"SELECT * FROM users WHERE username LIKE '%{query}%'"
    cursor.execute(sql)
    results = cursor.fetchall()
    
    return str(results)

if __name__ == '__main__':
    # SAST Test: Debug mode should never be true in production
    app.run(debug=True)