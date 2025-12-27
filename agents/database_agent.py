import psycopg2
import xmlrpc.client
import time

class DatabaseAgent:

    def __init__(self, pg_user, pg_password):
        self.pg_user = pg_user
        self.pg_password = pg_password

    def create_db(self, db_name):
        conn = psycopg2.connect(
            dbname="postgres",
            user=self.pg_user,
            password=self.pg_password,
            host="localhost",
            port=5432
        )
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute(f"CREATE DATABASE {db_name}")
        cur.close()
        conn.close()

    def init_odoo_db(self, db_name, admin_password):
        time.sleep(10)  # allow Odoo to boot
        common = xmlrpc.client.ServerProxy("http://localhost:8069/xmlrpc/2/common")
        common.db.create_database(
            admin_password,
            db_name,
            False,
            "admin@example.com",
            "en_US"
        )
