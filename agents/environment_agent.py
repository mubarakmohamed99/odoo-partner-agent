import os
import subprocess
import sys

BASE_DIR = os.path.abspath("workspace")
ODOO_VERSION = "17.0"
ODOO_GIT = "https://github.com/odoo/odoo.git"

class EnvironmentAgent:

    def run(self):
        self.create_workspace()
        self.create_virtualenv()
        self.clone_odoo()
        self.install_dependencies()
        self.create_addons_dirs()
        self.create_config()

    def run_cmd(self, cmd, cwd=None):
        subprocess.check_call(cmd, shell=True, cwd=cwd)

    def create_workspace(self):
        os.makedirs(BASE_DIR, exist_ok=True)

    def create_virtualenv(self):
        venv = os.path.join(BASE_DIR, "venv")
        if not os.path.exists(venv):
            self.run_cmd(f"{sys.executable} -m venv venv", cwd=BASE_DIR)

    def clone_odoo(self):
        if not os.path.exists(os.path.join(BASE_DIR, "odoo")):
            self.run_cmd(
                f"git clone --depth 1 --branch {ODOO_VERSION} {ODOO_GIT} odoo",
                cwd=BASE_DIR
            )

    def install_dependencies(self):
        python = os.path.join(BASE_DIR, "venv", "Scripts", "python")
        self.run_cmd(f"{python} -m pip install --upgrade pip setuptools wheel")
        self.run_cmd(f"{python} -m pip install -r odoo/requirements.txt", cwd=BASE_DIR)

    def create_addons_dirs(self):
        os.makedirs(os.path.join(BASE_DIR, "addons"), exist_ok=True)
        os.makedirs(os.path.join(BASE_DIR, "custom_addons"), exist_ok=True)

    def create_config(self):
        with open(os.path.join(BASE_DIR, "odoo.conf"), "w") as f:
            f.write(f"""
[options]
addons_path = {BASE_DIR}\\odoo\\addons,{BASE_DIR}\\addons,{BASE_DIR}\\custom_addons
http_port = 8069
""")
