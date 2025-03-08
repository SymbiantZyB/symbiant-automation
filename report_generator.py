"""
Report Generator Module
------------------------
Generates structured reports in Markdown and PDF formats.

Author: SymbiantZyB
"""

from fpdf import FPDF

class ReportGenerator:
    """
    Generates and exports reports in PDF format.
    """

    def __init__(self, title="Automation Report"):
        """
        Initializes the report generator.

        Args:
            title (str): The title of the report.
        """
        self.title = title
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)
    
    def add_section(self, heading: str, content: str):
        """Adds a section to the report."""
        self.pdf.add_page()
        self.pdf.set_font("Arial", style="B", size=16)
        self.pdf.cell(200, 10, heading, ln=True, align="C")
        self.pdf.set_font("Arial", size=12)
        self.pdf.multi_cell(0, 10, content)
    
    def save_report(self, filename="report.pdf"):
        """Saves the generated report."""
        self.pdf.output(filename)

# Example Usage
if __name__ == "__main__":
    report = ReportGenerator()
    report.add_section("Introduction", "This is a sample report section.")
    report.save_report("example_report.pdf")
