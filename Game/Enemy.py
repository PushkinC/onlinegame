from tkinter import Canvas



class Enemy:
    def __init__(self, canvas: Canvas, color: str, pos: [int, int], id:str, size:int, name='bot'):
        self.canvas = canvas
        self.color = color
        self.pos = pos
        self.name = name
        self.id = id
        self.size = size
        self.object = self.canvas.create_oval(self.pos[0], self.pos[1], self.pos[0] + self.size, self.pos[1] + self.size, fill=self.color)

    def move(self, x, y):
        self.pos = [self.pos[0] + x, self.pos[1] + y]

    def set_pos(self, x, y):
        self.pos = [x, y]




class Enemyes(list):
    def remove(self, __value: Enemy) -> None:
        __value.canvas.delete(__value.object)
        super().remove(__value)