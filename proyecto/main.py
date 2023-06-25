from tkinter import *
from Analizadores.sintactico import parser


def verificar():
    try:
        result.set(parser.parse(code.get()))
    except ValueError:
        pass


if __name__ == '__main__':
    window = Tk()
    window.title("Proyecto Grupo 2")
    top_frame = Frame(window, width=500).pack()
    project = Label(top_frame, text="Proyecto con Dart").pack()
    code = StringVar()
    code_label = Label(top_frame, text="Ingrese el código en Dart:").pack()
    entry_code = Entry(window, width=75, textvariable=code).pack()
    result = StringVar()
    result_label = Label(top_frame, text="Resultado:").pack()
    entry_result = Entry(window, width=75, textvariable=result).pack()
    bottom_frame = Frame(window, width=500).pack(side="bottom")
    btn1 = Button(bottom_frame, text="Verificar código", command=verificar).pack()

    window.mainloop()
