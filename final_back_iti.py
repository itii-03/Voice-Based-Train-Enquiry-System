import sqlite3

def connect():
    conn=sqlite3.connect("train.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTs train (id INTEGER PRIMARY KEY , name TEXT , source TEXT , currentstatus TEXT, Destination TEXT , ETA TEXT , ETD TEXT)")
    conn.commit()
    conn.close()
def insert(name,source,currentstatus,Destination,ETA,ETD):
    #from back import calculation
    conn=sqlite3.connect("train.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO train VALUES (NULL, ?,?,?,?,?,?)",(name,source,currentstatus,Destination,ETA,ETD))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("train.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM train")
    row=cur.fetchall()
    conn.close()
    return row

def search(name="",source="",currentstatus="",ETA="",Destination="",ETD=""):
    conn=sqlite3.connect("train.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM train WHERE name=? OR source=? OR currentstatus=?  OR  ETA=?  OR  Destination=?  OR  ETD=?",(name,source,currentstatus,ETA,Destination,ETD))
    row=cur.fetchall()
    conn.close()
    return row

def delete(id):
    conn=sqlite3.connect("train.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM train  where id=?",(id,))
    conn.commit()
    conn.close()

def update(id,name,source,currentstatus,ETA,Destination,ETD):
    from back import calculation
    conn=sqlite3.connect("train.db")
    cur=conn.cursor()
    cur.execute("UPDATE train SET name=? ,source=? , currentstatus=? ,  ETA=? , Destination=? , ETD=? where id=?",(name,source,currentstatus,ETA,Destination,ETD,id))
    conn.commit()
    conn.close()



connect()
