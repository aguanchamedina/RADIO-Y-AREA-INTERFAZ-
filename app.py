from tkinter import *
from tkinter import messagebox




# ventana principal
ventana_principal = Tk()
# funciones
def radio():
    R = input("Dijite el valor del Radio: ")
R = int(R)


A = math.pi * R*R
P = 2*math.pi*R


print("El area es: " + str(A))
print("El perimetro es: " + str(P))

def borrar():
    num.set("")
def salir():
    ventana_principal.destroy()

ventana_principal.geometry("500x230")
ventana_principal.config(bg="black")
ventana_principal.title("Número par")
ventana_principal.resizable(0,0)

# variable
num = StringVar()

# frame de datos
frame_datos = Frame(ventana_principal)
frame_datos.config(bg="yellow", width=480, height=100)
frame_datos.place(x=10, y=10)

# indicador de entrada para el número
lb_num = Label(frame_datos, text="Radio = ")
lb_num.config(bg="white", fg="Red", font=("Arial", 16), )
lb_num.place(x=125, y=35, width=100, height=30)

# entrada para el número
entry_num = Entry(frame_datos, textvariable=num)
entry_num.config(bg="white", fg="blue", font=("Arial", 16))
entry_num.focus_set()
entry_num.place(x=250, y=35, width=100, height=30)

# frame de opeaciones
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="blue", width=480, height=100)
frame_operaciones.place(x=10, y=120)

# boton para determinar
bt_sumar = Button(frame_operaciones, text="El area y perimetro es ", command=radio)
bt_sumar.place(x=35, y=35, width=125, height=30)

# botón para borrar
bt_borrar = Button(frame_operaciones, text="Borrar", command=borrar)
bt_borrar.place(x=190, y=35, width=100, height=30)

# botón para salir
bt_salir = Button(frame_operaciones, text="Salir", command=salir)
bt_salir.place(x=335, y=35, width=100, height=30)

ventana_principal.mainloop()