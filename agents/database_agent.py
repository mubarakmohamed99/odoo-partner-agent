import psycopg2
import xmlrpc.client
import time

class DatabaseAgent:

    def __init__(self, super_user="postgres", super_password="postgres"):
        self.super_user = super_user
        self.super_password = super_password

    def create_system_user(self, db_user="odoo_agent", db_password="agent123"):
        """Creates a PostgreSQL user if it doesn't exist"""
        conn = psycopg2.connect(
            dbname="postgres",
            user=self.super_user,
            password=self.super_password,
            host="localhost",
            port=5432
        )
        conn.autocommit = True
        cur = conn.cursor()
        # Check if user exists
        cur.execute("SELECT 1 FROM pg_roles WHERE rolname=%s", (db_user,))
        if not cur.fetchone():
            cur.execute(f"CREATE USER {db_user} WITH PASSWORD '{db_password}' SUPERUSER")
        cur.close()
        conn.close()
        return db_user, db_password

    def create_db(self, db_name="odoo_db", db_user="odoo_agent"):
        """Creates the database if it doesn't exist"""
        conn = psycopg2.connect(
            dbname="postgres",
            user=self.super_user,
            password=self.super_password,
            host="localhost",
            port=5432
        )
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute("SELECT 1 FROM pg_database WHERE datname=%s", (db_name,))
        if not cur.fetchone():
            cur.execute(f"CREATE DATABASE {db_name} OWNER {db_user}")
        cur.close()
        conn.close()
        return db_name

    def init_odoo_db(self, db_name="odoo_db", admin_password="admin123"):
        """Initialize Odoo DB via XML-RPC"""
        time.sleep(10)  # wait for Odoo to start
        common = xmlrpc.client.ServerProxy("http://localhost:8069/xmlrpc/2/common")
        try:
            common.db.create_database(
                admin_password,
                db_name,
                False,
                "admin",
                "en_US"
            )
        except Exception as e:
            print(f"⚠️ Database {db_name} may already exist: {e}")
