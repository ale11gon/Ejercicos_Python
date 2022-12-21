import tkinter

window = tkinter.Tk()

window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=3)

label_lista = tkinter.Label(window, text='Elige tu OS favorito!',bg='yellow',fg='blue')
label_lista.grid(column=1, row=0, sticky= tkinter.W)

lista = ['Windows','macOS','Linux','MS DOS','AmigaOS','BeOS','OS/2']
lista_items = tkinter.StringVar(value=lista)
listbox = tkinter.Listbox(window,height=10, listvariable= lista_items,fg='black')
listbox.grid(column=1, row=1, sticky= tkinter.W)

window.mainloop()