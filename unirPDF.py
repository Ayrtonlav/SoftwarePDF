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

# Crear la ventana de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Unir archivos PDF")
ventana.geometry("300x200")  # Tamaño de la ventana (ancho x alto)
ventana.configure(bg="white")  # Establecer el fondo en blanco
# Centrar la ventana en la pantalla
ventana.eval('tk::PlaceWindow . center')

# Centrar el botón
frame = ttk.Frame(ventana)
frame.pack(expand=True, fill="both")

# Botón para unir PDFs
unir_button = ttk.Button(frame, text="Unir PDFs", command=unir_pdf)
unir_button.pack(pady=20, padx=20, fill="both", expand=True)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

ventana.mainloop()