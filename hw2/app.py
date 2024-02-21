import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


app = Flask(__name__)

@app.route("/")
def index():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM Users').fetchall()
    conn.close()
    return render_template('index.html', users=users)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == "POST":
        name = request.form["name"]
        id = request.form["id"]
        points = request.form["points"]
        
        conn = get_db_connection()
        conn.execute("INSERT INTO users (name, id, points) VALUES (?, ?, ?)", (name, id, points))
        conn.commit()
        conn.close()
        return redirect(url_for("index"))
    return render_template('create.html')

@app.route('/delete/<int:id>', methods=('GET', 'POST'))
def delete(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM users WHERE id = ?",(id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=('GET', 'POST'))
def update(id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (id,)).fetchone()

    if request.method == "POST":
        name = request.form['name']
        points = request.form['points']

        conn.execute('UPDATE users SET name = ?, points = ? WHERE id = ?', (name, points, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    return render_template('update.html', user=user)