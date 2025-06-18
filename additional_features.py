
import streamlit as st
import json
from io import BytesIO 
from pdf_utils import generate_pdf_from_markdown 

def render_summary_output_section():
    """
    Renders the AI-generated human-readable summary and provides download options.
    """
    st.subheader("📄 Generated Table Summary")

    if st.session_state.generated_summary_markdown:
        
        st.markdown("### 📄 Summary Preview")
        
        st.markdown(f"<div class='documentation-output'>{st.session_state.generated_summary_markdown}</div>", unsafe_allow_html=True)
        st.success("Summary ready! Use the download options below.")

        st.markdown("---")
        st.markdown("<h3><i class='fas fa-download'></i> Download Summary</h3>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)

        with col1:
            
            st.download_button(
                label="⬇️ Download as Markdown",
                data=st.session_state.generated_summary_markdown.encode('utf-8'),
                file_name=f"{st.session_state.parsed_table_metadata.get('table_name', 'table_summary').replace(' ', '_').lower()}.md",
                mime="text/markdown",
                use_container_width=True,
                key="download_summary_md"
            )
        
        with col2:
           
            try:
                pdf_bytes = generate_pdf_from_markdown(st.session_state.generated_summary_markdown)
                st.download_button(
                    label="⬇️ Download as PDF",
                    data=pdf_bytes,
                    file_name=f"{st.session_state.parsed_table_metadata.get('table_name', 'table_summary').replace(' ', '_').lower()}.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                    key="download_summary_pdf"
                )
            except Exception as e:
                st.warning(f"Could not generate PDF for download: {e}. Ensure the content is not too complex for PDF conversion.")
                st.info("PDF generation has limitations with complex Markdown or special characters. Try downloading as Markdown instead.")

    else:
        st.info("No summary generated yet. Input table metadata and click 'Generate Table Summary'.")


def render_clear_button():
    """
    Renders a button to clear all application state and rerun.
    """
    st.markdown("---")
    st.markdown("<h3>🧹 Reset Application</h3>", unsafe_allow_html=True)
    if st.button("🔄 Clear All Data & Restart", type="secondary", use_container_width=True, key="clear_all_app_data_button"):
        for key in list(st.session_state.keys()):
            if key in ['table_metadata_input', 'generated_summary_markdown', 'parsed_table_metadata']:
                if key in st.session_state:
                    del st.session_state[key]
        st.info("Application state cleared. Reloading...")
        st.rerun()
