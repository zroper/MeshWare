import tkinter as tk

class ScrollFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, background='blue')

        # self lays out a canvas and, when necessary, vertical and
        # horizontal scrollbars; inside the canvas there is a frame
        # where the contents of the scroll frame should be placed 
        canvas = tk.Canvas(self)
        self.frame = frame = tk.Frame(canvas)
        frameid = canvas.create_window(0, 0, window=frame,
                                       anchor=tk.NW)

        vbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        hbar = tk.Scrollbar(self, orient=tk.HORIZONTAL)
        vbar.config(command=canvas.yview)
        hbar.config(command=canvas.xview)
        canvas.config(yscrollcommand=vbar.set,
                      xscrollcommand=hbar.set)

        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        def frameConfigure(e):
            # set the canvas scrollregion to the requested size of
            # the inside frame
            framew = frame.winfo_reqwidth()
            frameh = frame.winfo_reqheight()
            bbox = (0, 0, framew, frameh)
            canvas.config(scrollregion = bbox)

            # grid the scroll bars as necessary
            vbar.grid_forget()
            hbar.grid_forget()
            canvasw = canvas.winfo_width()
            canvash = canvas.winfo_height()
            if frameh > canvash:
                vbar.grid(row=0, column=1, sticky='ns')
            if framew > canvasw:
                hbar.grid(row=1, column=0, sticky='we')

        frame.bind('<Configure>', frameConfigure)

        # the canvas occupies the top left grid cell;
        # the v/h scrollbars are grided respectively right/below
        # the canvas
        canvas.grid(row=0, column=0, sticky='nesw') 
        self.rowconfigure(index=0, weight=1)
        self.columnconfigure(index=0, weight=1)

    def getFrame(self):
        return self.frame

if __name__ == "__main__":
    root = tk.Tk()

    sf = ScrollFrame(root)
    f = sf.getFrame()

    labels = map(lambda n: tk.Label(f, text='Label'+str(n)+'--'*n),
                 range(20))
    for l in labels:
        l.pack(anchor='w')

    sf.pack(fill=tk.BOTH, expand=True)
