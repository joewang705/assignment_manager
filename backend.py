import sqlite3

def connect():
    conn=sqlite3.connect("assignments.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS assignment (id INTEGER PRIMARY KEY,title text, course text, due float, details text)")
    conn.commit()
    conn.close()    

def insert(title,course,due,details):
    conn=sqlite3.connect("assignments.db")
    cur=conn.cursor()
    cur.execute('INSERT INTO assignment VALUES (NULL,?,?,?,?)',(title,course,due,details))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("assignments.db")
    cur=conn.cursor()
    cur.execute('SELECT * FROM assignment')
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",course="",due="",details=""):
    conn=sqlite3.connect("assignments.db")
    cur=conn.cursor()
    cur.execute('SELECT * FROM assignment WHERE title=? OR course=? OR due=? OR details=?', (title,course,due,details))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("assignments.db")
    cur=conn.cursor()
    cur.execute('DELETE FROM assignment WHERE id=?',(id,))
    conn.commit()
    conn.close()

def update(id,title,course,due,details):
    conn=sqlite3.connect("assignments.db")
    cur=conn.cursor()
    cur.execute('UPDATE assignment SET title=?,course=?,due=?,details=? WHERE id=?',(title,course,due,details,id))
    conn.commit()
    conn.close()

connect()
