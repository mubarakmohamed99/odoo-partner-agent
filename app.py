import streamlit as st
import os
from dotenv import load_dotenv
from orchestrator import Orchestrator

# Load environment variables from .env file
load_dotenv()

st.set_page_config(page_title="Autonomous Odoo Partner Agent")
st.title("🚀 Autonomous Odoo Partner Agent")

# Check for GitHub OAuth configuration
github_client_id = os.getenv("GITHUB_CLIENT_ID")
github_client_secret = os.getenv("GITHUB_CLIENT_SECRET")

if not github_client_id or not github_client_secret or \
   github_client_id == "Iv1.your-client-id-here" or \
   github_client_secret == "your-client-secret-here":
    st.warning("⚠️ GitHub OAuth is not configured. Please set up your credentials:")
    st.info("""
    **To configure GitHub OAuth:**
    1. Copy `.env.example` to `.env`
    2. Follow the instructions in README.md to create a GitHub OAuth App
    3. Add your Client ID and Client Secret to the `.env` file
    """)
    st.markdown("📖 [View Setup Instructions in README.md](./README.md)")
else:
    st.success("✅ GitHub OAuth is configured")

st.divider()

business = st.selectbox(
    "Select your business type:",
    ["Retail", "Services", "HR"]
)

st.write("✅ First-time deployment uses default PostgreSQL user 'odoo_agent' and DB 'odoo_db'.")

if st.button("Build My Odoo System"):
    orch = Orchestrator()
    orch.setup_odoo(business)
    st.success("🎉 Odoo is being set up! Open http://localhost:8069 after a few seconds.")
