import tkinter as tk
import json


def btn_click():
    with open('Saves/OpenSettings.json', 'w') as f:
        data = {'URL': inp_URL.get(), 'FPS': int(inp_FPS.get()), 'name': inp_name.get()}
        json.dump(data, f)
    app.destroy()


with open('Saves/OpenSettings.json', 'rt') as f:
    data = json.load(f)


app = tk.Tk()
app.geometry('500x500')



frame1 = tk.Frame(app)
frame1.pack(fill='x')

label_URL = tk.Label(frame1, text='Введите URL:')
label_URL.pack(side=tk.LEFT, padx=5, pady=5)
inp_URL = tk.Entry(frame1)
inp_URL.insert(0, data['URL'])
inp_URL.pack(fill='x', padx=5, expand=True)

frame2 = tk.Frame(app)
frame2.pack(fill='x')

label_FPS = tk.Label(frame2, text='Введите FPS:')
label_FPS.pack(side=tk.LEFT, padx=5, pady=5)
inp_FPS = tk.Entry(frame2)
inp_FPS.insert(0, data['FPS'])
inp_FPS.pack(fill='x', padx=5, expand=True)

frame3 = tk.Frame(app)
frame3.pack(fill='x')

label_name = tk.Label(frame3, text='Введите имя:')
label_name.pack(side=tk.LEFT, padx=5, pady=5)
inp_name = tk.Entry(frame3)
inp_name.insert(0, data['name'])
inp_name.pack(fill='x', padx=5, expand=True)






accept_btn = tk.Button(app, command=btn_click)
accept_btn['text'] = 'Начать'


accept_btn.pack()

app.mainloop()
