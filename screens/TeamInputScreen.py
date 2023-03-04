import random
import tkinter as tk
import tkinter.messagebox as messagebox
from string import ascii_letters


class TeamInputScreen(tk.Frame):
    def __init__(self, master):
        self.clicked = []
        super().__init__(master)
        self.initUI()

    def initUI(self):
        inputFrame = tk.Frame(self)
        inputFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.teamFields = []
        for i in range(1, 33):
            row = (i - 1) // 4
            col = (i - 1) % 4

            rankLabel = tk.Label(inputFrame, text=f'Team {i}:')
            rankLabel.grid(row=row, column=col * 2, padx=5, pady=5)
            teamField = tk.Entry(inputFrame)
            teamField.insert(0, "name, ranks")

            on_click_id = teamField.bind('<Button-1>', lambda event, teamField=teamField : self.on_click(event, teamField))
            teamField.grid(row=row, column=col * 2 + 1, padx=5, pady=5)
            self.teamFields.append(teamField)

        randomButton = tk.Button(inputFrame, text='Generate Random Values', command=self.generateRandom)
        randomButton.grid(row=8, column=0, padx=5, pady=5)

        submitButton = tk.Button(inputFrame, text='Submit', command=self.submit)
        submitButton.grid(row=8, column=1, columnspan=8, padx=5, pady=5)

    def generateRandom(self):
        # Generate a list of random team names that are unique
        names = ['Spain', 'Germany', 'Brazil', 'Argentina', 'France', 'Italy', 'England', 'Netherlands', 'Portugal', 'Belgium', 'Croatia', 'Switzerland', 'Poland', 'Denmark', 'Mexico', 'Uruguay', 'Colombia', 'Chile', 'USA', 'Peru', 'Ecuador', 'Paraguay', 'Bolivia', 'Venezuela', 'Honduras', 'Costa Rica', 'Panama', 'Jamaica', 'Trinidad and Tobago', 'Haiti', 'Canada', 'Cuba']
        random.shuffle(names)
        ranks = [i + 1 for i in range(32)]
        random.shuffle(ranks)

        for i, field in enumerate(self.teamFields):
            field.delete(0, tk.END)
            field.insert(0, f"{names[i]}, {ranks[i]}")


    def on_click(self, event, entry):
        should_return = entry in self.clicked

        if should_return:
            return

        self.clicked.append(entry)

        entry.delete(0, 'end')

    def submit(self):
        teams = []
        for field in self.teamFields:
            team, points = field.get().split(',')
            teams.append([team, int(points)])

        if len(set([l[0] for l in teams])) != 32:
            messagebox.showerror('Error', 'Please enter 32 unique team names.')
        else:
            for field in self.teamFields:
                field.delete(0, tk.END)

            teams = {team[0]: team[1] for team in teams}

            self.master.showNextScreen(teams)
