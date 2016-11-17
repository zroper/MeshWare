import tkinter as tk

class ScrollFrame(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        # Start up self
        tk.Frame.__init__(self, root, *args, **kwargs)
        # Put a canvas in the frame (self), along with scroll bars
        self.canvas = tk.Canvas(self)
        self.horizontal_scrollbar = tk.Scrollbar(
            self, orient="horizontal", command=self.canvas.xview
            )
        self.vertical_scrollbar = tk.Scrollbar(
            self, orient="vertical", command=self.canvas.yview
            )
        self.canvas.configure(
            yscrollcommand=self.vertical_scrollbar.set,
            xscrollcommand=self.horizontal_scrollbar.set
            )
        # Put a frame in the canvas, to hold all the widgets
        self.inner_frame = tk.Frame(self.canvas)
        # Pack the scroll bars and the canvas (in self)
        self.horizontal_scrollbar.pack(side="bottom", fill="x")
        self.vertical_scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((0,0), window=self.inner_frame, anchor="nw")
        self.inner_frame.bind("<Configure>", self.OnFrameConfigure)

    def OnFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

root = tk.Tk()
frame = ScrollFrame(root, borderwidth=2, relief="sunken")
labels = []
for i in range(20):
    labels.append(
        tk.Label(
            frame.inner_frame, text="Row {}".format(i) + "_"*20
            ) # Unfortunately, this widget's parent cannot just be frame but has to be frame.inner_frame
        )
frame.place(x=20, y=20, width=150, height=150)

for i,label in enumerate(labels):
    label.grid(row=i,column=0)
    #label.place(x=0, y=20*i, width=100, height=20)
root.mainloop()
