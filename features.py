
import streamlit as st
import json
import re 
from ai_logic import ask_gemini_text 

def render_metadata_input_section():
    """
    Renders the text area for users to input table metadata (JSON).
    Includes an example and a button to trigger summary generation.
    """
    st.subheader("📝 Input Table Metadata (JSON)")
    st.markdown(
        "Paste the JSON metadata for your data table. "
        "This should include `table_name`, `purpose`, `columns` (with `name`, `type`, `description`, `is_pk`, `is_fk`), and optionally `sample_rows` or `relationships`."
    )

    
    raw_metadata_input = st.text_area(
        "Enter your table metadata as JSON:",
        value=st.session_state.table_metadata_input,
        height=400,
        key="table_metadata_input_area"
    )
    st.session_state.table_metadata_input = raw_metadata_input 

    
    if st.button("Auto-Format JSON Input", key="format_json_button"):
        try:
            
            cleaned_input = re.sub(r"//.*?\n|/\*.*?\*/", "", raw_metadata_input, flags=re.DOTALL)
            formatted_json = json.dumps(json.loads(cleaned_input), indent=2)
            st.session_state.table_metadata_input = formatted_json
            st.success("JSON formatted successfully! ✅")
            st.rerun() 
        except json.JSONDecodeError as e:
            st.error(f"Invalid JSON format: {e}. Please ensure your JSON is syntactically correct.")
        except Exception as e:
            st.error(f"An unexpected error occurred during formatting: {e}")

    if st.button("✨ Generate Table Summary", type="primary", use_container_width=True, key="generate_summary_button"):
        if not raw_metadata_input.strip():
            st.warning("Please paste some table metadata to generate a summary.")
            st.session_state.generated_summary_markdown = "" 
            return

        try:
            
            cleaned_metadata_for_ai = re.sub(r"//.*?\n|/\*.*?\*/", "", raw_metadata_input, flags=re.DOTALL)
            parsed_metadata = json.loads(cleaned_metadata_for_ai)
            st.session_state.parsed_table_metadata = parsed_metadata 

            
            prompt = f"""
            You are a Data Catalog Agent. Read the following JSON metadata for a data table and generate a concise, human-readable summary.
            The summary should clearly describe:
            -   **Purpose of the table:** What the table is generally used for.
            -   **Key Data Elements:** A description of important columns, their data types, and any special characteristics (e.g., primary key, unique, foreign key relationships, descriptions).
            -   **Relationships:** Mention any foreign key relationships to other tables.
            -   **Observations from sample rows (if available):** Briefly describe what the sample rows illustrate.

            Focus on clarity and conciseness, suitable for a data catalog entry.
            If the schema or relationships are complex, simplify for readability.
            Format the output in Markdown using clear headings and bullet points for each section.

            Table Metadata:
            ```json
            {json.dumps(parsed_metadata, indent=2)}
            ```
            """
            with st.spinner("Generating summary with Gemini AI... 🤖"):
                summary_text = ask_gemini_text(prompt)
                st.session_state.generated_summary_markdown = summary_text
                st.success("Summary generated successfully! ✅")
        except json.JSONDecodeError as e:
            st.error(f"Invalid JSON input: {e}. Please ensure your table metadata is valid JSON.")
            st.session_state.generated_summary_markdown = ""
        except Exception as e:
            st.error(f"An error occurred during summary generation: {e}. Please check your input or API key.")
            st.session_state.generated_summary_markdown = ""
