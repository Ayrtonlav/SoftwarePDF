from fpdf import FPDF
from tkinter import filedialog
from tkinter import Label

# Función para convertir imágenes JPG a un archivo PDF
def jpg_a_pdf():
    imagenes = filedialog.askopenfilenames(title="Seleccionar imágenes JPG", filetypes=[("Archivos JPG", "*.jpg")])
    if imagenes:
        archivo_pdf = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Archivos PDF", "*.pdf")])
        if archivo_pdf:
            pdf = FPDF()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.add_page()
            
            for imagen in imagenes:
                pdf.image(imagen, x=10, y=10, w=190)
            
            pdf.output(archivo_pdf)
            
            resultado_label.config(text=f"Imágenes JPG convertidas a PDF: {archivo_pdf}")
        else:
            resultado_label.config(text="Operación cancelada")
    else:
        resultado_label.config(text="Ninguna imagen seleccionada")