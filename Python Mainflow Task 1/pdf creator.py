from reportlab.pdfgen import canvas

def convert_to_pdf_reportlab(input_file, output_pdf):
	pdf_canvas = canvas.Canvas(output_pdf)

	with open(input_file, 'r') as python_file:
		content = python_file.read()
		pdf_canvas.drawString(100, 800, content)

	pdf_canvas.save()
filename = r"C:\\Users\\nandh\\Downloads\\Programs\\Pyhton Task 1\\Python Mainflow Task 2\\Task 2_1.py"

# Example usage:
convert_to_pdf_reportlab(filename, 'output_reportlab.pdf')
print("PDF is Saved Successfully")
