
import streamlit as st

def apply_advanced_styles():
    """
    Applies additional custom CSS for more specific elements or complex layouts.
    Currently, this function can be used to extend the base styling defined in styling.py.
    """
    st.markdown("""
    <style>
    /* Add any advanced or granular CSS rules here that you want separate from base styles */

    /* Example: Styling for specific icons in headers */
    h3 i.fas, h4 i.fas {
        margin-right: 0.5rem;
        color: var(--accent-blue-light); /* Ensure icons match accent color */
    }

    /* Custom styling for the generated documentation output area */
    .documentation-output {
        background-color: var(--bg-primary);
        border: 1px solid var(--border-color);
        border-radius: var(--border-radius-md);
        padding: 1.5rem;
        min-height: 200px;
        max-height: 600px; /* Limit height for scroll */
        overflow-y: auto; /* Scroll for overflowing content */
        margin-top: 1.5rem;
        line-height: 1.8; /* Better readability for text */
        color: var(--text-light);
    }

    .documentation-output h3 {
        color: var(--accent-blue-light);
        font-size: 1.5rem;
        margin-top: 1rem;
        margin-bottom: 0.8rem;
        border-bottom: 1px dashed var(--border-color);
        padding-bottom: 0.3rem;
    }

    .documentation-output h4 {
        color: var(--accent-blue-dark);
        font-size: 1.2rem;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }

    .documentation-output p,
    .documentation-output ul,
    .documentation-output ol,
    .documentation-output li {
        color: var(--text-light);
        margin-bottom: 0.8rem;
    }

    .documentation-output ul {
        list-style-type: disc;
        margin-left: 20px;
    }

    .documentation-output strong {
        color: var(--accent-blue-light);
    }

    .documentation-output code {
        background-color: var(--border-color);
        padding: 0.2em 0.4em;
        border-radius: 4px;
        font-family: 'Fira Code', 'Cascadia Code', monospace;
        font-size: 0.9em;
        color: var(--accent-blue-light);
    }

    .documentation-output pre {
        background-color: var(--bg-primary);
        border: 1px solid var(--border-color);
        border-radius: 6px;
        padding: 1em;
        overflow-x: auto;
        margin-bottom: 1em;
        color: var(--text-light);
    }
    </style>
    """, unsafe_allow_html=True)
