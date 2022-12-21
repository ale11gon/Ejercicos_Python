import tkinter
from tkinter import ttk

window = tkinter.Tk()

def reiniciar(event):
	r1.deselect()
  r2.deselect()
  r3.deselect()

windwow.columnconfigure(0,weight=1)
windwow.columnconfigure(1,weight=3)

#Crear una variable a elegir entre 3 posibilidades
selected = tk.StringVar()

r1 = ttk.Radiobutton(window, text= "Opción 1", value="1", variable = selected)
r2 = ttk.Radiobutton(window, text= "Opción 2", value="2", variable = selected)
r3 = ttk.Radiobutton(window, text= "Opción 3", value="3", variable = selected)

r1.deselect()
r2.deselect()
r3.deselect()

r1.grid(column=0, row=0, padx=5, pady=5)
r2.grid(column=0, row=1, padx=5, pady=5)
r3.grid(column=0, row=2, padx=5, pady=5)

botonReiniciar = tkinter.Button(window, text='Reiniciar')
botonReiniciar.grid(column=2, row=0, padx=5, pady=5)

botonSalir.bind('<Button-1>', reiniciar)
	

window.mainloop()
