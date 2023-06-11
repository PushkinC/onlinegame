from tkinter import ttk
import tkinter as tk
import json


def btn_click():
    with open('../Saves/SettingsData.json', 'w') as f:
        data = {
            'URL': inp_URL.get(),
            'FPS': int(inp_FPS.get()),
            'width': int(inp_width.get()),
            'height': int(inp_height.get())
        }
        json.dump(data, f)

    with open('../Saves/PlayerData.json', 'w') as f:
        data = {
            'name': inp_name.get(),
            'weapon': inp_weapon.get(),
            'color': 'RANDOM'
        }
        json.dump(data, f)

    app.destroy()


with open('../Saves/SettingsData.json', 'rt') as f:
    SettingsData = json.load(f)
with open('../Saves/PlayerData.json', 'rt') as f:
    PlayerData = json.load(f)
with open('../Weapons/Weapons.json', 'rt') as f:
    lst_Weapons = json.load(f)

app = tk.Tk()
app.geometry('500x500')

frame1 = ttk.Frame(app)
frame1.pack(fill='x')

label_URL = ttk.Label(frame1, text='Введите URL:')
label_URL.pack(side=tk.LEFT, padx=5, pady=5)
inp_URL = ttk.Entry(frame1)
inp_URL.insert(0, SettingsData['URL'])
inp_URL.pack(fill='x', padx=5, expand=True)

frame2 = ttk.Frame(app)
frame2.pack(fill='x')

label_FPS = ttk.Label(frame2, text='Введите FPS:')
label_FPS.pack(side=tk.LEFT, padx=5, pady=5)
inp_FPS = ttk.Entry(frame2)
inp_FPS.insert(0, SettingsData['FPS'])
inp_FPS.pack(fill='x', padx=5, expand=True)

frame4 = ttk.Frame(app)
frame4.pack(fill='x')

label_width = ttk.Label(frame4, text='Введите ширину экрана:')
label_width.pack(side=tk.LEFT, padx=5, pady=5)
inp_width = ttk.Entry(frame4)
inp_width.insert(0, SettingsData['width'])
inp_width.pack(fill='x', padx=5, expand=True)

frame5 = ttk.Frame(app)
frame5.pack(fill='x')

label_height = ttk.Label(frame5, text='Введите высоту экрана:')
label_height.pack(side=tk.LEFT, padx=5, pady=5)
inp_height = ttk.Entry(frame5)
inp_height.insert(0, SettingsData['height'])
inp_height.pack(fill='x', padx=5, expand=True)

frame3 = ttk.Frame(app)
frame3.pack(fill='x')

label_name = ttk.Label(frame3, text='Введите имя:')
label_name.pack(side=tk.LEFT, padx=5, pady=5)
inp_name = ttk.Entry(frame3)
inp_name.insert(0, PlayerData['name'])
inp_name.pack(fill='x', padx=5, expand=True)

frame6 = ttk.Frame(app)
frame6.pack(fill='x')

label_name = ttk.Label(frame6, text='Выберите оружие:')
label_name.pack(side=tk.LEFT, padx=5, pady=5)
inp_weapon = ttk.Combobox(frame6, values=list(lst_Weapons.keys()), state='readonly')
inp_weapon.set(list(lst_Weapons.keys())[0])
inp_weapon.pack(fill='x', padx=5, expand=True)






accept_btn = ttk.Button(app, command=btn_click)
accept_btn['text'] = 'Начать'

accept_btn.pack()

app.mainloop()
