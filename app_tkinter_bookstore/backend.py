"""
Backend using the Sqlite3 package
"""

import sqlite3

class Database:
    
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS store (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()
    
    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO store VALUES (NULL, ?,?,?,?)", (title, author, year, isbn))
        self.conn.commit()
    
    def view_all(self):
        self.cur.execute("SELECT * FROM store")
        rows = self.cur.fetchall()
        self.conn.commit()
        return rows
        
    def search(self, title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM store WHERE title=? OR author=? OR year=? OR isbn=?",(title, author, year, isbn))
        rows = self.cur.fetchall()
        self.conn.commit()
        return rows
    
    def delete(self, id):
        self.cur.execute("DELETE FROM store WHERE id=?", (id,))
        self.conn.commit()
    
    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE store SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.conn.commit()
        
    def close_conn(self):
        self.conn.close()
        
    def __del__(self):
        self.conn.close()