import xmlrpc.client

class CoreAppsAgent:

    def __init__(self, db, password):
        self.db = db
        self.password = password
        self.url = "http://localhost:8069"

        common = xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/common")
        self.uid = common.authenticate(db, "admin", password, {})
        self.models = xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/object")

    def install(self, module):
        ids = self.models.execute_kw(
            self.db, self.uid, self.password,
            "ir.module.module", "search",
            [[("name", "=", module)]]
        )
        if ids:
            self.models.execute_kw(
                self.db, self.uid, self.password,
                "ir.module.module", "button_immediate_install",
                [ids]
            )

    def install_for_business(self, business):
        mapping = {
            "Retail": ["sale", "stock", "account"],
            "Services": ["crm", "project", "hr_timesheet"],
            "HR": ["hr", "hr_holidays"]
        }
        for module in mapping.get(business, []):
            self.install(module)
