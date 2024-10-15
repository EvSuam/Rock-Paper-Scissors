import tkinter as tk
import random
from tkinter import font




app = tk.Tk()
app.geometry("600x300")
app.configure(background="black")
app.title("Rock, Paper, Scissors")


label_resultado = tk.Label(app, text="", background="black", font=("Courier", 25))
label_resultado.grid(row=3, column=0, columnspan=5, padx=5, pady=20)

# Función para actualizar la etiqueta (borrarla o mostrar nuevo texto)
def actualizar_label(texto="", fondo="black"):
    label_resultado.config(text=texto, background=fondo)

# Función para la opción "Piedra"
def rock():
    numero_random = random.randint(1, 3)
    print("Escojo Piedra")
    
    if numero_random == 1:
        actualizar_label(texto="Escojo Papel, ¡Has Perdido!", fondo="#ff6961")
    elif numero_random == 2:
        actualizar_label(texto="Escojo Tijera, ¡Has Ganado!", fondo="#ff6961")
    elif numero_random == 3:
        actualizar_label(texto="Escojo Piedra, ¡Hemos Empatado!", fondo="#ff6961")

def scissors():
    numero_random = random.randint(1, 3)
    print("Escojo Tijera")
    
    if numero_random == 1:
        actualizar_label(texto="Escojo Papel, ¡Has Ganado!", fondo="#efa94a")
    elif numero_random == 2:
        actualizar_label(texto="Escojo Tijera, ¡Hemos Empatado!", fondo="#efa94a")
    elif numero_random == 3:
        actualizar_label(texto="Escojo Piedra, ¡Has Perdido!", fondo="#efa94a")

def paper():
    numero_random = random.randint(1, 3)
    print("Escojo Papel")
    
    if numero_random == 1:
        actualizar_label(texto="Escojo Papel, ¡Hemos Empatado!", fondo="#8CBED6")
    elif numero_random == 2:
        actualizar_label(texto="Escojo Tijera, ¡Has Perdido!", fondo="#8CBED6")
    elif numero_random == 3:
        actualizar_label(texto="Escojo Piedra, ¡Has Ganado!", fondo="#8CBED6")



tk.Label(
    text= ("Bienvenido al Piedra, Papel o Tijera de la muerte"),
    font=("Courier", 14),
    background= "green",
    foreground="black",
).grid(row=0, column=0, columnspan=3, padx=10, pady=20)


tk.Label(
    text= ("----Haz tu elección----"),
    background= "white",
    foreground="black",
).grid(row=1, column=0, columnspan=3, padx=10, pady=10)

tk.Button(
    app,
    text="Roca",
    background="white",
    command=rock,
    justify="left"
).grid(row=2, column=0, padx=10, pady=20)

tk.Button(
    app,
    text="Tijera",
    background="white",
    command=scissors,
    justify= "center"
).grid(row=2, column=1, padx=10, pady=20)

tk.Button(
    app,
    text="Papel",
    background="white",
    command=paper,
    justify="right"
).grid(row=2, column=2, padx=10, pady=20)



tk.mainloop()