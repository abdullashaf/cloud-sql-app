from flask import Flask
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS visits (id INTEGER PRIMARY KEY)')
    conn.execute('INSERT INTO visits DEFAULT VALUES')
    visits = conn.execute('SELECT COUNT(*) FROM visits').fetchone()[0]
    conn.close()
    return f"Cloud App Running 🚀 | Visits: {visits}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
