
from fpdf import FPDF
import re

class PDF(FPDF):
    def header(self):
       
        self.set_font('Helvetica', 'B', 16)
        self.set_text_color(0, 0, 0) # Changed to black
        self.cell(0, 10, 'Data Catalog Summary', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(0, 0, 0) # Changed to black
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(0, 0, 0) # Changed to black
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Helvetica', '', 10)
        self.set_text_color(0, 0, 0) # Changed to black
        
        lines = body.split('\n')
        for line in lines:
            line = line.strip()
            if not line:
                self.ln(3)
                continue

            # Handle headings
            if line.startswith('### '):
                self.set_font('Helvetica', 'B', 12)
                self.set_text_color(0, 0, 0) # Changed to black
                self.write(8, line[4:])
                self.ln(8)
                self.set_font('Helvetica', '', 10)
                self.set_text_color(0, 0, 0) # Changed to black
                continue
            elif line.startswith('## '):
                self.set_font('Helvetica', 'B', 13)
                self.set_text_color(0, 0, 0) # Changed to black
                self.write(8, line[3:])
                self.ln(8)
                self.set_font('Helvetica', '', 10)
                self.set_text_color(0, 0, 0) # Changed to black
                continue
            elif line.startswith('# '):
                self.set_font('Helvetica', 'B', 15)
                self.set_text_color(0, 0, 0) # Changed to black
                self.write(8, line[2:])
                self.ln(10)
                self.set_font('Helvetica', '', 10)
                self.set_text_color(0, 0, 0) # Changed to black
                continue
            
            # Handle list items (simple bullet points)
            # MODIFIED: Removed explicit '•' to avoid font issue
            if line.startswith('* ') or line.startswith('- '):
                self.set_x(self.l_margin + 5) # Indent for list
                processed_line = line[2:].replace('**', '').replace('`', '') # Remove markdown for plain text
                self.write(8, processed_line) # Just write the text after the bullet char
                self.ln(8)
            else:
                # Basic handling for bold text within paragraphs
                # Remove Markdown formatting for basic text rendering
                processed_line = line.replace('**', '').replace('`', '') 
                processed_line = processed_line.replace('\n', ' ')

                self.multi_cell(0, 8, processed_line)
                self.ln(3) # Small gap after each paragraph

    def add_markdown_content(self, markdown_text):
        lines = markdown_text.split('\n')
        
        for line in lines:
            line = line.strip()
            if not line:
                self.ln(3)
                continue

            # Check for headings
            if line.startswith('### '):
                self.set_font('Helvetica', 'B', 12)
                self.set_text_color(0, 0, 0) # Changed to black
                self.multi_cell(0, 8, line[4:])
                self.ln(4)
                self.set_font('Helvetica', '', 10)
                self.set_text_color(0, 0, 0) # Changed to black
                continue
            elif line.startswith('## '):
                self.set_font('Helvetica', 'B', 13)
                self.set_text_color(0, 0, 0) # Changed to black
                self.multi_cell(0, 8, line[3:])
                self.ln(6)
                self.set_font('Helvetica', '', 10)
                self.set_text_color(0, 0, 0) # Changed to black
                continue
            elif line.startswith('# '):
                self.set_font('Helvetica', 'B', 15)
                self.set_text_color(0, 0, 0) # Changed to black
                self.multi_cell(0, 8, line[2:])
                self.ln(8)
                self.set_font('Helvetica', '', 10)
                self.set_text_color(0, 0, 0) # Changed to black
                continue
            # Check for bullet points
            # MODIFIED: Removed explicit '•' to avoid font issue
            elif line.startswith('* ') or line.startswith('- '):
                self.set_x(self.l_margin + 5)
                cleaned_line = line[2:].replace('**', '').replace('`', '')
                self.multi_cell(0, 8, cleaned_line) # Just write the text after the bullet char
                self.ln(2)
            else:
                # Regular paragraph text
                cleaned_line = line.replace('**', '').replace('`', '')
                self.multi_cell(0, 8, cleaned_line)
                self.ln(3)

def generate_pdf_from_markdown(markdown_content: str) -> bytes:
    """
    Generates a PDF from markdown content.
    Returns the PDF as bytes.
    """
    try:
        pdf = PDF('P', 'mm', 'A4')
        pdf.add_page()
        # Set colors for the document body
        # Consider changing this to white (255, 255, 255) if you want black text on a white background
        pdf.set_fill_color(13, 17, 23) 
        pdf.set_text_color(0, 0, 0) # Changed to black for default text color

        pdf.add_markdown_content(markdown_content)
        
        # Explicitly convert to bytes to satisfy st.download_button if it's strict
        return bytes(pdf.output(dest='S'))
    except Exception as e:
        # Re-raising the exception with a more descriptive message
        raise Exception(f"PDF generation failed: {e}. Ensure the content is not too complex for conversion, and check for unsupported characters.") from e
