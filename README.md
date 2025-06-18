
# 📚 Data Catalog Summarizer

## 📝 Overview

The **Data Catalog Summarizer** is a Streamlit-based web application designed to automate the process of generating human-readable summaries for data tables from their metadata. This tool leverages **Google Gemini AI** to interpret structured or semi-structured table definitions (e.g., SQL `CREATE TABLE` statements or JSON schema) and produce clear, concise summaries suitable for modern data catalogs.

In data-rich environments with thousands of tables, manual documentation is cumbersome and prone to errors. This application improves **data discoverability**, enhances **data literacy** across teams, and accelerates the population of **automated data catalogs**.

---

## ✨ Features

### 🔗 Flexible Metadata Input
- Accepts metadata in SQL `CREATE TABLE` statements or a custom JSON schema array.
- Includes a pre-filled example JSON for quick demonstration.
- **JSON Auto-Formatting**: Dedicated button to cleanly format pasted JSON.
- **Comment Stripping**: Removes `//` and `/* */` comments for better parsing.

### 🤖 AI-Powered Summary Generation
- Uses **Google Gemini AI** to analyze metadata.
- Generates summaries with:
  - Purpose of the table.
  - Key columns, types, relationships, and descriptions.
  - Relationships (primary/foreign keys).
  - Observations from sample rows.

### 🧾 Structured Markdown Output
- Summaries are formatted in **Markdown** with headings and bullet points for easy readability.

### 🖼️ Visual Summary Preview
- Displays the generated Markdown summary directly in the app for review before download.

### 📥 Multi-Format Download Options
- **Markdown**: Export the summary as `.md`.
- **PDF**: Export the summary as `.pdf` using 'Helvetica' font for wide compatibility.

### 🔁 Clear All Functionality
- Reset all inputs and generated results with one button.

### 💻 Modular & Professional UI
- Built with **Streamlit** for interactivity.
- Custom **CSS** for modern, dark-themed UI with responsive design.
- Session state maintains continuity during interactions.

---

## 🚀 Technologies Used

- **Python** 🐍 – Core language.
- **Streamlit** 🌐 – UI framework.
- **Google Gemini API** 🧠 – AI metadata analysis.
- **python-dotenv** 🔒 – Load API keys securely.
- **fpdf2** 📄 – Convert Markdown summaries to PDF.
- **Custom CSS** 🎨 – For styling and responsive design.

---

## ⚙️ Setup Instructions

### ✅ Prerequisites
- Python 3.8+ installed.
- `pip` available.

### 📁 Clone the Project
> *(If using Canvas, files are already provided. For local use, place files in one directory.)*

### 📦 Install Dependencies
Create `requirements.txt` with:

```

streamlit
python-dotenv
google-generativeai
fpdf2

````

Then run:
```bash
pip install -r requirements.txt
````

### 🔐 Set Up Gemini API Key

1. Get your key from [Google AI Studio](https://aistudio.google.com).
2. Create a `.env` file at the project root.
3. Add:

```env
GEMINI_API_KEY="YOUR_ACTUAL_GEMINI_API_KEY_HERE"
```

> Replace with your real key. No extra spaces or quotes.

---

## ▶️ Usage

1. Open terminal in project directory.
2. Run the app:

```bash
streamlit run main.py
```

3. Browser should auto-open at `http://localhost:8501`.

### 💡 Using the App

* **Input Metadata**: Paste SQL or JSON metadata.
* **Auto-Format**: Use the button to clean JSON.
* **Generate Summary**: Click “✨ Generate Table Summary”.
* **Preview & Download**:

  * View the summary preview.
  * Download as `.md` or `.pdf`.
* **Reset**: Use “🔄 Clear All Data & Restart” to start over.

---

## 📂 Project Structure

| File                     | Purpose                                                          |
| ------------------------ | ---------------------------------------------------------------- |
| `main.py`                | Main entry point; handles layout, styling, and session state.    |
| `styling.py`             | Base custom CSS injection and theme setup.                       |
| `advanced_styling.py`    | Extra CSS rules for specific UI components.                      |
| `ai_logic.py`            | Gemini API logic, prompt management, and AI calls.               |
| `features.py`            | Input handling, auto-formatting, and summary generation trigger. |
| `additional_features.py` | Displays output, manages downloads and reset.                    |
| `pdf_utils.py`           | Converts Markdown summary to PDF using fpdf2.                    |
| `.env`                   | Stores your API key securely (should be ignored in Git).         |
| `requirements.txt`       | Python dependencies list.                                        |

---
