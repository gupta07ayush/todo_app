import sqlite3
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

DB_PATH = 'todos.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute('''
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0,
            created_at TEXT NOT NULL
        )
    ''')
    conn.close()

init_db()

# Rest of your routes remain the same...
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            conn = sqlite3.connect(DB_PATH)
            conn.execute("INSERT INTO todos (task, created_at) VALUES (?, ?)",
                        (task, datetime.now().strftime("%Y-%m-%d %H:%M")))
            conn.commit()
            conn.close()
        return redirect(url_for("index"))

    conn = sqlite3.connect(DB_PATH)
    todos = conn.execute("SELECT * FROM todos ORDER BY created_at DESC").fetchall()
    conn.close()
    
    return render_template("index.html", todos=todos)

# toggle and delete routes also use DB_PATH
@app.route("/toggle/<int:todo_id>")
def toggle(todo_id):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("UPDATE todos SET completed = NOT completed WHERE id = ?", (todo_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)