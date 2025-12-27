import subprocess
import os
from agents.environment_agent import EnvironmentAgent
from agents.database_agent import DatabaseAgent
from agents.core_apps_agent import CoreAppsAgent

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
        db_agent = DatabaseAgent(super_user="postgres", super_password="postgres")
        db_user, db_pass = db_agent.create_system_user()
        db_name = db_agent.create_db(db_user=db_user)
        db_agent.init_odoo_db(db_name, admin_password="admin123")

        # 4. Core Apps
        apps = CoreAppsAgent(db_name, "admin123")
        apps.install_for_business(business)
