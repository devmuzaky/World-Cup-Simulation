import tkinter as tk


class WinnerScreen(tk.Frame):
    def __init__(self, master, winner, second, third):
        super().__init__(master)
        self.initUI(winner, second, third)

    def initUI(self, winner, second, third):
        btnFrame = tk.Frame(self)
        btnFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        prevButton5 = tk.Button(btnFrame, text='Prev', command=self.master.showPrevScreen)
        prevButton5.grid(row=1, column=0)
        resetButton = tk.Button(btnFrame, text='Reset', command=self.master.resetScreen)
        resetButton.grid(row=1
                         , column=1)

        canvasFrame = tk.Frame(self)
        canvasFrame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        canvas = tk.Canvas(canvasFrame, width=300, height=350)
        canvas.grid(row=0, column=0)

        canvas.create_line(150, 105, 75, 200)
        canvas.create_line(150, 105, 225, 250)
        canvas.create_text(50, 45, text="Winners", font=('Helvetica', 16, 'bold'), fill='black')
        canvas.create_text(150, 75, text=f"1. {winner}", font=('Helvetica', 16, 'bold'), fill='black')
        canvas.create_text(75, 245, text=f"2. {second}", font=('Helvetica', 16, 'bold'), fill='black')
        canvas.create_text(225, 295, text=f"3. {third}", font=('Helvetica', 16, 'bold'), fill='black')
