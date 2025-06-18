# styling.py
import streamlit as st

def apply_base_styles():
    """Applies custom CSS for the Streamlit application base styles."""
    st.markdown("""
    <style>
    /* Import Inter font and Font Awesome */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css');

    :root {
        /* New Color Palette: Clean Dark Gray & Blue Accents */
        --bg-primary: #0D1117; /* Very Dark Grey/Blue (like GitHub dark) */
        --bg-secondary: #161B22; /* Slightly Lighter Dark Grey/Blue (Card/Header) */
        --text-light: #C9D1D9; /* Light Gray Text */
        --text-medium: #8B949E; /* Medium Gray Text */

        --accent-blue-light: #58A6FF; /* Vibrant Blue */
        --accent-blue-dark: #1F6FD8; /* Darker Blue */

        --success-color: #3FB950; /* Green */
        --danger-color: #F85149; /* Red */
        --warning-color: #DD9F1B; /* Orange/Amber */
        --info-color: #79C0FF; /* Lighter Blue */

        --border-color: #30363D; /* Darker Gray for Borders */
        --shadow-light: rgba(0, 0, 0, 0.2);
        --shadow-medium: rgba(0, 0, 0, 0.4);
        --border-radius-lg: 12px;
        --border-radius-md: 8px;
        --border-radius-sm: 4px;
    }

    /* Base Streamlit overrides */
    .stApp {
        background-color: var(--bg-primary);
        color: var(--text-light);
        font-family: 'Inter', sans-serif;
    }

    /* Main content area (Streamlit's block-container) */
    .main .block-container {
        max-width: 1200px;
        padding: 2.5rem 3rem;
        background-color: var(--bg-secondary);
        border-radius: var(--border-radius-lg);
        box-shadow: 0 10px 25px var(--shadow-medium);
        margin: 2rem auto; /* Center it */
        border: 1px solid var(--border-color);
    }

    /* Headers and Titles */
    .stApp > header {
        background-color: var(--bg-secondary);
        padding: 1.5rem 2rem;
        box-shadow: 0 4px 8px var(--shadow-medium);
        text-align: center;
        position: sticky;
        top: 0;
        z-index: 1000;
        border-bottom: 1px solid var(--border-color);
    }
    .stApp > header h1 {
        color: var(--accent-blue-light); /* Title color */
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .stApp > header h1 i {
        color: var(--accent-blue-dark); /* Icon color */
        margin-right: 0.5rem;
    }

    /* General Headings */
    h1, h2, h3, h4, h5, h6 {
        color: var(--accent-blue-light);
        font-weight: 600;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }

    h1 {
        font-size: 2.8em;
        text-align: center;
        margin-bottom: 1em;
        color: var(--accent-blue-light);
    }
    h2 {
        font-size: 2.2em;
        color: var(--text-light);
        border-bottom: 2px solid var(--accent-blue-light);
        padding-bottom: 0.5em;
        margin-top: 2em;
    }
    h3 {
        font-size: 1.8em;
        color: var(--accent-blue-dark);
        border-bottom: 1px dashed var(--border-color);
        padding-bottom: 0.3em;
        margin-top: 1.5em;
    }
    h4 {
        font-size: 1.4em;
        color: var(--accent-blue-light);
        margin-top: 1.2em;
    }

    /* Text */
    p {
        color: var(--text-light);
        line-height: 1.6;
        margin-bottom: 1rem;
    }
    strong {
        color: var(--accent-blue-light);
    }
    em {
        color: var(--text-medium);
    }
    a {
        color: var(--accent-blue-light);
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }

    /* Buttons */
    .stButton > button {
        background-color: var(--accent-blue-light);
        color: white;
        border-radius: var(--border-radius-md);
        padding: 0.8rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 8px var(--shadow-light);
        border: none;
    }
    .stButton > button:hover {
        background-color: var(--accent-blue-dark);
        transform: translateY(-2px);
        box-shadow: 0 6px 12px var(--shadow-medium);
    }
    .stButton > button.primary { /* Primary buttons */
        background-color: var(--accent-blue-dark);
    }
    .stButton > button.primary:hover {
        background-color: var(--accent-blue-light);
    }
    .stButton > button.secondary { /* Secondary buttons */
        background-color: var(--bg-primary);
        border: 1px solid var(--accent-blue-light);
        color: var(--accent-blue-light);
    }
    .stButton > button.secondary:hover {
        background-color: var(--accent-blue-light);
        color: var(--bg-primary);
    }

    /* Text Inputs & Text Areas */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background-color: var(--bg-primary);
        border: 1px solid var(--border-color);
        border-radius: var(--border-radius-md);
        color: var(--text-light);
        padding: 0.75rem 1rem;
        font-size: 1em;
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: var(--accent-blue-light);
        box-shadow: 0 0 0 2px rgba(88, 166, 255, 0.2);
        outline: none;
    }

    /* Dataframes */
    .stDataFrame {
        border: 1px solid var(--border-color);
        border-radius: var(--border-radius-md);
        overflow: hidden; /* Ensures rounded corners */
    }
    .stDataFrame table {
        background-color: var(--bg-primary);
    }
    .stDataFrame th {
        background-color: var(--bg-secondary);
        color: var(--text-light);
    }
    .stDataFrame td {
        color: var(--text-light);
    }
    .stDataFrame tbody tr:nth-child(odd) {
        background-color: var(--bg-primary);
    }
    .stDataFrame tbody tr:nth-child(even) {
        background-color: #10151C; /* Slightly different shade for zebra striping */
    }

    /* Info, Success, Warning, Error messages */
    .stAlert {
        border-radius: var(--border-radius-md);
        margin-top: 1rem;
        padding: 1rem 1.5rem;
    }
    .stAlert.st-emotion-cache-1fcpknu { /* Success */
        border-left: 5px solid var(--success-color);
        background-color: rgba(63, 185, 80, 0.1);
        color: var(--success-color);
    }
    .stAlert.st-emotion-cache-1wdd6qg { /* Warning */
        border-left: 5px solid var(--warning-color);
        background-color: rgba(221, 159, 27, 0.1);
        color: var(--warning-color);
    }
    .stAlert.st-emotion-cache-1215i5j { /* Error */
        border-left: 5px solid var(--danger-color);
        background-color: rgba(248, 81, 73, 0.1);
        color: var(--danger-color);
    }
    .stInfo {
        border-left: 5px solid var(--info-color);
        background-color: rgba(121, 192, 255, 0.1);
        border-radius: var(--border-radius-md);
        padding: 1rem 1.5rem;
        margin-top: 1rem;
        color: var(--info-color);
    }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        border-bottom: 2px solid var(--border-color);
        margin-bottom: 1.5rem;
    }
    .stTabs [data-baseweb="tab-list"] button {
        background-color: transparent;
        color: var(--text-medium);
        border: none;
        padding: 0.8rem 1.2rem;
        font-size: 1.05em;
        font-weight: 600;
        transition: all 0.3s ease;
        border-bottom: 3px solid transparent;
    }
    .stTabs [data-baseweb="tab-list"] button:hover:not([aria-selected="true"]) {
        color: var(--text-light);
        background-color: var(--border-color);
        border-radius: var(--border-radius-sm) var(--border-radius-sm) 0 0;
    }
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
        color: var(--accent-blue-light) !important;
        border-bottom: 3px solid var(--accent-blue-light) !important;
        background-color: var(--bg-secondary) !important;
        border-radius: var(--border-radius-sm) var(--border-radius-sm) 0 0;
    }

    /* Expander */
    .streamlit-expanderHeader {
        background-color: var(--bg-primary);
        border: 1px solid var(--border-color);
        border-radius: var(--border-radius-md);
        padding: 0.8rem 1rem;
        margin-bottom: 0.5rem;
        color: var(--text-light);
        font-weight: 600;
        transition: background-color 0.3s ease;
    }
    .streamlit-expanderHeader:hover {
        background-color: #1A222B;
    }
    .streamlit-expanderContent {
        background-color: var(--bg-primary);
        border: 1px solid var(--border-color);
        border-top: none;
        border-radius: 0 0 var(--border-radius-md) var(--border-radius-md);
        padding: 1rem;
    }

    /* Code blocks / Pre-formatted text */
    code {
        background-color: var(--border-color);
        border-radius: var(--border-radius-sm);
        padding: 0.2em 0.4em;
        font-family: 'Fira Code', monospace;
        font-size: 0.9em;
        color: var(--accent-blue-light);
    }
    pre code {
        background-color: var(--bg-primary);
        border: 1px solid var(--border-color);
        border-radius: var(--border-radius-md);
        padding: 1em;
        overflow-x: auto;
        color: var(--text-light);
    }

    /* Responsive Adjustments */
    @media (max-width: 768px) {
        .main .block-container {
            padding: 1.5rem;
            margin: 1rem auto;
            width: 98%;
        }
        .stButton > button {
            display: block;
            width: 100%;
            margin: 0.8rem 0;
        }
        h1 { font-size: 2.2em; }
        h2 { font-size: 1.8em; }
        h3 { font-size: 1.4em; }
        h4 { font-size: 1.1em; }
        .stTabs [data-baseweb="tab-list"] button {
            padding: 0.6rem 0.8rem;
            font-size: 0.9em;
        }
    }
    </style>
    """, unsafe_allow_html=True)
