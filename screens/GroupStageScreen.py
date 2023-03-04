import tkinter as tk


class GroupStageScreen(tk.Frame):
    def __init__(self, master, data1, data2):
        super().__init__(master)
        self.initUI(data1, data2)

    def initUI(self, data1, data2):
        btnFrame = tk.Frame(self)
        btnFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        nextButton0 = tk.Button(btnFrame,
                                text='Next',
                                command=self.master.showNextScreen)
        nextButton0.grid(row=0, column=1)
        prevButton0 = tk.Button(btnFrame, text='Prev', command=self.master.showPrevScreen)
        prevButton0.grid(row=0, column=0)

        # Create a frame
        screenFrame = tk.Frame(self)
        screenFrame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        headerLabel = tk.Label(screenFrame, text='group_stage teams',
                               font=('Helvetica', 16, 'bold'))
        headerLabel.pack(pady=10)

        table1Frame = tk.Frame(screenFrame)
        table1Frame.pack(padx=50, side="left")

        for i, row in enumerate(data1):
            rowFrame = tk.Frame(table1Frame)
            rowFrame.pack(pady=5, side='top', fill="x")

            rowFrame.config(bd=1, relief='solid')

            for j, item in enumerate(row):
                label = tk.Label(rowFrame, text=item, padx=5, pady=5)
                label.pack(side='left')

        header1 = tk.Label(table1Frame, text='Dividing teams By Rank', font=('Helvetica', 14, 'bold'), bd=1,
                           relief='groove')
        header1.pack(pady=5)

        table2Frame = tk.Frame(screenFrame)
        table2Frame.pack(pady=10, side="left")

        for i, row in enumerate(data2):
            # Create a frame for the row
            rowFrame = tk.Frame(table2Frame)
            rowFrame.pack(pady=5, side='top', fill="x")

            # Add a border around the entire row frame
            rowFrame.config(bd=1, relief='solid')

            # Add the items in the row
            for j, item in enumerate(row):
                label = tk.Label(rowFrame, text=item, padx=5, pady=5)
                label.pack(side='left')

        header2 = tk.Label(table2Frame, text='Dividing teams into groups', font=('Helvetica', 14, 'bold'), bd=1,
                           relief='groove')
        header2.pack(pady=5)
