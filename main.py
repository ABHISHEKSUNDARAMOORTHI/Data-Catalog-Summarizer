
import streamlit as st
import json
from styling import apply_base_styles
from advanced_styling import apply_advanced_styles 
from features import render_metadata_input_section
from additional_features import render_summary_output_section, render_clear_button
st.set_page_config(
    page_title="Data Catalog Summarizer",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)
apply_base_styles()
apply_advanced_styles()
if 'table_metadata_input' not in st.session_state:
    
    st.session_state.table_metadata_input = json.dumps({
      "table_name": "Customers",
      "purpose": "Stores information about registered customers.",
      "columns": [
        {"name": "customer_id", "type": "INT", "description": "Unique identifier for each customer.", "is_pk": True},
        {"name": "first_name", "type": "VARCHAR(50)", "description": "Customer's first name."},
        {"name": "last_name", "type": "VARCHAR(50)", "description": "Customer's last name."},
        {"name": "email", "type": "VARCHAR(100)", "description": "Customer's email address (unique).", "is_unique": True},
        {"name": "registration_date", "type": "DATE", "description": "Date customer registered."},
        {"name": "address_id", "type": "INT", "description": "Foreign key to the Addresses table.", "is_fk": True, "references": "Addresses.address_id"}
      ],
      "sample_rows": [
        {"customer_id": 1, "first_name": "Alice", "last_name": "Smith", "email": "alice@example.com", "registration_date": "2023-01-15", "address_id": 101},
        {"customer_id": 2, "first_name": "Bob", "last_name": "Johnson", "email": "bob@example.com", "registration_date": "2023-02-20", "address_id": 102}
      ],
      "relationships": [
        {"from_table": "Customers", "from_column": "address_id", "to_table": "Addresses", "to_column": "address_id", "type": "One-to-Many"}
      ]
    }, indent=2)

if 'generated_summary_markdown' not in st.session_state:
    st.session_state.generated_summary_markdown = ""
if 'parsed_table_metadata' not in st.session_state:
    st.session_state.parsed_table_metadata = {}
st.title("📚 Data Catalog Summarizer")
st.write(
    "Generate human-readable summaries for your data tables "
    "from metadata, leveraging Google Gemini AI for automated data cataloging."
)
st.markdown("---")
render_metadata_input_section()

st.markdown("---")
render_summary_output_section()

st.markdown("---")
render_clear_button()

st.markdown("---")
st.caption("Data Catalog Summarizer | Powered by Streamlit & Google Gemini AI")
