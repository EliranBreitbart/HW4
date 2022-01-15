import atexit
import sqlite3
import sys

import DAOs_DTOs


class Repository:
    def __init__(self):
        self.conn = sqlite3.connect(sys.argv[4])
        self.hats = DAOs_DTOs.Hats(self.conn)  # DAO for hats table
        self.suppliers = DAOs_DTOs.Suppliers(self.conn)  # DAO for suppliers table
        self.orders = DAOs_DTOs.Orders(self.conn)  # DAO for orders table

    def close(self):
        self.conn.commit()
        self.conn.close()

    def create_tables(self):
        self.conn.executescript("""
        CREATE TABLE IF NOT EXISTS suppliers (id INT PRIMARY KEY, name TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS hats (id INT PRIMARY KEY, topping TEXT NOT NULL, supplier INT REFERENCES suppliers(id), quantity INT NOT NULL);
        CREATE TABLE IF NOT EXISTS orders (id INT PRIMARY KEY, location TEXT NOT NULL, hat INT REFERENCES hats(id));
        """)


repo = Repository()
atexit.register(repo.close)
