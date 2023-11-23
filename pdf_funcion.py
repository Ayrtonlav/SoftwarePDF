import PyPDF2
import tkinter as tk
from tkinter import ttk,filedialog

# Función para unir archivos PDF
def unir_pdf():
    archivos = filedialog.askopenfilenames(title="Seleccionar archivos PDF", filetypes=[("Archivos PDF", "*.pdf")])
    if archivos:
        nombre_salida = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Archivos PDF", "*.pdf")])
        if nombre_salida:
            pdf_final = PyPDF2.PdfMerger()
            for nombre_archivo in archivos:
                pdf_final.append(nombre_archivo)
            with open(nombre_salida, "wb") as salida:
                pdf_final.write(salida)
            pdf_final.close()
            resultado_label.config(text=f"PDF unido como: {nombre_salida}")
        else:
            resultado_label.config(text="Operación cancelada")
    else:
        resultado_label.config(text="Ningún archivo seleccionado")
