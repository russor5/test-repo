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


@app.route('/test')
def test():

    return jsonify("results")

if __name__ == '__main__':
    app.run(debug=True, port=8090)