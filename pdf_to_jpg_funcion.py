import tkinter as tk
from tkinter import filedialog
from pdf2image import convert_from_path

# Función para convertir un archivo PDF a imágenes JPG
def pdf_a_jpg(resultado_label):
    archivo_pdf = filedialog.askopenfilename(title="Seleccionar archivo PDF", filetypes=[("Archivos PDF", "*.pdf")])
    if archivo_pdf:
        carpeta_destino = filedialog.askdirectory(title="Seleccionar carpeta de destino")
        if carpeta_destino:
            imagenes = convert_from_path(archivo_pdf)
            if imagenes:
                resultado_label.config(text=f"PDF convertido a imágenes JPG: {len(imagenes)} páginas")
                for i, imagen in enumerate(imagenes):
                    nombre_archivo = f"pagina_{i + 1}.jpg"
                    ruta_completa = f"{carpeta_destino}/{nombre_archivo}"
                    imagen.save(ruta_completa, "JPEG")
            else:
                resultado_label.config(text="No se pudo convertir el PDF a imágenes")
        else:
            resultado_label.config(text="Operación cancelada")
    else:
        resultado_label.config(text="Ningún archivo seleccionado")
