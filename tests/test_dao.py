"""DAO tests with a fake MySQL connection (no database server needed)."""

import orders_dao
import products_dao


class FakeCursor:
    def __init__(self, rows=None):
        self.rows, self.calls, self.lastrowid = rows or [], [], 7

    def execute(self, query, params=None):
        self.calls.append((query, params))

    def executemany(self, query, params):
        self.calls.append((query, list(params)))

    def __iter__(self):
        return iter(self.rows)

    def close(self):
        pass


class FakeConnection:
    def __init__(self, cursor):
        self._cursor, self.committed = cursor, False

    def cursor(self):
        return self._cursor

    def commit(self):
        self.committed = True


def test_delete_product_is_parameterised():
    cur = FakeCursor()
    conn = FakeConnection(cur)
    products_dao.delete_product(conn, "3")
    query, params = cur.calls[0]
    assert "%s" in query and params == (3,)
    assert conn.committed


def test_get_all_products_maps_columns():
    cur = FakeCursor(rows=[(1, "Rice", 2, 60.0, "kg")])
    out = products_dao.get_all_products(FakeConnection(cur))
    assert out == [{"product_id": 1, "name": "Rice", "uom_id": 2, "price_per_unit": 60.0, "uom_name": "kg"}]


def test_insert_order_writes_header_and_details():
    cur = FakeCursor()
    conn = FakeConnection(cur)
    order = {
        "customer_name": "Asha",
        "grand_total": 120.0,
        "order_details": [{"product_id": "1", "quantity": "2", "total_price": "120"}],
    }
    assert orders_dao.insert_order(conn, order) == 7
    assert cur.calls[1][1] == [[7, 1, 2.0, 120.0]]
    assert conn.committed
