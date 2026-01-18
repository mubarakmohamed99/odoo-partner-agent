import subprocess
import os
from dotenv import load_dotenv
from agents.environment_agent import EnvironmentAgent
from agents.database_agent import DatabaseAgent
from agents.core_apps_agent import CoreAppsAgent

# Load environment variables
load_dotenv()

class Orchestrator:

    def setup_odoo(self, business):
        # 1. Environment
        env = EnvironmentAgent()
        env.run()

        # 2. Start Odoo server
        python = os.path.join("workspace", "venv", "Scripts", "python")
        subprocess.Popen(
            f"{python} workspace/odoo/odoo-bin -c workspace/odoo.conf",
            shell=True
        )

        # 3. Database Agent (auto-create user & DB)
        super_user = os.getenv("POSTGRES_USER", "postgres")
        super_password = os.getenv("POSTGRES_PASSWORD", "postgres")
        db_agent = DatabaseAgent(super_user=super_user, super_password=super_password)
        
        db_user = os.getenv("ODOO_DB_USER", "odoo_agent")
        db_password = os.getenv("ODOO_DB_PASSWORD", "agent123")
        db_user, db_pass = db_agent.create_system_user(db_user=db_user, db_password=db_password)
        
        db_name = os.getenv("ODOO_DB_NAME", "odoo_db")
        db_name = db_agent.create_db(db_name=db_name, db_user=db_user)
        
        admin_password = os.getenv("ODOO_ADMIN_PASSWORD", "admin123")
        db_agent.init_odoo_db(db_name, admin_password=admin_password)

        # 4. Core Apps
        apps = CoreAppsAgent(db_name, admin_password)
        apps.install_for_business(business)
