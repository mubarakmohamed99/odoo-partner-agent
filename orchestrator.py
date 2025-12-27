import subprocess
import os
from agents.environment_agent import EnvironmentAgent
from agents.database_agent import DatabaseAgent
from agents.core_apps_agent import CoreAppsAgent

class Orchestrator:

    def setup_odoo(self, business, db_name, pg_user, pg_password, admin_password):
        # 1. Environment
        env = EnvironmentAgent()
        env.run()

        # 2. Start Odoo
        python = os.path.join("workspace", "venv", "Scripts", "python")
        subprocess.Popen(
            f"{python} workspace/odoo/odoo-bin -c workspace/odoo.conf",
            shell=True
        )

        # 3. Database
        db_agent = DatabaseAgent(pg_user, pg_password)
        db_agent.create_db(db_name)
        db_agent.init_odoo_db(db_name, admin_password)

        # 4. Core apps
        apps = CoreAppsAgent(db_name, admin_password)
        apps.install_for_business(business)
