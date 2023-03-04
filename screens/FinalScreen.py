import tkinter as tk


class FinalScreen(tk.Frame):
    def __init__(self, master, final_teams, third_place_teams):
        super().__init__(master)
        self.initUI(final_teams, third_place_teams)

    def initUI(self, final_teams, third_place_teams):
        btnFrame = tk.Frame(self)
        btnFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        nextButton4 = tk.Button(btnFrame, text='Next', command=self.master.showNextScreen)
        nextButton4.grid(row=1, column=1)
        prevButton4 = tk.Button(btnFrame, text='Prev', command=self.master.showPrevScreen)
        prevButton4.grid(row=1, column=0)

        # Create a frame
        screenFrame = tk.Frame(self)
        screenFrame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        # Create and display the header label
        headerLabel = tk.Label(screenFrame, text='Finals',
                               font=('Helvetica', 16, 'bold'))
        headerLabel.pack(pady=10)

        final_frame = tk.Frame(screenFrame)
        final_frame.pack(pady=5)
        header2 = tk.Label(final_frame, text="Final: ", font=('Helvetica', 14, 'bold'), bd=1,
                           relief='groove')
        header2.pack(side='left', padx=15)

        teamLabel = tk.Label(final_frame, text="{} X {}".format(final_teams[0], final_teams[1]), font=('Helvetica', 14))
        teamLabel.pack(side='left', padx=10)

        separator = tk.Frame(screenFrame, height=2, bd=1, relief='sunken')
        separator.pack(fill='x', pady=5)

        third_place_frame = tk.Frame(screenFrame)
        third_place_frame.pack(pady=20)
        header3 = tk.Label(third_place_frame, text="Third Place: ", font=('Helvetica', 14, 'bold'), bd=1,
                           relief='groove')
        header3.pack(side='left', padx=15)
        teamLabel = tk.Label(third_place_frame, text="{} X {}".format(third_place_teams[0], third_place_teams[1]),
                             font=('Helvetica', 14))
        teamLabel.pack(side='left', padx=10)
