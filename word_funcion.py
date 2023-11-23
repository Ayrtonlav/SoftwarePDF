import fitz  # PyMuPDF
from docx import Document
from tkinter import filedialog
from tkinter import Label

# Función para convertir un PDF a Word
def pdf_a_word():
    archivo_pdf = filedialog.askopenfilename(title="Boleta de Venta.pdf", filetypes=[("Archivos PDF", "*.pdf")])
    if archivo_pdf:
        archivo_word = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Archivos Word", "*.docx")])
        if archivo_word:
            doc = Document()
            pdf_document = fitz.open(archivo_pdf)
            
            for page_num in range(pdf_document.page_count):
                page = pdf_document[page_num]
                text = page.get_text()
                doc.add_paragraph(text)
            
            doc.save(archivo_word)
            
            resultado_label.config(text=f"PDF convertido a Word: {archivo_word}")
        else:
            resultado_label.config(text="Operación cancelada")
    else:
        resultado_label.config(text="Ningún archivo seleccionado")

# Resto del código para la interfaz gráfica...