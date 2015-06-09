# -*- coding: utf-8 -*-
from Tkinter import *
from processor import *
from functools import partial
import threading


class LifeGUI:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.prev_x = self.prev_y = None
        self.root = Tk()
        self.field = init_field(height=self.height, width=self.width)
        self.canvas = Canvas(self.root, width=10 * len(self.field[0]), height=10 * len(self.field))
        self.clear()
        self.next_button = Button(self.root, bg="blue", text="step", command=self.step)
        self.next_button.pack()
        self.clear_button = Button(self.root, bg="yellow", text="clean", command=self.clear)
        self.clear_button.pack()
        self.clear_button = Button(self.root, bg="green", text="play", command=partial(self.step, {'repeat': True}))
        self.clear_button.pack()
        self.clear_button = Button(self.root, bg="red", text="stop", command=self.stop)
        self.clear_button.pack()
        self.canvas.bind("<Button-1>", self.switch_cell)
        self.canvas.bind("<B1-Motion>", self.switch_cell)
        self.canvas.bind("<ButtonRelease-1>", self.forget)
        self.canvas.pack()
        self.timer = threading.Timer(0.1, partial(self.step, {'repeat': True}))
        self.root.mainloop()

    def switch_cell(self, event):
        x = event.x / 10
        y = event.y / 10
        if (self.prev_x, self.prev_y) != (x, y):
            self.field[y][x] = not self.field[y][x]
            self.redraw()
        self.prev_x, self.prev_y = x, y

    def forget(self, event):
        self.prev_y = self.prev_x = None

    def step(self, repeat=False):
        self.field = next_step(self.field)
        self.redraw()
        if repeat:
            self.timer = threading.Timer(0.1, partial(self.step, {'repeat': True}))
            self.timer.start()

    def stop(self):
        self.timer.cancel()
        self.timer = None

    def clear(self):
        self.field = init_field(height=self.height, width=self.width)
        self.redraw()

    def redraw(self):
        self.canvas.delete("all")
        for i in range(len(self.field)):
            for j in range(len(self.field[0])):
                self.canvas.create_rectangle(j * 10, i * 10, (j + 1) * 10 - 2, (i + 1) * 10 - 2, fill="blue" if self.field[i][j] else "orange")



def main():

    LifeGUI(40, 40)

if __name__ == '__main__':
    main()