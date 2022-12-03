from tkinter import *

root=Tk()
root.title('Calculadora')

frame1=Frame(root)
frame1.grid(column=0, row=0)

ecuacion=StringVar()

def press(num):
    ecuacion.set(ecuacion.get()+str(num))

def igual():
    try:
        total=str(eval(ecuacion.get())) #eval desarrolla la operacion
        ecuacion.set(total)
    except:
        ecuacion.set('Error')

def limpiar():
    ecuacion.set('')

e=Entry(frame1, width=32, textvariable=ecuacion)
e.grid(row=0, columnspan=4, sticky='nswe') #permito que mi entry ocupe 4 columnas

btn0=Button(frame1, text='0', fg='black', bg='grey', width=8, command=lambda: press(0)) #permite que se muestre en mi entry los botones que oprimo
btn1=Button(frame1, text='1', fg='black', bg='grey', width=8, command=lambda: press(1))
btn2=Button(frame1, text='2', fg='black', bg='grey', width=8, command=lambda: press(2))
btn3=Button(frame1, text='3', fg='black', bg='grey', width=8, command=lambda: press(3))
btn4=Button(frame1, text='4', fg='black', bg='grey', width=8, command=lambda: press(4))
btn5=Button(frame1, text='5', fg='black', bg='grey', width=8, command=lambda: press(5))
btn6=Button(frame1, text='6', fg='black', bg='grey', width=8, command=lambda: press(6))
btn7=Button(frame1, text='7', fg='black', bg='grey', width=8, command=lambda: press(7))
btn8=Button(frame1, text='8', fg='black', bg='grey', width=8, command=lambda: press(8))
btn9=Button(frame1, text='9', fg='black', bg='grey', width=8, command=lambda: press(9))
btnpunt=Button(frame1, text='.', fg='black', bg='grey', width=8, command=lambda: press('.'))
btnmas=Button(frame1, text='+', fg='black', bg='orange', width=8, command=lambda: press('+'))
btnmen=Button(frame1, text='-', fg='black', bg='orange', width=8, command=lambda: press('-'))
btnpor=Button(frame1, text='*', fg='black', bg='orange', width=8, command=lambda: press('*'))
btndiv=Button(frame1, text='/', fg='black', bg='orange', width=8, command=lambda: press('/'))
btnigual=Button(frame1, text='=', fg='black', bg='orange', width=8, command=igual)
btnclear=Button(frame1, text='Limpiar', fg='black', bg='orange', width=8, command=limpiar)

btn0.grid(columnspan=2, row=4, sticky='nswe')
btn1.grid(column=0, row=3)
btn2.grid(column=1, row=3)
btn3.grid(column=2, row=3)
btn4.grid(column=0, row=2)
btn5.grid(column=1, row=2)
btn6.grid(column=2, row=2)
btn7.grid(column=0, row=1)
btn8.grid(column=1, row=1)
btn9.grid(column=2, row=1)
btnpunt.grid(column=2, row=4)
btnmas.grid(column=3, row=1)
btnmen.grid(column=3, row=2)
btnpor.grid(column=3, row=3)
btndiv.grid(column=3, row=4)
btnigual.grid(column=3, row=5)
btnclear.grid(column=2, row=5)



root.mainloop()