from tkinter import *
import math

def calc(operation):
    global mem
    if operation == 'C':
        mem = '0'
    elif operation == '=':
        mem = str(eval(mem))
    elif operation == 'sin':
        mem = str(math.sin(float(mem)))
    elif operation == 'cos':
        mem = str(math.cos(float(mem)))
    elif operation == 'tan':
        mem = str(math.tan(float(mem)))
    elif operation == 'ctg':
        mem = str(math.log1p(float(mem)))
    elif operation == 'log':
        mem = str(math.log10(float(mem)))
    elif operation == 'ln':
        mem = str(math.log(float(mem)))
    elif operation == 'Bin':
        mem = str(bin(int(mem)))
    else:
        if mem == '0':
            mem = ''
        mem += operation
    label_txt.configure(text=mem)

# Створюємо інтерфейс програми
gui = Tk()
gui.title('Calculator')
gui.geometry('510x650')
gui.resizable(width=False, height=False)
gui.configure(bg='grey18')
# Створюємо усі кнопки
btns = ['C', '/', '*', '=',
        '1', '2', '3', '+',
        '4', '5', '6', '-',
        '7', '8', '9', '0', 'sin', 'cos', 'tan',
        'ctg', 'log', 'ln', '%', 'Bin', ]
x = 20
y = 140
# Надаємо кнопкам вигляд та властивість натискання
for button in btns:
    get_lbl = lambda x = button: calc(x)
    Button(text=button, bg='gold', font=('Helvetica', 20, 'bold'), command=get_lbl).place(x=x, y=y,
                                                                                              width=115,
                                                                                              height=80)
    x += 120
    if x > 400:
        x = 20
        y += 85
mem = '0'
# Надаємо вигляд строці вводу/виводу
label_txt = Label(text=mem, font=('Helvetica', 35, 'bold'), bg='grey18', fg='white')
label_txt.place(x=20, y=50)
gui.mainloop()