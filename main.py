import tkinter as tk
from tkinter import ttk, filedialog
from pdf_funcion import unir_pdf
from word_funcion import pdf_a_word
from pdf_to_jpg_funcion import pdf_a_jpg
from jpg_to_pdf_function import jpg_a_pdf

# Función para abrir la función de unir PDF
def abrir_unir_pdf():
    unir_pdf()

# Función para abrir la función de convertir PDF a Word
def abrir_pdf_a_word():
    pdf_a_word()

# Función para abrir la función de convertir PDF a imágenes JPG
def abrir_pdf_a_jpg():
    pdf_a_jpg(resultado_label)

# Función para abrir la función de convertir JPG a PDF
def abrir_jpg_a_pdf():
    jpg_a_pdf()

# Crear la ventana de la interfaz gráfica principal
ventana_principal = tk.Tk()
ventana_principal.title("Herramientas PDF")
ventana_principal.geometry("400x200")  # Tamaño de la ventana
ventana_principal.configure(bg="white")  # Establecer el fondo en blanco
ventana_principal.eval('tk::PlaceWindow . center')  # Centrar la ventana

# Botones para las funciones
frame = ttk.Frame(ventana_principal)
frame.pack(expand=True, fill="both")

# Botón para unir PDFs
unir_pdf_button = ttk.Button(frame, text="Unir PDFs", command=abrir_unir_pdf)
unir_pdf_button.pack(pady=10, padx=20, fill="both", expand=True)

# Botón para convertir PDF a Word
pdf_a_word_button = ttk.Button(frame, text="PDF a Word", command=abrir_pdf_a_word)
pdf_a_word_button.pack(pady=10, padx=20, fill="both", expand=True)

# Botón para convertir PDF a imágenes JPG
pdf_a_imagenes_button = ttk.Button(frame, text="PDF a Imágenes", command=abrir_pdf_a_jpg)
pdf_a_imagenes_button.pack(pady=10, padx=20, fill="both", expand=True)

# Botón para convertir JPG a PDF
jpg_a_pdf_button = ttk.Button(frame, text="JPG a PDF", command=abrir_jpg_a_pdf)
jpg_a_pdf_button.pack(pady=10, padx=20, fill="both", expand=True)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana_principal, text="")
resultado_label.pack()

ventana_principal.mainloop()