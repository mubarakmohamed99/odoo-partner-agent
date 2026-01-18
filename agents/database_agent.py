import psycopg2
from psycopg2 import sql
import xmlrpc.client
import time
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class DatabaseAgent:

    def __init__(self, super_user="postgres", super_password="postgres"):
        self.super_user = super_user
        self.super_password = super_password
        self.host = os.getenv("POSTGRES_HOST", "localhost")
        self.port = int(os.getenv("POSTGRES_PORT", "5432"))

    def create_system_user(self, db_user="odoo_agent", db_password="agent123"):
        """Create PostgreSQL user if it does not exist"""
        try:
            conn = psycopg2.connect(
                dbname="postgres",
                user=self.super_user,
                password=self.super_password,
                host=self.host,
                port=self.port
            )
            conn.autocommit = True
            cur = conn.cursor()
            cur.execute("SELECT 1 FROM pg_roles WHERE rolname=%s", (db_user,))
            if not cur.fetchone():
                # Use safe identifier quoting to prevent SQL injection
                cur.execute(
                    sql.SQL("CREATE USER {} WITH PASSWORD %s SUPERUSER").format(
                        sql.Identifier(db_user)
                    ),
                    (db_password,)
                )
            cur.close()
            conn.close()
        except Exception as e:
            print(f"⚠️ Could not create DB user: {e}")
        return db_user, db_password

    def create_db(self, db_name="odoo_db", db_user="odoo_agent"):
        """Create a new database if it does not exist"""
        try:
            conn = psycopg2.connect(
                dbname="postgres",
                user=self.super_user,
                password=self.super_password,
                host=self.host,
                port=self.port
            )
            conn.autocommit = True
            cur = conn.cursor()
            cur.execute("SELECT 1 FROM pg_database WHERE datname=%s", (db_name,))
            if not cur.fetchone():
                # Use safe identifier quoting to prevent SQL injection
                cur.execute(
                    sql.SQL("CREATE DATABASE {} OWNER {}").format(
                        sql.Identifier(db_name),
                        sql.Identifier(db_user)
                    )
                )
            cur.close()
            conn.close()
        except Exception as e:
            print(f"⚠️ Could not create database: {e}")
        return db_name

    def init_odoo_db(self, db_name="odoo_db", admin_password="admin123"):
        """Initialize Odoo DB via XML-RPC"""
        time.sleep(15)  # wait for Odoo server to start
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
