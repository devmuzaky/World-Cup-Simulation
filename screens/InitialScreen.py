import tkinter as tk


class InitialScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.canvas = tk.Canvas(self, width=1000, height=500, bg="white")
        self.canvas.pack()

        self.x = 500
        self.y = 200

        self.font = ("Helvetica", 24, "bold")
        self.color = "black"

        self.text = "World Cup Simulation"
        self.delay = 100

        self.index = 0

        self.width = 1000
        self.height = 500
        self.x = 10
        self.y = 250

        self.direction = 5

        self.count = 10
        self.animate_background()

    def write_text(self):
        if self.index == 0:
            self.width = 1000
            self.height = 500
            self.x = 200
            self.y = 200
        self.canvas.create_text(self.x, self.y, text=self.text[self.index], font=self.font, fill=self.color)

        self.x += 25

        self.index += 1

        if self.index < len(self.text):
            self.after(self.delay, self.write_text)
        else:
            self.after(1000, self.master.showNextScreen)

    def animate_background(self):
        if self.width < 1800:
            self.width += self.direction
            self.height += self.direction
            self.x -= self.direction / 2
            self.y -= self.direction / 2

        self.canvas.create_arc(self.x, self.y, self.x + self.width, self.y + self.height, start=0, extent=180, width=2,
                               fill="yellow")

        if self.width >= 1800:
            self.write_text()
        else:
            self.after(1, self.animate_background)
