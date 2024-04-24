import tkinter as tk
from tkinter import filedialog

# Función para leer el contenido de un archivo .txt seleccionado por el usuario
def lectura():
    archivo = filedialog.askopenfile(title="Seleccione el archivo txt")
    if archivo:
        contenido = archivo.read()
        archivo.close()
        return contenido
    else:
        return None

# Función para contar la cantidad de cada caracter en un texto dado
def Contador_caracteres(texto):
    diccionario_car = {}
    for caracter in texto:
        diccionario_car[caracter] = diccionario_car.get(caracter, 0) + 1
    # Ordenar el diccionario por valor (contador) de mayor a menor
    diccionario_car_ordenado = {k: v for k, v in sorted(diccionario_car.items(), key=lambda item: item[1], reverse=True)}
    return diccionario_car_ordenado

# Función para mostrar el conteo de caracteres en un widget Text de tkinter
def Mostrar_Cont(Diccionario):
    texto_contador = ""
    for Caracter, Contador in Diccionario.items():
        texto_contador += "'{}' = {}\n".format(Caracter, Contador)
    Texto2.delete(1.0, tk.END)
    Texto2.insert(tk.END, texto_contador)

# Función que actualiza el contador de caracteres después de leer un archivo
def actualizar_texto_contador():
    texto_archivo = lectura()
    if texto_archivo:
        contador_caracteres = Contador_caracteres(texto_archivo)
        Mostrar_Cont(contador_caracteres)

# Creación de la ventana principal de la aplicación
Pantalla = tk.Tk()
Pantalla.title("Practica 7")
Pantalla.geometry("1920x1080")

# Etiqueta para mostrar el título de la práctica
Texto1 = tk.Label(Pantalla, text="Practica 7", bg="cyan", fg="black", font="Arial 14")
Texto1.pack(fill=tk.X)

# Botón para leer el archivo y mostrar el conteo de caracteres
BotonA = tk.Button(Pantalla, text="Leer Archivo", bg="light green", fg="black", font="Arial 12", command=actualizar_texto_contador)
BotonA.pack(side=tk.TOP, padx=10, pady=10)

# BotonB para comprimir archivo (sin funcionalidad)
BotonB = tk.Button(Pantalla, text="Comprimir Archivo", bg="light green", fg="black", font="Arial 12")
BotonB.pack(side=tk.TOP, padx=10, pady=10)

# BotonC para descomprimir archivo (sin funcionalidad)
BotonC = tk.Button(Pantalla, text="Descomprimir Archivo", bg="light green", fg="black", font="Arial 12")
BotonC.pack(side=tk.TOP, padx=10, pady=10)

# Widget Text para mostrar el resultado del contador de caracteres
Texto2 = tk.Text(Pantalla, font="Arial 12")
Texto2.pack(pady=20)

# Método principal para mostrar la ventana y ejecutar la aplicación
Pantalla.mainloop()
