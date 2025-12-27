import streamlit as st
from orchestrator import Orchestrator

st.set_page_config(page_title="Autonomous Odoo Partner")

st.title("🚀 Autonomous Odoo Partner Agent")

business = st.selectbox(
    "What type of business are you?",
    ["Retail", "Services", "HR"]
)

db_name = st.text_input("Database name", "my_business_db")
pg_user = st.text_input("PostgreSQL user")
pg_password = st.text_input("PostgreSQL password", type="password")
admin_password = st.text_input("Odoo admin password", type="password")

if st.button("Build My Odoo System"):
    orch = Orchestrator()
    orch.setup_odoo(
        business,
        db_name,
        pg_user,
        pg_password,
        admin_password
    )
    st.success("🎉 Odoo is being set up! Open http://localhost:8069")
