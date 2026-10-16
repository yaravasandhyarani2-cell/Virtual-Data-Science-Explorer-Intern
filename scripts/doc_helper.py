"""
doc_helper.py
Provides formatting utilities for generating professional 10-15 page DOCX files
with custom typography (Calibri, 1.15 line spacing), branded tables, cover pages,
headers/footers, and figure embeds with captions.
"""

import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml

NAVY = RGBColor(27, 54, 93)      # #1B365D
TEAL = RGBColor(0, 128, 128)     # #008080
DARK_TEXT = RGBColor(30, 41, 59) # #1E293B
GRAY = RGBColor(92, 118, 141)    # #5C768D


def set_cell_background(cell, fill_hex):
    """Sets background shading of a table cell."""
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tc_pr.append(shd)


def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Sets cell padding in dxa."""
    tc_pr = cell._tc.get_or_add_tcPr()
    tc_mar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tc_pr.append(tc_mar)


def create_styled_document():
    """Initializes and styles a python-docx Document with Calibri 11pt, 1.15 line spacing."""
    doc = Document()
    
    # Set standard 1-inch margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)
        
        # Configure Header & Footer
        footer = section.footer
        f_p = footer.paragraphs[0]
        f_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        f_run = f_p.add_run("Virtual Data Science Explorer Internship | October 2026")
        f_run.font.name = "Calibri"
        f_run.font.size = Pt(9)
        f_run.font.color.rgb = GRAY

    # Set Normal Style
    style_normal = doc.styles['Normal']
    style_normal.font.name = 'Calibri'
    style_normal.font.size = Pt(11)
    style_normal.font.color.rgb = DARK_TEXT
    style_normal.paragraph_format.line_spacing = 1.15
    style_normal.paragraph_format.space_after = Pt(6)

    return doc


def add_cover_page(doc, title, subtitle, doc_ref):
    """Creates a modern executive title page."""
    # Top spacing
    for _ in range(3):
        doc.add_paragraph()

    p_org = doc.add_paragraph()
    r_org = p_org.add_run("VIRTUAL DATA SCIENCE EXPLORER INTERNSHIP")
    r_org.font.size = Pt(12)
    r_org.font.bold = True
    r_org.font.color.rgb = TEAL

    p_title = doc.add_paragraph()
    r_title = p_title.add_run(title)
    r_title.font.size = Pt(26)
    r_title.font.bold = True
    r_title.font.color.rgb = NAVY
    p_title.paragraph_format.space_after = Pt(8)

    p_sub = doc.add_paragraph()
    r_sub = p_sub.add_run(subtitle)
    r_sub.font.size = Pt(14)
    r_sub.font.color.rgb = GRAY
    p_sub.paragraph_format.space_after = Pt(28)

    # Decorative horizontal line
    p_line = doc.add_paragraph()
    p_line.paragraph_format.space_after = Pt(36)

    # Metadata Table
    meta_table = doc.add_table(rows=5, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.LEFT
    meta_data = [
        ("Project Domain:", "Customer Churn Prediction for Subscription Telecom"),
        ("Deliverable Code:", doc_ref),
        ("Author / Intern:", "Data Science Explorer Intern"),
        ("Architectural Role:", "Senior Data Science Manager & Python Architect"),
        ("Publication Date:", "16-Oct-2026")
    ]
    for row_idx, (label, val) in enumerate(meta_data):
        row = meta_table.rows[row_idx]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width = Inches(2.2)
        c1.width = Inches(4.3)
        p0 = c0.paragraphs[0]
        r0 = p0.add_run(label)
        r0.bold = True
        r0.font.color.rgb = NAVY
        p1 = c1.paragraphs[0]
        r1 = p1.add_run(val)
        r1.font.color.rgb = DARK_TEXT

    doc.add_page_break()


def add_table_of_contents(doc, sections_list):
    """Adds a structured, stylized Table of Contents list."""
    p_h = doc.add_paragraph()
    r_h = p_h.add_run("Table of Contents")
    r_h.font.size = Pt(18)
    r_h.font.bold = True
    r_h.font.color.rgb = NAVY
    p_h.paragraph_format.space_after = Pt(12)

    toc_table = doc.add_table(rows=len(sections_list) + 1, cols=2)
    toc_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = toc_table.rows[0]
    hdr.cells[0].paragraphs[0].add_run("Section / Content Area").bold = True
    hdr.cells[0].paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
    hdr.cells[1].paragraphs[0].add_run("Page Ref").bold = True
    hdr.cells[1].paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
    set_cell_background(hdr.cells[0], "1B365D")
    set_cell_background(hdr.cells[1], "1B365D")
    hdr.cells[0].width = Inches(5.2)
    hdr.cells[1].width = Inches(1.3)

    for idx, (title, page) in enumerate(sections_list):
        row = toc_table.rows[idx + 1]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width = Inches(5.2)
        c1.width = Inches(1.3)
        p0 = c0.paragraphs[0]
        r0 = p0.add_run(title)
        r0.font.color.rgb = DARK_TEXT
        p1 = c1.paragraphs[0]
        r1 = p1.add_run(str(page))
        r1.font.color.rgb = GRAY
        if idx % 2 == 1:
            set_cell_background(c0, "F8FAFC")
            set_cell_background(c1, "F8FAFC")

    doc.add_page_break()


def add_heading_1(doc, text):
    """Adds a styled Level 1 Heading."""
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.font.size = Pt(16)
    r.font.bold = True
    r.font.color.rgb = NAVY
    p.paragraph_format.space_before = Pt(18)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    return p


def add_heading_2(doc, text):
    """Adds a styled Level 2 Heading."""
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.font.size = Pt(13)
    r.font.bold = True
    r.font.color.rgb = TEAL
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    return p


def add_heading_3(doc, text):
    """Adds a styled Level 3 Heading."""
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.font.size = Pt(11.5)
    r.font.bold = True
    r.font.color.rgb = DARK_TEXT
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    return p


def add_bullet_point(doc, bold_prefix, text):
    """Adds a bullet point with bold lead-in."""
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_b = p.add_run(bold_prefix + " ")
        r_b.bold = True
        r_b.font.color.rgb = NAVY
    r_t = p.add_run(text)
    r_t.font.color.rgb = DARK_TEXT
    return p


def add_styled_table(doc, headers, data, col_widths=None):
    """Adds a modern corporate styled table with navy headers and alternating shading."""
    table = doc.add_table(rows=len(data) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER

    # Format Header Row
    hdr_row = table.rows[0]
    for idx, text in enumerate(headers):
        cell = hdr_row.cells[idx]
        set_cell_background(cell, "1B365D")
        set_cell_margins(cell, top=120, bottom=120, left=140, right=140)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(text)
        r.bold = True
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(255, 255, 255)

    # Format Data Rows
    for row_idx, row_data in enumerate(data):
        row = table.rows[row_idx + 1]
        bg_color = "F8FAFC" if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, val in enumerate(row_data):
            cell = row.cells[col_idx]
            set_cell_background(cell, bg_color)
            set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(str(val))
            r.font.size = Pt(9)
            r.font.color.rgb = DARK_TEXT

    # Set Column Widths if provided
    if col_widths:
        for row in table.rows:
            for idx, width in enumerate(col_widths):
                row.cells[idx].width = Inches(width)

    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(4)
    p_after.paragraph_format.space_after = Pt(8)
    return table


def add_figure_with_caption(doc, img_path, caption_text, width_inches=5.8):
    """Embeds an image into the document centered with an explicit figure caption."""
    if not os.path.exists(img_path):
        p_err = doc.add_paragraph(f"[Image Missing: {img_path}]")
        p_err.runs[0].font.color.rgb = RGBColor(200, 0, 0)
        return

    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(10)
    p_img.paragraph_format.space_after = Pt(4)
    run_img = p_img.add_run()
    run_img.add_picture(img_path, width=Inches(width_inches))

    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(2)
    p_cap.paragraph_format.space_after = Pt(12)
    r_cap = p_cap.add_run(caption_text)
    r_cap.font.size = Pt(9.5)
    r_cap.font.italic = True
    r_cap.font.color.rgb = GRAY


def add_code_block(doc, code_str):
    """Embeds a monospaced code snippet block with subtle light gray shading."""
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_background(cell, "F1F5F9")
    set_cell_margins(cell, top=100, bottom=100, left=150, right=150)
    cell.width = Inches(6.5)

    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.05
    r = p.add_run(code_str)
    r.font.name = "Consolas"
    r.font.size = Pt(8.5)
    r.font.color.rgb = RGBColor(15, 23, 42)

    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_after = Pt(6)
