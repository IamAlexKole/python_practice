import http.client
import json
from tkinter import *
import tkinter as tk

# Створення інтерфейсу вікна
gui = Tk()
gui.title("Covid Status Info")
gui.geometry('450x500')
gui.resizable(0, 0)
gui['bg']='grey18'

# Кількість(змінна) країн, про які інформацію программа витягує з сайту
n=5

conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
headers = {
    'x-rapidapi-key': "e36cf147d2msh773e180e52d7742p1f4ad1jsnd148121bd4cf",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

conn.request("GET", "/api/npm-covid-data/europe", headers=headers)
res = conn.getresponse()
data = res.read()
info = data.decode("utf-8")
json = json.loads(info)

# Розбиття інтерфейсу на зручні блоки
frametop = Frame(gui)
framebot = Frame(gui)
frametop.pack()
framebot.pack()

# Функція оновлення, стирає усе в полі інформації і замінюється актуальною у певний момент часу
def Refresh():
    import json
    TextBox.delete(1.0,END)
    conn.request("GET", "/api/npm-covid-data/europe", headers=headers)
    res = conn.getresponse()
    data = res.read()
    info = data.decode("utf-8")
    json = json.loads(info)
    TextBox.insert('1.0', '\n')
    for i in range(n):
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', list(json[i].items())[14])
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', list(json[i].items())[12])
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', list(json[i].items())[10])
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', list(json[i].items())[3])
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', list(json[i].items())[2])
        TextBox.insert('1.0', '\n')

# Створення кнопки-функції "оновлення"
Refreshbutton = Button(frametop, text="REFRESH",command=Refresh)
Refreshbutton['bg']='red'
Refreshbutton['fg']='#fff'
Refreshbutton.pack(side=LEFT)

# Перевірка наявності вказаної за пошуком країни в json. У разі успіху, інфо про країну виводиться на верх списку
def Search():
    j=0
    for i in range(n):
        InputedCountry = EntryCountry.get()
        GetCountry = json[i].get('Country')
        if InputedCountry == GetCountry:
                TextBox.insert('1.0', '\n')
                TextBox.insert('1.0', json[i].get('TotalRecovered'))
                TextBox.insert('1.0', 'TotalRecovered : ')
                TextBox.insert('1.0', '\n')
                TextBox.insert('1.0', json[i].get('TotalDeaths'))
                TextBox.insert('1.0', 'TotalDeaths : ')
                TextBox.insert('1.0', '\n')
                TextBox.insert('1.0', json[i].get('TotalCases'))
                TextBox.insert('1.0', 'TotalCases : ')
                TextBox.insert('1.0', '\n')
                TextBox.insert('1.0', json[i].get('Continent'))
                TextBox.insert('1.0', 'Continent : ')
                TextBox.insert('1.0', '\n')
                TextBox.insert('1.0', json[i].get('Country'))
                TextBox.insert('1.0', 'Country : ')
                TextBox.insert('1.0', '\n')
                TextBox.insert('1.0', '\t\t     ***Found!***')
                TextBox.insert('1.0', '\n\n')
        else : j+=1
        if j==20:
            TextBox.insert('1.0', '\n')
            TextBox.insert('1.0', '\n')
            TextBox.insert('1.0', '\t\t      ***Not found!***')
            TextBox.insert('1.0', '\n')

# Створення поля для введення
EntryCountry = Entry(frametop, width=54, borderwidth=6)
EntryCountry['bg']='white'
EntryCountry['fg']='black'
EntryCountry.pack(side=LEFT)

# Створення кнопки-функції "пошуку"
Searchbutton = Button(frametop, text="SEARCH", command=Search)
Searchbutton.pack(side=LEFT)
Searchbutton['bg']='red'
Searchbutton['fg']='#fff'

# Створення поля-блоку для виведення інформації
TextBox = Text(framebot,width=500, height=500)
TextBox['bg']='grey15'
TextBox['fg']='#fff'
TextBox.pack()

# Перший виклик функції для заповнення при запуску
Refresh()
gui.mainloop()