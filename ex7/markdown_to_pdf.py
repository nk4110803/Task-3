import markdown
import pdfkit
config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

with open('example.md', 'r', encoding='utf-8') as md_file:
    md_content = md_file.read()
html_content = markdown.markdown(md_content)
pdfkit.from_string(html_content, 'output.pdf', configuration=config)
print("PDF created successfully")

