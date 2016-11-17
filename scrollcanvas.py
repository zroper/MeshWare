	
##Overview
##
##Create a canvas widget and associate the scrollbars with that widget. Then, into that canvas embed the frame that contains your label widgets. Determine the width/height of the frame and feed that into the canvas scrollregion option so that the scrollregion exactly matches the size of the frame.
##
##Drawing the text items directly on the canvas isn't very hard, so you might want to reconsider that approach if the frame-embedded-in-a-canvas solution seems too complex. Since you're creating a grid, the coordinates of each text item is going to be very easy to compute, especially if each row is the same height (which it probably is if you're using a single font).
##
##For drawing directly on the canvas, just figure out the line height of the font you're using (and there are commands for that). Then, each y coordinate is row*(lineheight+spacing). The x coordinate will be a fixed number based on the widest item in each column. If you give everything a tag for the column it is in, you can adjust the x coordinate and width of all items in a column with a single command.

##Object-oriented solution
##
##Here's an example of the frame-embedded-in-canvas solution, using an object-oriented approach:

from tkinter import *
from tkinter import ttk

class ScrollCanvas(Frame):
    def __init__(self, root):

        Frame.__init__(self, root)
        self.canvas = Canvas(root, borderwidth=0, background="pink")
        self.frame0 = ttk.Frame(self.canvas)
        self.pw = ttk.Panedwindow(self.frame0, orient = HORIZONTAL)
        self.pw.pack(fill = 'x', expand = True)
        self.frame1 = ttk.Frame(self.pw)
        self.frame2 = ttk.Frame(self.pw)        
        self.vsb = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.hsb = Scrollbar(root, orient="horizontal", command=self.canvas.xview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.canvas.configure(xscrollcommand=self.hsb.set)
        
        self.vsb.pack(side="right", fill="y")
        self.hsb.pack(side="bottom", fill="x")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((0,0), window=self.frame0, anchor="nw", 
                                  tags="self.pw")
        self.pw.add(self.frame1, weight = 1)
        self.pw.add(self.frame2, weight = 4)
        
        self.frame0.bind("<Configure>", self.onFrameConfigure)
        self.frame0.bind('<Enter>', self._bound_to_mousewheel)
        self.frame0.bind('<Leave>', self._unbound_to_mousewheel)
        
        self.populate()

    def _bound_to_mousewheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel_y)   
        #self.canvas.bind_all("<Shift-MouseWheel>", self._on_mousewheel_x)   

    def _unbound_to_mousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>") 
        
    def _on_mousewheel_y(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

##    def _on_mousewheel_x(self, event):
##        self.canvas.xview_scroll(int(-1*(event.delta/120)), "units")        

    def populate(self):
        '''Put in some fake data'''
        for line in range(100):
           button = ttk.Button(self.frame1,
                    text = ("This is button number " + str(line)),
                    style = 'grey.TButton')
           button.pack(expand = True)
        for line in range(100):
           button = ttk.Button(self.frame2,
                    text = ("This is button number " + str(line)),
                    style = 'grey.TButton')
           button.pack(expand = True)
        for line in range(100):
           button = ttk.Button(self.frame2,
                    text = ("This is button number " + str(line)),
                    style = 'grey.TButton')
           button.pack(side = 'right', expand = True)           
##        for row in range(100):
##            Label(self.frame, text="%s" % row, width=3, borderwidth="1", 
##                     relief="solid").grid(row=row, column=0)
##            t="this is the second column for row %s" %row
##            Label(self.frame, text=t).grid(row=row, column=1)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    root=Tk()
    root.title('Button Scroller')
    root.resizable(True, True)
    root.configure(background = 'grey', padx = 10, pady = 10, relief = SUNKEN)
    sizex = 180
    sizey = 500
    posx  = 0
    posy  = 0
    root.geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))    
    ScrollCanvas(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

##from tkinter import *
##
### This example program creates a scroling canvas, and demonstrates
### how to tie scrollbars and canvses together. The mechanism
### is analogus for listboxes and other widgets with
### "xscroll" and "yscroll" configuration options.
##
##class Test(Frame):
##    def printit(self):
##        print("hi")
##
##    def createWidgets(self):
##        self.question = Label(self, text="Can Find The BLUE Square??????")
##        self.question.pack()
##
##        self.QUIT = Button(self, text='QUIT', background='red',
##                           height=3, command=self.quit)
##        self.QUIT.pack(side=BOTTOM, fill=BOTH)
##        spacer = Frame(self, height="0.25i")
##        spacer.pack(side=BOTTOM)
##
##        # notice that the scroll region (20" x 20") is larger than
##        # displayed size of the widget (5" x 5")
##        self.draw = Canvas(self, width="5i", height="5i",
##                           background="white",
##                           scrollregion=(0, 0, "20i", "20i"))
##
##        self.draw.scrollX = Scrollbar(self, orient=HORIZONTAL)
##        self.draw.scrollY = Scrollbar(self, orient=VERTICAL)
##
##        # now tie the three together. This is standard boilerplate text
##        self.draw['xscrollcommand'] = self.draw.scrollX.set
##        self.draw['yscrollcommand'] = self.draw.scrollY.set
##        self.draw.scrollX['command'] = self.draw.xview
##        self.draw.scrollY['command'] = self.draw.yview
##
##        # draw something. Note that the first square
##        # is visible, but you need to scroll to see the second one.
##        self.draw.create_rectangle(0, 0, "3.5i", "3.5i", fill="black")
##        self.draw.create_rectangle("10i", "10i", "13.5i", "13.5i", fill="blue")
##
##        # pack 'em up
##        self.draw.scrollX.pack(side=BOTTOM, fill=X)
##        self.draw.scrollY.pack(side=RIGHT, fill=Y)
##        self.draw.pack(side=LEFT)
##
##
##    def scrollCanvasX(self, *args):
##        print("scrolling", args)
##        print(self.draw.scrollX.get())
##
##
##    def __init__(self, master=None):
##        Frame.__init__(self, master)
##        Pack.config(self)
##        self.createWidgets()
##
##test = Test()
##
##test.mainloop()
##
##
####from tkinter import *
####
####root = Tk()
####
####w = Canvas(root, width=100, height=100,
####           borderwidth=0,
####           highlightthickness=0,
####           background='gold'
####          )
####w.pack(padx=10,pady=10)
####w.config(scrollregion=[0,0,400,400])
####frame = Frame(w, relief = SUNKEN, bg = 'black')
####w.create_window(0,0, anchor = NW, window = frame)
####
####frame.pack()
####label = Label(frame, text = '      Subtasks      ', justify = 'center')
####label.config(bg = 'white', fg = 'green')
####label.pack(side = LEFT)
####label2 = Label(frame, text = '      Subtasks      ', justify = 'center')
####label2.config(bg = 'white', fg = 'green')
####label2.pack(side = LEFT)
######label3 = Label(frame, text = '      Subtasks      ', justify = 'center')
######label3.config(bg = 'white', fg = 'green')
######label3.pack(side = LEFT)
######label4 = Label(frame, text = '      Subtasks      ', justify = 'center')
######label4.config(bg = 'white', fg = 'green')
######label4.pack(side = LEFT)
######label5 = Label(frame, text = '      Subtasks      ', justify = 'center')
######label5.config(bg = 'white', fg = 'green')
######label5.pack(side = LEFT)
####hbar=Scrollbar(w,orient=HORIZONTAL)
####hbar.pack(side=BOTTOM,fill=X)
####hbar.config(command=w.xview)
####w.config(xscrollcommand=hbar.set)
##
##
####from tkinter import *
####from tkinter import ttk
####root=Tk()
####frame=Frame(root,width=300,height=300)
####frame.pack()
####canvas=Canvas(frame,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,500,500))
####ProgressbarPanes = Frame(canvas,width=5,height=5)
####ProgressbarPanes.pack()
####progress_tab_label = Label(ProgressbarPanes, text = 'Welcome to the Progress tab', foreground = 'gold', background = 'black')
####progress_tab_label.pack()
####hbar=Scrollbar(frame,orient=HORIZONTAL)
####hbar.pack(side=BOTTOM,fill=X)
####hbar.config(command=canvas.xview)
####vbar=Scrollbar(frame,orient=VERTICAL)
####vbar.pack(side=RIGHT,fill=Y)
####vbar.config(command=canvas.yview)
####canvas.config(width=50,height=50)
####canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
####canvas.pack(side=LEFT)
####
####root.mainloop()
