from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# SQLite database initialization
conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT)''')
conn.commit()
conn.close()

# Vulnerable endpoint
@app.route('/search')
def search():
    query = request.args.get('query')
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE name LIKE '%{}%'".format(query))
    results = c.fetchall()
    conn.close()
    return jsonify(results)

#@app.route('/')
#def health():
#    print("/")
#    return jsonify("OK")

#@app.route('/health')
#def health_check():
#    print("/health")
#    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
