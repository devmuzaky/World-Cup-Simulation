import tkinter as tk

class intermediateStageScreen(tk.Frame):
    def __init__(self, master, teams, matches, teamHeader, matchHeader, stageName):
        super().__init__(master)
        self.initUI(teams, matches, teamHeader, matchHeader, stageName)

    def initUI(self, teams, matches, teamHeader, matchHeader, stageName):
        btnFrame = tk.Frame(self)
        btnFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        nextButton1 = tk.Button(btnFrame,
                                text='Next',
                                command=self.master.showNextScreen)
        nextButton1.grid(row=0, column=1)
        prevButton1 = tk.Button(btnFrame, text='Prev', command=self.master.showPrevScreen)
        prevButton1.grid(row=0, column=0)

        screenFrame = tk.Frame(self)
        screenFrame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        headerLabel = tk.Label(screenFrame, text=stageName,
                               font=('Helvetica', 16, 'bold'))
        headerLabel.pack(pady=10)

        teams_frame = tk.Frame(screenFrame)
        teams_frame.pack(side="left")
        for i in range(0, len(teams), 4):
            frame = tk.Frame(teams_frame)
            frame.pack(pady=5)

            for j, team in enumerate(teams[i:i + 4]):
                teamLabel = tk.Label(frame, text=team, font=('Helvetica', 14))
                teamLabel.pack(side='left', padx=10)

            if i < len(teams) - 4:
                separator = tk.Frame(teams_frame, height=2, bd=1, relief='sunken')
                separator.pack(fill='x', pady=5)

        header2 = tk.Label(teams_frame, text=teamHeader, font=('Helvetica', 14, 'bold'), bd=1,
                           relief='groove')
        header2.pack(padx=15)

        tableFrame = tk.Frame(screenFrame)
        tableFrame.pack(padx=50)

        for i, match in enumerate(matches):
            rowFrame = tk.Frame(tableFrame)
            rowFrame.pack(pady=5, side='top', fill="x")

            rowFrame.config(bd=1, relief='solid')

            label = tk.Label(rowFrame, text=f'{match[0]} X {match[1]}', padx=5, pady=5)
            label.pack(side='left')

        header2 = tk.Label(tableFrame, text=matchHeader, font=('Helvetica', 14, 'bold'), bd=1,
                           relief='groove')
        header2.pack(padx=15)
