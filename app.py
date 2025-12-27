import streamlit as st
from orchestrator import Orchestrator

st.set_page_config(page_title="Autonomous Odoo Partner Agent")
st.title("🚀 Autonomous Odoo Partner Agent")

business = st.selectbox(
    "Select your business type:",
    ["Retail", "Services", "HR"]
)

st.write("✅ First-time deployment uses default database and user.")
if st.button("Build My Odoo System"):
    orch = Orchestrator()
    orch.setup_odoo(business)
    st.success("🎉 Odoo is being set up! Open http://localhost:8069 after a few seconds.")
