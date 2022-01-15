class Hats:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, hatDTO):
        self.conn.execute("""
        INSERT INTO hats (id,topping,supplier,quantity) VALUES (?,?,?,?)
        """, [hatDTO.id, hatDTO.topping, hatDTO.supplier, hatDTO.quantity])

    def query_all(self):
        c = self.conn.cursor()
        all_items = c.execute("""SELECT * FROM hats ORDER BY supplier ASC""").fetchall()
        return [HatDTO(*row) for row in all_items]

    def query_toppings(self, topping):
        c = self.conn.cursor()
        all_items = c.execute("""SELECT supplier,quantity FROM hats WHERE topping = (?)""", [topping, ])
        return all_items

    def update(self, hatDTO):
        c = self.conn.cursor()
        c.execute(f"""UPDATE hats SET quantity = {hatDTO.quantity} WHERE id = {hatDTO.id} """)

    def delete(self, hatDTO):
        c = self.conn.cursor()
        c.execute(f"""DELETE FROM hats WHERE id = {hatDTO.id}""")


class HatDTO:
    def __init__(self, hid, topping, supplier, quantity):
        self.id = hid
        self.topping = topping
        self.supplier = supplier
        self.quantity = quantity


class Suppliers:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, supplierDTO):
        self.conn.execute("""
        INSERT INTO suppliers (id,name) VALUES (?,?)
        """, [supplierDTO.id, supplierDTO.name])

    def query_all(self):
        c = self.conn.cursor()
        all_items = c.execute("""SELECT * FROM suppliers""").fetchall()
        return [SupplierDTO(*row) for row in all_items]

class SupplierDTO:
    def __init__(self, sid, name):
        self.id = sid
        self.name = name


class Orders:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, orderDTO):
        self.conn.execute("""
        INSERT INTO orders (id,location, hat) VALUES (?,?,?)
        """, [orderDTO.id, orderDTO.name, orderDTO.hat])


class OrderDTO:
    def __init__(self, oid, location, hat):
        self.id = oid
        self.name = location
        self.hat = hat
