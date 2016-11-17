            #------------------ MeshWare Console ------------------#
                # Concept & Design      : Zachary J.J. Roper    #
                # Coding Commenced      : 2016-02-10            #
                # Coding Completed      : xxxx-xx-xx            #
                #-----------------------------------------------#
                
##                                    ud$$$**$$$$$$$bc.                          
##                                  u@**"        4$$$$$$$Nu                       
##                                J                ""#$$$$$$r                     
##                               @                       $$$$b                    
##                             .F                        ^*3$$$                   
##                            :% 4                         J$$$N                  
##                            $  :F                       :$$$$$                  
##                           4F  9                       J$$$$$$$                 
##                           4$   k             4$$$$bed$$$$$$$$$                 
##                           $$r  'F            $$$$$$$$$$$$$$$$$r                
##                           $$$   b.           $$$$$$$$$$$$$$$$$N                
##                           $$$$$k 3eeed$$b    $$$Euec."$$$$$$$$$                
##            .@$**N.        $$$$$" $$$$$$F'L $$$$$$$$$$$  $$$$$$$                
##            :$$L  'L       $$$$$ 4$$$$$$  * $$$$$$$$$$F  $$$$$$F         edNc   
##           @$$$$N  ^k      $$$$$  3$$$$*%   $F4$$$$$$$   $$$$$"        d"  z$N  
##           $$$$$$   ^k     '$$$"   #$$$F   .$  $$$$$c.u@$$$          J"  @$$$$r 
##           $$$$$$$b   *u    ^$L            $$  $$$$$$$$$$$$u@       $$  d$$$$$$ 
##            ^$$$$$$.    "NL   "N. z@*     $$$  $$$$$$$$$$$$$P      $P  d$$$$$$$ 
##               ^"*$$$$b   '*L   9$E      4$$$  d$$$$$$$$$$$"     d*   J$$$$$r   
##                    ^$$$$u  '$.  $$$L     "#" d$$$$$$".@$$    .@$"  z$$$$*"     
##                      ^$$$$. ^$N.3$$$       4u$$$$$$$ 4$$$  u$*" z$$$"          
##                        '*$$$$$$$$ *$b      J$$$$$$$b u$$P $"  d$$P             
##                           #$$$$$$ 4$ 3*$"$*$ $"$'c@@$$$$ .u@$$$P               
##                             "$$$$  ""F~$ $uNr$$$^&J$$$$F $$$$#                 
##                               "$$    "$$$bd$.$W$$$$$$$$F $$"                   
##                                 ?k         ?$$$$$$$$$$$F'*                     
##                                  9$$bL     z$$$$$$$$$$$F                       
##                                   $$$$    $$$$$$$$$$$$$                        
##                                    '#$$c  '$$$$$$$$$"                          
##                                     .@"#$$$$$$$$$$$$b                          
##                                   z*      $$$$$$$$$$$$N.                       
##                                 e"      z$$"  #$$$k  '*$$.                     
##                             .u*      u@$P"      '#$$c   "$$c                   
##                      u@$*"""       d$$"            "$$$u  ^*$$b.               
##                    :$F           J$P"                ^$$$c   '"$$$$$$bL        
##                   d$$  ..      @$#                      #$$b         '#$       
##                   9$$$$$$b   4$$                          ^$$k         '$      
##                    "$$6""$b u$$                             '$    d$$$$$P      
##                      '$F $$$$$"                              ^b  ^$$$$b$       
##                       '$W$$$$"                                'b@$$$$"         
##                                                                ^$$$*


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.font
import os
import webbrowser
import ast
import datetime
import uuid
import collections
import calendar
import time
from PIL import Image, ImageTk


path = ('C:\\Users\\Zachary Roper\\Desktop\\MeshWare')
os.chdir(path)

def get_calendar(locale, fwday):
    # instantiate proper calendar class
    if locale is None:
        return calendar.TextCalendar(fwday)
    else:
        return calendar.LocaleTextCalendar(fwday, locale)
    
class Load_Dict:
    
    def __init__(self):
        
        verbsraw = open('action_verbs.txt','r')
        verbsraw.readlines()
        verbs = [verb.strip().lower() for verb in verbsraw]
        verbsraw.close()
        global verb_dict
        verb_dict = dict.fromkeys(verbs)
        verb_dict = {}
        global test_verb_dict
        test_verb_dict = {}
##        test_verb_dict = {'invest':{'TSLA',
##                                    'BTC',
##                                    }, 
##                         'run':{'Tues',
##                                '5 miles'
##                                },
##                         'write':{'abstract': {'length':'300 words', 
##                                               'dedline':'Wed'
##                                               },
##                                  'manuscript':{'methods',
##                                                'intro',
##                                                'results',
##                                                'discussion'
##                                                }
##                                  },
##                         'code':{'experiment',
##                                 'button factory'
##                                 },
##                         'eat':{'buy': {'eggs',
##                                        'milk'
##                                        },
##                                'cook':{'ziti', 
##                                        'steaks'
##                                        }
##                                },
##                         'play':{'ukulele',
##                                 'heros',
##                                 }
##                         }

    def Load_Button_Values(input_dict):
    
        button_syles_list = ('grey', 'gold', 'red', 'green')
        
        style_grey = ttk.Style()
        style_grey.theme_use("default")
        style_grey.configure("grey.TButton",
                             foreground="white",
                             background="grey")
        style_gold = ttk.Style()
        style_gold.theme_use("default")
        style_gold.configure("gold.TButton",
                             foreground="black",
                             background="yellow")
        style_red = ttk.Style()
        style_red.theme_use("default")
        style_red.configure("red.TButton",
                            foreground="black",
                            background="red")
        style_green = ttk.Style()
        style_green.theme_use("default")
        style_green.configure("green.TButton",
                            foreground="black",
                            background="green2")
        style_orange = ttk.Style()
        style_orange.theme_use("default")
        style_orange.configure("orange.TButton",
                            foreground="black",
                            background="orange")
        style_purple = ttk.Style()
        style_purple.theme_use("default")
        style_purple.configure("purple.TButton",
                            foreground="white",
                            background="purple")
        style_blue = ttk.Style()
        style_blue.theme_use("default")
        style_blue.configure("blue.TButton",
                            foreground="white",
                            background="blue")
        style_pink = ttk.Style()
        style_pink.theme_use("default")
        style_pink.configure("pink.TButton",
                            foreground="black",
                            background="DeepPink2")
        style_black = ttk.Style()
        style_black.theme_use("default")
        style_black.configure("black.TButton",
                            foreground="grey",
                            background="darkblue")
        rowloc = -1
        global subtaskbuttonsgrid
        subtaskbuttonsgrid = {}
        global taskbuttonspack
        taskbuttonspack = {}
        global subtaskentrygrid
        subtaskentrygrid = {}
        
        task_list = list(input_dict.keys())
        
        global somethingnew
        somethingnew = {}
        
        global gridbuttonsiter
        gridbuttonsiter = {}        
        
        for x in sorted(task_list):
            taskbuttonspack['{0}'.format(x)]={'fill': BOTH,
                                              'padx': 5,
                                              'pady': 1}
            
            subtask_dict = sorted(input_dict[x])
            gridbuttonsiter['{0}'.format(x)] = subtask_dict
            rowloc += 1
            columnloc = 0
            for z in subtask_dict:

                subtaskbuttonsgrid['{0}'.format(z)]={'sticky': W+E+N+S,
                                                     'row': rowloc,
                                                     'column': columnloc,
                                                     'padx': 5,
                                                     'pady': 1,}
                subtaskentrygrid['{0}'.format(z)]={'sticky': W+E+N+S,
                                                     'row': rowloc,
                                                     'column': columnloc,
                                                     'padx': 5,
                                                     'pady': 4}
                somethingnew['{0}'.format(x)] = ('{0}'.format(z))
                columnloc += 1
        
class Build_Dicts:
    def __init__(self, master):
        pass
##        self.default_value_elements = ['parent name','children names','genesis date',
##                                          'hard deadline','soft deadline',
##                                          'completion date','weblink',
##                                          'filelink','parent defcon',
##                                          'self defcon','children defcon',
##                                 'self name','self id']
##        self.write_value_elements = ['word length','text snippet','estimated duration']
##        self.buy_value_elements = ['price','shipping','frequency']


    def main_dict(input_key = ''):
        test_verb_dict[input_key] = {}

    def sub_dict(input_key = '', input_value = ''):

        default_value_elements = ('parent name','children names','genesis date',
                                          'hard deadline','soft deadline',
                                          'completion date','weblink',
                                          'filelink','parent defcon',
                                          'self defcon','children defcon',
                                 'self name','self id', 'complete', 'progress')
        write_value_elements = ('word length','text snippet','estimated duration')
        buy_value_elements = ('price','shipping','frequency')
        
        if input_key == 'write':
            sub_dict_builder_list = default_value_elements + write_value_elements
            sub_dict_builder_dict = dict.fromkeys(sub_dict_builder_list)
        elif input_key == 'buy' or input_key == 'rent':
            sub_dict_builder_list = default_value_elements + buy_value_elements
            sub_dict_builder_dict = dict.fromkeys(sub_dict_builder_list)
        else:
            sub_dict_builder_dict = dict.fromkeys(default_value_elements)
        i = 0
        for key in sorted(sub_dict_builder_dict.keys()):
##            sub_dict_builder_dict[key] = {('<no value>'): {}}
            i = i + 1
            sub_dict_builder_dict[key] = {('empty_%d' % i): {}}
            
        test_verb_dict[input_key][input_value] = sub_dict_builder_dict
        test_verb_dict[input_key][input_value]['genesis date'] = {str(datetime.datetime.now()): {}}
        test_verb_dict[input_key][input_value]['parent'] = {input_key:{}}
        test_verb_dict[input_key][input_value]['self id'] = {str(uuid.uuid4()): {}}
        test_verb_dict[input_key][input_value]['self name'] = {input_value: {}}
        test_verb_dict[input_key][input_value]['complete'] = {'False':{}}
        
class Input_Frame:
    def __init__(self, master, frame):
        self.frame1 = Frame(master)
        self.frame1.pack(side = TOP)
        self.entryframe0 = Frame(self.frame1)
        self.entryframe0.pack(fill = X, expand = True)
        self.entryframe1 = Frame(self.frame1) 
        self.entryframe1.pack(fill = X, expand = True)
        self.entryframe2 = Frame(self.frame1)
        self.entryframe2.pack(fill = X, expand = True)
        self.entryframe3 = Frame(self.frame1)
        self.entryframe3.pack(fill = X, expand = True)
        
        self.label0 = Label(self.entryframe0,
                            text ='Verb:')
        self.label0.pack(fill = X, expand = True, side = LEFT)
        global verbentry0
        verbentry0 = Entry(self.entryframe0,
                        width = 15)
        verbentry0.pack(fill = X, expand = True) 
        verbentry0.focus_set
        
        self.label1 = Label(self.entryframe1,
                            text ='Noun:')
        self.label1.pack(fill = X, expand = True, side = LEFT) 
        self.e1 = Entry(self.entryframe1,
                        width = 15)
        self.e1.pack(fill = X, expand = True)
        
        self.label2 = Label(self.entryframe2,
                            text ='SubNoun:')
        self.label2.pack(fill = X, expand = True, side = LEFT) 
        self.e2 = Entry(self.entryframe2,
                         width = 15)
        self.e2.pack(fill = X, expand = True)
        
        self.label3 = Label(self.entryframe3,
                            text ='Noun:')
        self.label3.pack(fill = X, expand = True, side = LEFT) 
        self.e3 = Entry(self.entryframe3,
                         width = 15)
        self.e3.pack(fill = X, expand = True)

        image = Image.open("anja.png")
        icon = ImageTk.PhotoImage(image)

        self.add_task_button = ttk.Button(self.frame1,
                                          text = "submit",
                                          width = 10,
                                          command=self.addTask_callback,
                                          style = 'main.TButton')
        self.add_task_button.pack()
        self.remove_task_button = ttk.Button(self.frame1,
                                          text="remove",
                                          width=10,
                                          command=self.removeTask_callback,
                                          style = 'main.TButton')
        self.remove_task_button.pack()
        self.clear_task_button = ttk.Button(self.frame1,
                                       text="hide",
                                       command=self.clearTask_callback,
                                       style = 'main.TButton')
        self.clear_task_button.pack()
        self.go_home_button = ttk.Button(self.frame1,
                                          text="home",
                                          width=10,
                                          command=self.go_home_callback,
                                          style = 'main.TButton')
        self.go_home_button.pack()
##        self.drill_task_button = ttk.Button(self.frame1,
##                                          text="drill",
##                                          width=10,
##                                          command= self.sub_button_function,
##                                          style = 'main.TButton')
##        self.drill_task_button.pack()
        
        self.entryframe4 = Frame(self.frame1)
        self.entryframe4.pack(fill = X, expand = True)

        self.label4 = Label(self.entryframe4,
                            text ='Output Filename:')
        self.label4.pack(fill = X, expand = True, side = TOP)
        
        self.e4 = Entry(self.entryframe4,
                         width = 15)
        self.e4.insert(0, "mylist_" + time.strftime("%m_%d_%Y"))
        self.e4.pack(fill = X, expand = True, side = LEFT)
        
        filetype_list = ['','.txt','.csv']
        self.save_file_ext =  StringVar()
        self.save_file_ext.set('.txt')
                
        self.opt0 = ttk.OptionMenu(self.entryframe4, self.save_file_ext, *filetype_list)
        self.opt0.pack(fill = X, expand = True)

        self.save_task_button = ttk.Button(self.frame1,
                                          text="save",
                                          width=10,
                                          command= self.save_session,
                                          style = 'main.TButton')
        self.save_task_button.pack()
        
        self.entryframe5 = Frame(self.frame1)
        self.entryframe5.pack(fill = X, expand = True)

        self.label5 = Label(self.entryframe5,
                            text ='Input Filename:')
        self.label5.pack(fill = X, expand = True, side = TOP)
        
        self.e5 = Entry(self.entryframe5,
                         width = 15)
        self.e5.insert(0, "mylist_" + time.strftime("%m_%d_%Y"))
        self.e5.pack(fill = X, expand = True, side = LEFT)

        filetype_list = ['','.txt','.csv']
        self.load_file_ext =  StringVar()
        self.load_file_ext.set('.txt')

        self.opt1 = ttk.OptionMenu(self.entryframe5, self.load_file_ext, *filetype_list)
        self.opt1.pack(fill = X, expand = True)

        self.load_task_button = ttk.Button(self.frame1,
                                          text="load",
                                          width=10,
                                          command= self.load_session,
                                          style = 'main.TButton')
        self.load_task_button.pack()

        
    def open_link(link_name):
        if link_name == ('art of the deal'):
            webbrowser.open('http://www.funnyordie.com/videos/ad38087bac/donald-trump-art-of-the-deal-movie')
        elif link_name == ('malcolm in the middle'):
            webbrowser.open('http://www.netflix.com/browse/my-list')
        
    def sub_button_function(button_dict):

        for g,h in button_dict.items():
            submittedVerb = g
            submittedVP0 = h      
        newdict = test_verb_dict[submittedVerb][submittedVP0]
        Load_Dict.Load_Button_Values(newdict)
        Input_Frame.clearTask_callback()
        Build_Buttons.pack_grid_subbuttons()
    
    def sub_button_save_function(some_dict):
##        print(some_dict)
        pass
        for g,h in some_dict.items():
            x = g ## parent
            for j,k in h.items():
                y = j ## self
                for r,s in k.items():
                    z = r ## property name
                    textfield = s ## property value (entry_object)
##        print(textfield.cget('state'))
##        function 1
        if  textfield.cget('state') == 'normal': ##        if the text field is enabled, then on button press
            input_property = textfield.get("1.0",END) ##        get the input text from the text field
##            print(input_property)
            global test_verb_dict
            test_verb_dict[x][y][z] = {input_property.strip(): {}} ##        and assign that text to the working dict
            textfield.configure(state='disabled',
                                background='black',
                                foreground='white',
                                relief = FLAT) ##        disable the text box                
            textfield.tag_configure('justify', justify='center')
            textfield.tag_add('justify', 1.0, "end")
##        function 2
        elif textfield.cget('state') == 'disabled': ##        if the text field is diabled, then on button press
            textfield.configure(state='normal',
                                background='white',
                                foreground='black',
                                relief = SUNKEN) ##        enable the text field
            textfield.tag_configure('justify', justify='left')

            
    def save_session(self=0):
        save_name = self.e4.get()
        ext_name = self.save_file_ext.get()
        filename = save_name + ext_name
        if save_name != (''):
            target = open(filename, 'w')
            target.write(str(test_verb_dict)) 
            target.close()
            messagebox.showinfo(title = 'MeshWare', message = ('Session has been saved as %s ' % filename))
        else:
            messagebox.showinfo(title = 'MeshWare', message = ('a filename is required!'))

    def load_session(self):
        load_name = self.e5.get()
        ext_name = self.load_file_ext.get()
        filename = load_name + ext_name
        if load_name != (''):
            with open(filename,'r') as loadedverbsraw:
                global test_verb_dict
                test_verb_dict  = ast.literal_eval(loadedverbsraw.read())           
                Load_Dict.Load_Button_Values(test_verb_dict)
        else:
            messagebox.showinfo(title = 'MeshWare', message = ('a filename is required!'))

        self.clearTask_callback()
        Build_Buttons.pack_grid_buttons()
        Build_Buttons.pack_prog_buttons()
        Build_Buttons.pack_prog_step_buttons()
        Build_Buttons.pack_progress_bars()

    def transfer_text_callback(buttontext = ''):
        print(buttontext)
        global verbentry0
        verbentry0.delete(0, END)
        verbentry0.insert(0, buttontext)
        
    def go_home_callback(self):
        Load_Dict.Load_Button_Values(test_verb_dict)
        self.clearTask_callback()
        Build_Buttons.pack_grid_buttons()
        Build_Buttons.pack_prog_buttons()
        Build_Buttons.pack_prog_step_buttons()
        Build_Buttons.pack_progress_bars()
        
    def addTask_callback(self):
        global verbentry0
        submittedVerb = verbentry0.get()
        submittedVP0 = self.e1.get()
        submittedVPA = self.e2.get()
        submittedVP1 = self.e3.get()

        if submittedVerb == (''):
            messagebox.showinfo(title = 'MeshWare', message = ('a main task is required'))
            return
        
        if submittedVerb != (''):
            novelverb = submittedVerb in test_verb_dict
            if novelverb == False:
                print('verb sent to dict')
                Build_Dicts.main_dict(submittedVerb)
            elif novelverb == True:
                print('verb alread in dict')

        if test_verb_dict[submittedVerb] != (''):
            tasklist = test_verb_dict[submittedVerb]        
        else:
            tasklist = ()
            
        if submittedVerb != (''):
            if submittedVP0 != (''):
                novelverb0 = submittedVP0 in tasklist #Returns True if present, False if novel
                if novelverb0 == False:
                    print('first task sent to verb dict')
                    Build_Dicts.sub_dict(submittedVerb, submittedVP0)
                elif novelverb0 == True:
                    print('first task already in dict')
##                    messagebox.showinfo(title = 'MeshWare', message = ("%s %s is already in the dictionary" % (submittedVerb, submittedVP0)
            elif submittedVP1 == (''):
                print('no first task submitted')                                    
##                messagebox.showinfo(title = 'MeshWare', message = ('no first task submitted')
            if submittedVP1 != (''):
                novelverb1 = submittedVP1 in tasklist #Returns True if present, False if novel
                if novelverb1 == False:
                    print('second task sent to dict')
                    Build_Dicts.sub_dict(submittedVerb, submittedVP1)
                elif novelverb1 == True:
                    print('second task already in dict')
##                    messagebox.showinfo(title = 'MeshWare', message = ("%s %s is already in the dictionary" % (submittedVerb, submittedVP1)
            elif submittedVP1 == (''):
                print('no second task submitted')
                                                

        Load_Dict.Load_Button_Values(test_verb_dict)
        self.clearTask_callback()
        Build_Buttons.pack_grid_buttons()
        Build_Buttons.pack_prog_buttons()
        Build_Buttons.pack_prog_step_buttons()
        Build_Buttons.pack_progress_bars()

    def removeTask_callback(self):
        global verbentry0
        submittedVerb = verbentry0.get()
        submittedVP0 = self.e1.get()
##        submittedVPA = self.e2.get()
##        submittedVP1 = self.e3.get()
        
        if submittedVerb != (''):
            novelverb = submittedVerb in test_verb_dict #Returns True if present, False if novel
            if novelverb == True:
                iter_dict = {}
                iter_dict = test_verb_dict[submittedVerb]
                if submittedVP0 != (''):
                    noveltask = submittedVP0 in iter_dict #Returns True if present, False if novel
                    if noveltask == True:
                        trashdict = {}
                        trashdict = iter_dict.pop(submittedVP0)
                        test_verb_dict[submittedVerb].update(iter_dict)
                        messagebox.showinfo(title = 'MeshWare', message = ("%s %s has been removed from the dictionary" % (submittedVerb, submittedVP0)))
                    else:
                        messagebox.showinfo(title = 'MeshWare', message = ('%s %s is not in the dictionary' % (submittedVerb, submittedVP0)))
                else:
                    deletekeyconfirm = messagebox.askokcancel('Delete Dictionary Key',
                                                              ('Are you sure you want to delete the following verb from the dictionary?\n\n **%s**' % submittedVerb))
                    if deletekeyconfirm == True:
                        test_verb_dict.pop(submittedVerb)
            else:
                messagebox.showerror(title = 'MeshWare', message = ('%s is not in the dictionary' % submittedVerb))
                return
        else:
            messagebox.showerror(title = 'MeshWare', message = ('a main task and subtask are required'))
            return
        
        Load_Dict.Load_Button_Values(test_verb_dict)
        self.clearTask_callback()
        Build_Buttons.pack_grid_buttons()
        Build_Buttons.pack_prog_buttons()
        Build_Buttons.pack_prog_step_buttons()
        Build_Buttons.pack_progress_bars()
        
    def clearTask_callback(self=0):
        global buttonframe
        global progressframe
        
        buttonframe.pack_forget()
        buttonframe.destroy()
        progressframe.pack_forget()
        progressframe.destroy()
        

        progressframe = Frame(progress_tab_frame,
                        relief = SUNKEN,
                          bg = 'grey')
        progressframe.pack(fill = BOTH, expand = True)
        
        buttonframe = Frame(tasks_tab_frame,
                            relief = SUNKEN)
        buttonframe.pack(fill = BOTH, expand = True)
        #ScrollCanvas(buttonframe).pack(side="top", fill="both", expand=True)
        
        global canvas
        canvas = Canvas(buttonframe, borderwidth=0, background='black')
        frame_on_canvas = ttk.Frame(canvas)
        
        ##Pack paned window in tasks tab
        global tasks_tab_panedwindow
        tasks_tab_panedwindow = ttk.Panedwindow(frame_on_canvas, orient = HORIZONTAL)
        tasks_tab_panedwindow.pack(fill = 'x', expand = True)
        vsb = Scrollbar(buttonframe, orient="vertical", command=canvas.yview)
        hsb = Scrollbar(buttonframe, orient="horizontal", command=canvas.xview)
        canvas.configure(yscrollcommand=vsb.set)
        canvas.configure(xscrollcommand=hsb.set)
        
        ##Add panes to Task tab paned window
        global ttpw_taskpane
        ttpw_taskpane = ttk.Frame(tasks_tab_panedwindow, relief = SUNKEN)
        global ttpw_subtaskpane
        ttpw_subtaskpane = ttk.Frame(tasks_tab_panedwindow, relief = SUNKEN)

        vsb.pack(side="right", fill="y")
        hsb.pack(side="bottom", fill="x")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((0,0), window=frame_on_canvas, anchor="nw", 
                                  tags="frame_on_canvas")
        

        tasks_tab_panedwindow.add(ttpw_taskpane, weight = 1)
        tasks_tab_panedwindow.add(ttpw_subtaskpane, weight = 4)
        
        frame_on_canvas.bind("<Configure>", Scroll_Events.onFrameConfigure)
        frame_on_canvas.bind('<Enter>', Scroll_Events._bound_to_mousewheel)
        frame_on_canvas.bind('<Leave>', Scroll_Events._unbound_to_mousewheel)

        Build_Buttons.pack_grid_buttons()

        ##Progress paned windows
        ProgressbarPanes = ttk.Panedwindow(progressframe, orient = HORIZONTAL)
        ProgressbarPanes.pack(fill = BOTH, expand = True)

        ##Add panes to Progress tab paned window
        global progresstab_taskpane
        global barsframe
        global statsframe1
        global statsframe2
        
        progresstab_taskpane = Frame(ProgressbarPanes, width = 100, height = 200)
        barsframe = Frame(ProgressbarPanes, width = 200, height = 200)
        statsframe1 = Frame(ProgressbarPanes, width = 50, height = 200)
        statsframe2 = Frame(ProgressbarPanes, width = 50, height = 200)

        ProgressbarPanes.add(progresstab_taskpane, weight = 2)
        ProgressbarPanes.add(barsframe, weight = 6)
        ProgressbarPanes.add(statsframe1, weight = 1)
        ProgressbarPanes.add(statsframe2, weight = 1)   
        
    def progress_step_button_function(self, step): #self = task name as string
        
        for key,value in pbars.items():
            if key == self:
                value.step(step)
        
    def genTask_callback():
        pass
    
class ScrollCanvas(Frame):
    def __init__(self, root):

        Frame.__init__(self, root)
        self.canvas = Canvas(root, borderwidth=0, background='black', bd=-50)
        self.frame = Frame(self.canvas, background='white', padx=5, pady=5)
##        self.frame2 = Frame(self.canvas, background="#ffffff")        
        self.vsb = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.hsb = Scrollbar(root, orient="horizontal", command=self.canvas.xview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.canvas.configure(xscrollcommand=self.hsb.set)
        
        self.vsb.pack(side="right", fill="y")
        self.hsb.pack(side="bottom", fill="x")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((0,0), window=self.frame, anchor="nw", 
                                  tags="self.frame")
##        self.canvas.create_window((0,0), window=self.frame2, anchor="ne", 
##                                  tags="self.frame2")
        
        self.frame.bind("<Configure>", self.onFrameConfigure)
        self.frame.bind('<Enter>', self._bound_to_mousewheel)
        #self.frame.bind('<Leave>', self._unbound_to_mousewheel)

##        self.frame2.bind("<Configure>", self.onFrameConfigure)
##        self.frame2.bind('<Enter>', self._bound_to_mousewheel)
##        #self.frame2.bind('<Leave>', self._unbound_to_mousewheel)
        
        #self.populate()
        #Build_Buttons.pack_grid_buttons()
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
           button = ttk.Button(self.frame,
                    text = ("This is button number " + str(line)),
                    style = 'grey.TButton')
           button.pack(expand = True)
##        for line in range(100):
##           button = ttk.Button(self.frame2,
##                    text = ("This is button number " + str(line)),
##                    style = 'grey.TButton')
##           button.pack(expand = True)           

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
class Build_Buttons:

    def __init__(self, master):
        pass
            
    def pack_buttons(self=0):

        ##Tasks pane
        task_label_frame = ttk.Frame(ttpw_taskpane)
        task_label_frame.pack(fill = X)
        task_label = Label(task_label_frame, text = 'Tasks', justify = 'center')
        task_label.pack(fill = X)

        #ScrollCanvas(ttpw_taskpane).pack(side="top", fill="both", expand=True)
        
        frame = Frame(ttpw_taskpane,
                      relief = SUNKEN,
                      bg = 'grey')
        frame.pack(fill = BOTH, expand = True)
        for f in sorted(taskbuttonspack):
            if f == 'buy':
                button = ttk.Button(frame,
                                    text = f.upper(),
                                    style = 'gold.TButton')  
            elif f == 'write':
                button = ttk.Button(frame,
                                    text = f.upper(),
                                    style = 'red.TButton') 
            else:
                button = ttk.Button(frame,
                                    text = f.title(),
                                    style = 'grey.TButton')
            button.config(command = lambda i=f: Input_Frame.transfer_text_callback(i))
            setattr(frame, f, button)   
            button.pack(**taskbuttonspack[f])
            
    def pack_prog_buttons(self=0):

        ##Task Progress pane label
        task_label_frame = ttk.Frame(progresstab_taskpane)
        task_label_frame.pack(fill = X)
        task_label = Label(task_label_frame, text = 'Tasks', justify = 'center')
        task_label.pack(fill = X)
    
        frame = Frame(progresstab_taskpane,
                      relief = SUNKEN,
                      bg = 'grey')
        frame.pack(fill = BOTH, expand = True)
        for f in sorted(taskbuttonspack):
            if f == 'buy':
                button = ttk.Button(frame,
                                    text = f.upper(),
                                    style = 'gold.TButton')  
            elif f == 'write':
                button = ttk.Button(frame,
                                    text = f.upper(),
                                    style = 'red.TButton') 
            else:
                button = ttk.Button(frame,
                                    text = f.title(),
                                    style = 'grey.TButton')
            button.config(command = lambda i=f: Input_Frame.transfer_text_callback(i))
            setattr(frame, f, button)   
            button.pack(**taskbuttonspack[f])

    def pack_prog_step_buttons(self=0):

        taskProgress_add_label_frame = ttk.Frame(statsframe1)
        taskProgress_add_label_frame.pack(fill = X)
        taskProgress_add_label = Label(taskProgress_add_label_frame, text = 'Add', justify = 'center')
        taskProgress_add_label.pack(fill = X)

        taskProgress_minus_label_frame = ttk.Frame(statsframe2)
        taskProgress_minus_label_frame.pack(fill = X)
        taskProgress_minus_label = Label(taskProgress_minus_label_frame, text = 'Subtract', justify = 'center')
        taskProgress_minus_label.pack(fill = X)

        frame = Frame(statsframe2,
                      relief = SUNKEN,
                      bg = 'black')
        frame.pack(fill = BOTH, expand = True)
        for f in sorted(taskbuttonspack):
            button = ttk.Button(frame, text = '-', style = 'grey.TButton')
            button.config(command = lambda i=f: Input_Frame.progress_step_button_function(i,-5))
            setattr(frame, f, button)   
            button.pack(**taskbuttonspack[f])        

        frame = Frame(statsframe1,
                      relief = SUNKEN,
                      bg = 'black')
        frame.pack(fill = BOTH, expand = True)
        for f in sorted(taskbuttonspack):
            button = ttk.Button(frame, text = '+', style = 'grey.TButton')
            button.config(command = lambda i=f: Input_Frame.progress_step_button_function(i,5))
            setattr(frame, f, button)   
            button.pack(**taskbuttonspack[f])



    def pack_progress_bars(self=0):

        taskProgress_label_frame = ttk.Frame(barsframe)
        taskProgress_label_frame.pack(fill = X)
        taskProgress_label = Label(taskProgress_label_frame, text = 'Progress', justify = 'center')
        taskProgress_label.pack(fill = X)

        frame = Frame(barsframe,
                      relief = SUNKEN,
                      bg = 'black')
        frame.pack(fill = BOTH, expand = True)
        global pbars
        pbars = {}
        for f in sorted(taskbuttonspack):
            progressbar = ttk.Progressbar(frame, orient = HORIZONTAL, length = 200, style='TProgressbar')
            progressbar.config(mode = 'determinate', maximum = 100.0, value = 25)
            progressbar.pack(**taskbuttonspack[f])
            pbars[f] = progressbar
            
    def grid_buttons(self=0):

        ##Subtasks pane
        ttpw_subtask_label_frame = ttk.Frame(ttpw_subtaskpane)
        ttpw_subtask_label_frame.pack(fill = BOTH)
        ttpw_subtask_label = Label(ttpw_subtask_label_frame, text = '      Subtasks      ', justify = 'center')
        ttpw_subtask_label.pack(fill = X)

        #ScrollCanvas(ttpw_subtaskpane).pack(side="top", fill="both", expand=True)

        frame = Frame(ttpw_subtaskpane,
                      relief = SUNKEN, bg='black')

        frame.pack(fill = BOTH, expand = True)
        
        for g, t in gridbuttonsiter.items():
            for f in t:
##                print(g)
##                print(f)
                defcon = test_verb_dict[g][f]['self defcon']
##                print(defcon)
                if defcon == {'1':{}}:
                    b_style = 'red.TButton'
                elif defcon == {'2':{}}:
                    b_style = 'pink.TButton' 
                elif defcon == {'3':{}}:
                    b_style = 'orange.TButton'
                elif defcon == {'4':{}}:
                    b_style = 'gold.TButton'
                elif defcon == {'5':{}}:
                    b_style = 'green.TButton'
                elif defcon == {'6':{}}:
                    b_style = 'blue.TButton'
                elif defcon == {'7':{}}:
                    b_style = 'purple.TButton'
                elif defcon == {'10':{}}:
                    b_style = 'black.TButton'
                else:
                    b_style = 'grey.TButton'

            
                q = {}
                q[g] = f
                button = ttk.Button(frame,
                                    text = f,
                                    style = b_style)
                button.config(command = lambda i=q: Input_Frame.sub_button_function(i))
                button.bind("<Button-3>", Input_Frame.transfer_text_callback)
                setattr(frame, f, button)   
                button.grid(**subtaskbuttonsgrid[f])
                
            
    def pack_grid_buttons():
        Build_Buttons.pack_buttons()
        Build_Buttons.grid_buttons()
        
        
    def pack_subbuttons(self=0):
        
        ##Tasks pane
        task_label_frame = ttk.Frame(ttpw_taskpane)
        task_label_frame.pack(fill = X)
        
        task_label = Label(task_label_frame, text = 'Property', justify = 'center')
        task_label.pack(fill = X)
        
        frame = Frame(ttpw_taskpane,
                      relief = SUNKEN,
                      bg = 'grey')
        frame.pack(fill = BOTH, expand = True)        
        
        for f in sorted(taskbuttonspack):
##            if f == 'invest':
##                button = ttk.Button(frame,
##                                    text = f.upper(),
##                                    style = 'gold.TButton')  
##            elif f == 'write':
##                button = ttk.Button(frame,
##                                    text = f.upper(),
##                                    style = 'red.TButton') 
##            else:
            property_name = f
            parent_name = somethingnew['parent'].lower()
            self_name = somethingnew['self name'].lower()
            field = property_dict[parent_name][self_name][property_name]
            pp_dict = {parent_name: {self_name: {property_name: field}}}           

            
            button = ttk.Button(frame,
                                text = f.title(),
                                style = 'grey.TButton')
            button.config(command = lambda i=pp_dict: Input_Frame.sub_button_save_function(i))
            if f == 'genesis date' or f == 'self id' or f == 'parent' or f == 'self name':
                button.config(state=DISABLED)    
            setattr(frame, f, button)   
            button.pack(**taskbuttonspack[f])
        
        
    def grid_subbuttons(self = 0):
        ##Properties pane
        ttpw_subtask_label_frame = ttk.Frame(ttpw_subtaskpane)
        ttpw_subtask_label_frame.pack(fill = BOTH)
        ttpw_subtask_label = Label(ttpw_subtask_label_frame, text = '      Values      ', justify = 'center')
        ttpw_subtask_label.pack(fill = X)
        
        frame = Frame(ttpw_subtaskpane,
                      relief = SUNKEN,
                      bg = 'black')
        frame.pack(fill = BOTH, expand = True)
        
        parent_name = somethingnew['parent'].lower()
        self_name = somethingnew['self name'].lower()
        property_name = somethingnew.keys()

        global property_dict
        property_dict = {parent_name:{self_name:{}}}
        
        for h in somethingnew.keys():
            property_dict[parent_name][self_name] = {h:{}}
            
        for g, f in somethingnew.items():

            if f[:6] != 'empty_':
                field = Text(frame,
                             height = 1,
                             width = 30,
                             background='black',
                             foreground='white',
                             relief = FLAT)
                field.insert(END, f)
                field.tag_configure('center', justify='center')
                field.tag_add('center', 1.0, "end")
                field.config(state=DISABLED)
                setattr(frame, f, field)   
                field.grid(**subtaskentrygrid[f])
            else:
                field = Text(frame,
                             height = 1,
                             width = 30)
                field.insert(END, f)
                setattr(frame, f, field)   
                field.grid(**subtaskentrygrid[f])
                
            field_state = field.cget('state')
            property_dict[parent_name][self_name][g] = field
##        print(property_dict)
        
    def pack_grid_subbuttons():
        Build_Buttons.grid_subbuttons()
        Build_Buttons.pack_subbuttons()
        
##class Schedule_Tasks:
##
##    def __init__(self, master):
##        pass
##            
##    def calculate_time(self=0):
##        due_date = test_verb_dict[parent][self]['hard deadline']
##        current_date = {str(datetime.datetime.now()): {}}
##        time_left = due_date - current_date

class Calendar(ttk.Frame):
    # XXX ToDo: cget and configure

    datetime = calendar.datetime.datetime
    timedelta = calendar.datetime.timedelta

    def __init__(self, master=None, **kw):
        """
        WIDGET-SPECIFIC OPTIONS

            locale, firstweekday, year, month, selectbackground,
            selectforeground
        """
        # remove custom options from kw before initializating ttk.Frame
        fwday = kw.pop('firstweekday', calendar.MONDAY)
        year = kw.pop('year', self.datetime.now().year)
        month = kw.pop('month', self.datetime.now().month)
        locale = kw.pop('locale', None)
        sel_bg = kw.pop('selectbackground', '#ecffc4')
        sel_fg = kw.pop('selectforeground', '#05640e')

        self._date = self.datetime(year, month, 1)
        self._selection = None # no date selected

        ttk.Frame.__init__(self, master, **kw)

        self._cal = get_calendar(locale, fwday)

        self.__setup_styles()       # creates custom styles
        self.__place_widgets()      # pack/grid used widgets
        self.__config_calendar()    # adjust calendar columns and setup tags
        # configure a canvas, and proper bindings, for selecting dates
        self.__setup_selection(sel_bg, sel_fg)

        # store items ids, used for insertion later
        self._items = [self._calendar.insert('', 'end', values='')
                            for _ in range(6)]
        # insert dates in the currently empty calendar
        self._build_calendar()

        # set the minimal size for the widget
        self._calendar.bind('<Map>', self.__minsize)

    def __setitem__(self, item, value):
        if item in ('year', 'month'):
            raise AttributeError("attribute '%s' is not writeable" % item)
        elif item == 'selectbackground':
            self._canvas['background'] = value
        elif item == 'selectforeground':
            self._canvas.itemconfigure(self._canvas.text, item=value)
        else:
            ttk.Frame.__setitem__(self, item, value)

    def __getitem__(self, item):
        if item in ('year', 'month'):
            return getattr(self._date, item)
        elif item == 'selectbackground':
            return self._canvas['background']
        elif item == 'selectforeground':
            return self._canvas.itemcget(self._canvas.text, 'fill')
        else:
            r = ttk.tclobjs_to_py({item: ttk.Frame.__getitem__(self, item)})
            return r[item]

    def __setup_styles(self):
        # custom ttk styles
        style = ttk.Style(self.master)
        arrow_layout = lambda dir: (
            [('Button.focus', {'children': [('Button.%sarrow' % dir, None)]})]
        )
        style.layout('L.TButton', arrow_layout('left'))
        style.layout('R.TButton', arrow_layout('right'))

    def __place_widgets(self):
        # header frame and its widgets
        hframe = ttk.Frame(self)
        lbtn = ttk.Button(hframe, style='L.TButton', command=self._prev_month)
        rbtn = ttk.Button(hframe, style='R.TButton', command=self._next_month)
        self._header = ttk.Label(hframe, width=15, anchor='center')
        # the calendar
        self._calendar = ttk.Treeview(show='', selectmode='none', height=7)

        # pack the widgets
        hframe.pack(in_=self, side='top', pady=4, anchor='center')
        lbtn.grid(in_=hframe)
        self._header.grid(in_=hframe, column=1, row=0, padx=12)
        rbtn.grid(in_=hframe, column=2, row=0)
        self._calendar.pack(in_=self, expand=1, fill='both', side='bottom')

    def __config_calendar(self):
        cols = self._cal.formatweekheader(3).split()
        self._calendar['columns'] = cols
        self._calendar.tag_configure('header', background='grey90')
        self._calendar.insert('', 'end', values=cols, tag='header')
        # adjust its columns width
        font = tkinter.font.Font()
        maxwidth = max(font.measure(col) for col in cols)
        for col in cols:
            self._calendar.column(col, width=maxwidth, minwidth=maxwidth,
                anchor='e')

    def __setup_selection(self, sel_bg, sel_fg):
        self._font = tkinter.font.Font()
        self._canvas = canvas = tkinter.Canvas(self._calendar,
            background=sel_bg, borderwidth=0, highlightthickness=0)
        canvas.text = canvas.create_text(0, 0, fill=sel_fg, anchor='w')

        canvas.bind('<ButtonPress-1>', lambda evt: canvas.place_forget())
        self._calendar.bind('<Configure>', lambda evt: canvas.place_forget())
        self._calendar.bind('<ButtonPress-1>', self._pressed)

    def __minsize(self, evt):
        width, height = self._calendar.master.geometry().split('x')
        height = height[:height.index('+')]
        self._calendar.master.minsize(width, height)

    def _build_calendar(self):
        year, month = self._date.year, self._date.month

        # update header text (Month, YEAR)
        header = self._cal.formatmonthname(year, month, 0)
        self._header['text'] = header.title()

        # update calendar shown dates
        cal = self._cal.monthdayscalendar(year, month)
        for indx, item in enumerate(self._items):
            week = cal[indx] if indx < len(cal) else []
            fmt_week = [('%02d' % day) if day else '' for day in week]
            self._calendar.item(item, values=fmt_week)

    def _show_selection(self, text, bbox):
        """Configure canvas for a new selection."""
        x, y, width, height = bbox

        textw = self._font.measure(text)

        canvas = self._canvas
        canvas.configure(width=width, height=height)
        canvas.coords(canvas.text, width - textw, height / 2 - 1)
        canvas.itemconfigure(canvas.text, text=text)
        canvas.place(in_=self._calendar, x=x, y=y)

    # Callbacks

    def _pressed(self, evt):
        """Clicked somewhere in the calendar."""
        x, y, widget = evt.x, evt.y, evt.widget
        item = widget.identify_row(y)
        column = widget.identify_column(x)

        if not column or not item in self._items:
            # clicked in the weekdays row or just outside the columns
            return

        item_values = widget.item(item)['values']
        if not len(item_values): # row is empty for this month
            return

        text = item_values[int(column[1]) - 1]
        if not text: # date is empty
            return

        bbox = widget.bbox(item, column)
        if not bbox: # calendar not visible yet
            return

        # update and then show selection
        text = '%02d' % text
        self._selection = (text, item, column)
        self._show_selection(text, bbox)

    def _prev_month(self):
        """Updated calendar to show the previous month."""
        self._canvas.place_forget()

        self._date = self._date - self.timedelta(days=1)
        self._date = self.datetime(self._date.year, self._date.month, 1)
        self._build_calendar() # reconstuct calendar

    def _next_month(self):
        """Update calendar to show the next month."""
        self._canvas.place_forget()

        year, month = self._date.year, self._date.month
        self._date = self._date + self.timedelta(
            days=calendar.monthrange(year, month)[1] + 1)
        self._date = self.datetime(self._date.year, self._date.month, 1)
        self._build_calendar() # reconstruct calendar

    # Properties

    @property
    def selection(self):
        """Return a datetime representing the current selected date."""
        if not self._selection:
            return None
        
        year, month = self._date.year, self._date.month
        return self.datetime(year, month, int(self._selection[0]))


class Games(ttk.Frame):

    def SCMD():

        import pygame, sys, random, time
        screenwidth = 600                   #set screen width
        screenheight = 600                  #set screen height
        ceiling = 200                       #Set size of 'house'
        maxshots = 3                       #set number of shots player can have on screen
        black = 0, 0, 0                     #defines black color for background
        playerspeed = 5                     #sets per frame speed of player ship
        shotspeed = 15                     #speed of player shots
        isalive = True                      #leave this alone
        playerlives = 3                     #number of lives for player
        collisions = True                   #set to False, player is invincible
        showlevel = True                    #leave alone

        pygame.mixer.pre_init(22050 , -16, 2, 2048)                      #Initialize pygame mixer
        pygame.mixer.init()
        pygame.font.init()                                              #Initialize pygame font object
        screen = pygame.display.set_mode((screenwidth, screenheight))
        clock = pygame.time.Clock()
        myfont = pygame.font.SysFont(None ,24)


        gamelevels = [(2,4,5, False, 0), (3,5,6, False, 0), (3,5,6, True, 0),
                  (3,7,6, False, 1), (4,7,6, True, 1), (4,8,6, False, 2),
                  (4,8,5, True, 2), (12,3, 4, True, 1), (5,10,5, True, 2)]



        spaceship = pygame.image.load("ship.png").convert()                  #this section loads images and sounds
        cootieball = pygame.image.load("ball1.png").convert()
        cootieball2 = pygame.image.load("ball2.png").convert()
        bomber1 = pygame.image.load("bomber1.png")
        bomber2 = pygame.image.load("bomber2.png")
        house1 = pygame.image.load("house1.png")
        house2 = pygame.image.load("house2.png")
        bomb = pygame.image.load("ball.png").convert()
        cootieshot = pygame.image.load("cootieshot.png").convert()
        title = pygame.image.load("title1.png")
        title2 = pygame.image.load("title2.png")
        gameovertitle = pygame.image.load("gameover.png")
        explosionimg = pygame.image.load("explode.png")
        shotsnd = pygame.mixer.Sound("shot.wav")
        shotsnd.set_volume(.6)
        deathsnd = pygame.mixer.Sound("DeathFlash.wav")
        splodesnd = pygame.mixer.Sound("splode.wav")
        titlemusic = pygame.mixer.Sound("darkfallout.ogg")
        titlemusic.play(-1)
        music = pygame.mixer.Sound("action.ogg")
        music.set_volume(1)
        #music.play(-1)

        score = myfont.render(" SCORE:", True, (255,255,255))            #these setup rect objects for score and lives display
        scorerect = score.get_rect()
        lives = myfont.render(" LIVES:", True, (255,255,255))
        livesrect = lives.get_rect()
        livesrect.top = 785
        leveltext = myfont.render("LEVEL 0", True, (255,255,255))
        levelrect = leveltext.get_rect()
        levelrect.center = (screenwidth / 2, screenheight / 2)
        instructions = myfont.render("SPACE TO FIRE - ARROWS OR W/A/S/D TO MOVE - SPACE TO START", True, (255,255,255))
        instructrect = instructions.get_rect()
        instructrect.center = (screenwidth / 2, screenheight - 40)



        class explosion:
            def __init__(self, pos):
                self.fc = 0
                self.exploderect = explosionimg.get_rect()
                self.exploderect.size = (32, 32)
                self.exploderect.center = pos


            def update(self):
                #exframe = ((self.fc // 4) * 32, ((self.fc+4)%4) * 32, (self.fc // 4) * 32 + 32, ((self.fc+4) % 4)* 32 + 32)
                #exframe = ((self.fc // 4) * 32, ((self.fc+4)%4) * 32, 32, 32)
                exframe = (((self.fc+4)%4) * 32, (self.fc // 4) * 32, 32, 32)
                screen.blit(explosionimg, self.exploderect, exframe)
                self.fc += 1
                if self.fc > 15:
                    self.killsplode()


            def killsplode(self):
                mysegs.remove(self)

            def iscollided(self, x):
                pass


        class shot:               #player shot object
            def __init__(self):
                self.pos = player1.pos
                self.speed = shotspeed
                self.img = cootieshot
                self.shotrect = cootieshot.get_rect()
                self.shotrect.center = self.pos

            def update(self):
                if self.pos[1] < 10:
                    myshots.remove(self)
                else:


                    self.pos = (self.pos[0], self.pos[1]-self.speed)
                    self.shotrect.center = self.pos
                    self.checkcollision()
                    screen.blit(self.img, self.shotrect)


            def checkcollision(self):

                for coot in mysegs:
                    if coot.iscollided(self.shotrect) != None:
                        myshots.remove(self)
                        break


        class segment:              #basic space cootie segment class
            def __init__(self, nextseg = None, pos = (-20,20)):
                self.pos = pos
                self.speed = 2
                self.right = True
                self.fall = True
                self.nextseg = nextseg
                self.pos2 = pos
                self.pos3 = pos
                self.frame = cootieball
                self.cootieballrect = cootieball.get_rect()
                self.cootieballrect.center = pos
                self.framecount = random.randint(0,5)
                self.bombcounter = 0


            def update(self):

                if self.framecount == 5:
                    if self.frame == cootieball:
                        self.frame = cootieball2
                        2
                    else:
                        self.frame = cootieball
                    self.framecount = 0
                self.framecount += 1
                self.pos3 = self.pos2
                self.pos2 = self.pos

                if self.nextseg != None:
                    self.pos = self.nextseg.pos3
                    self.right = self.nextseg.right
                    self.nextseg.update()
                else:

                    if self.right:
                        self.pos = (self.pos[0]+self.speed, self.pos[1])
                        if self.cootieballrect.center[0] > screenwidth - 20:
                            if self.fall == True:
                                self.pos = (self.pos[0], self.pos[1]+30)
                                if self.pos[1] > screenheight -40:
                                    self.fall = False
                            else:
                                self.pos =(self.pos[0], self.pos[1]-30)
                                if self.pos[1] < screenheight-200:
                                    self.fall = True
                            self.right = False
                    else:
                        self.pos = (self.pos[0]-self.speed, self.pos[1])
                        if self.cootieballrect.center[0] < 20:
                            if self.fall == True:
                                self.pos = (self.pos[0], self.pos[1]+30)
                                if self.pos[1] > screenheight-40:
                                    self.fall = False
                            else:
                                self.pos =(self.pos[0], self.pos[1]-30)
                                if self.pos[1] < screenheight-200:
                                    self.fall = True
                            self.right = True
                    self.bombcheck()
                self.cootieballrect.center = self.pos
                screen.blit(self.frame, self.cootieballrect)


            def iscollided(self, somerect):
                hits = None
                if self.nextseg != None:
                    hits = self.nextseg.iscollided(somerect)
                    if self.nextseg == hits:
                        self.pos =(self.pos[0], self.pos[1] + 30)
                        if self.right == True:
                            self.right = False
                        else:
                            self.right = True
                        self.nextseg = None


                if self.cootieballrect.colliderect(somerect):
                    splodesnd.play()
                    self.explode()

                    updatescore(20)
                    hits = self
                    if self.nextseg != None:
                        mysegs.append(self.nextseg)
                        self.nextseg = None
                    if self in mysegs:
                        self.killseg()

                return hits

            def killseg(self):
                #insert explosion code?

                mysegs.remove(self)




            def grow(self, length):
                for i in range(length):
                    self.spawn()

            def spawn(self):
                if self.nextseg == None:
                    self.nextseg = segment()
                    self.nextseg.pos = self.pos

                else:
                    self.nextseg.spawn()

            def showpos(self):
                if self.nextseg!= None:
                    self.nextseg.showpos()
                print("({0},{1})".format(self.pos[0], self.pos[1]), end = "")
                if self.nextseg == None:
                    print(" I'm the head!")

            def dropbomb(self):
                mybomb = bombseg(None, self.pos)
                mysegs.append(mybomb)
                self.bombcounter = 0

            def explode(self):
                mysplode = explosion(self.pos)
                mysegs.append(mysplode)

            def bombcheck(self):
                self.bombcounter += 1
                if self.bombcounter > 500 and random.randint(0,50) == 20:
                    self.dropbomb()



        class bombseg(segment):      #cootie bombs inherit from segment for collisions etc

            def __init__(self, nextseg = None, pos = (-20,20)):
                self.pos = pos
                self.speed = 3
                self.right = True
                self.nextseg = nextseg
                self.pos2 = pos
                self.pos3 = pos
                self.frame = bomb
                self.cootieballrect = bomb.get_rect()
                self.cootieballrect.center = pos
                self.framecount = random.randint(0,5)


            def update(self):

                self.pos = (self.pos[0], self.pos[1]+self.speed)
                self.speed += 1
                self.cootieballrect.center = self.pos
                if self.pos[1] >= screenheight:
                    self.killseg()

                screen.blit(self.frame, self.cootieballrect)


        class housecootie(segment):   #this guy runs around the house
            def __init__(self, nextseg = None, pos = (-20 ,screenheight - ceiling)):
                self.pos = pos
                self.speed = 1
                self.right = True
                self.nextseg = nextseg
                self.pos2 = pos
                self.pos3 = pos
                self.frame = house1
                self.cootieballrect = house1.get_rect()
                self.cootieballrect.center = pos
                self.framecount = random.randint(0,5)
                self.fallspeed = 1

            def update(self):

                if self.fallspeed < 0:
                    self.frame = house1

                else:
                    self.frame = house2




                if self.right:
                    self.pos = (self.pos[0]+self.speed, self.pos[1]+self.fallspeed)
                    self.cootieballrect.center = self.pos
                    if self.cootieballrect.center[0] > screenwidth:
                        self.right = False


                else:
                    self.pos = (self.pos[0]-self.speed, self.pos[1]+self.fallspeed)
                    self.cootieballrect.center = self.pos
                    if self.cootieballrect.center[0] < 0:
                        self.right = True

                self.fallspeed += 1
                if self.pos[1] >= screenheight - 15:
                    self.fallspeed = -random.randint(10,25)
                    print(self.fallspeed)

                screen.blit(self.frame, self.cootieballrect)

            def killseg(self):
                #insert explosion code?

                mysegs.remove(self)
                level.remhc()

        class bomber(segment): #bomber segment class to drop many bombs, boooom
            def __init__(self, nextseg = None, pos = (-20 ,20)):
                self.pos = pos
                self.speed = 2
                self.right = True
                self.nextseg = nextseg
                self.pos2 = pos
                self.pos3 = pos
                self.frame = bomber1
                self.cootieballrect = bomber1.get_rect()
                self.cootieballrect.center = pos
                self.framecount = random.randint(0,5)
                self.bombcounter = 0

            def bombcheck(self):
                self.bombcounter += 1
                if self.bombcounter > 5 and random.randint(0,10) == 10:
                    self.dropbomb()

            def update(self):

                if self.framecount == 10:
                    if self.frame == bomber1:
                        self.frame = bomber2
                        2
                    else:
                        self.frame = bomber1
                    self.framecount = 0
                self.framecount += 1


                if self.right:
                    self.pos = (self.pos[0]+self.speed, self.pos[1])
                    self.cootieballrect.center = self.pos
                    if self.cootieballrect.center[0] > screenwidth:
                        self.killseg()


                else:
                    self.pos = (self.pos[0]-self.speed, self.pos[1])
                    self.cootieballrect.center = self.pos
                    if self.cootieballrect.center[0] < 0:
                        self.killseg()

                self.bombcheck()
                #self.cootieballrect.center = self.pos
                screen.blit(self.frame, self.cootieballrect)



        class player:
            def __init__(self):
                self.pos = (screenwidth // 2, screenheight - 40)
                self.img = spaceship   # make player image
                self.uboundary = screenheight - ceiling
                self.lboundary = screenheight -30
                self.speed = (0,0)
                self.playerrect=self.img.get_rect()

            def reset(self):
                self.pos = (screenwidth // 2, screenheight - 40)


            def update(self):


                self.pos =(self.pos[0] + self.speed[0], self.pos[1] + self.speed[1])
                if self.pos[1] < self.uboundary or self.pos[1] > self.lboundary:
                    self.pos =(self.pos[0], self.pos[1] - self.speed[1])
                if self.pos[0] < 20 or self.pos[0] > screenwidth - 20:
                    self.pos = (self.pos[0] - self.speed[0], self.pos[1])
                self.playerrect.center = self.pos
                if collisions:
                    self.checkcollision()
                screen.blit(self.img, self.playerrect)


            def checkcollision(self):
                global isalive
                global gamelives
                for coot in mysegs:
                    if coot.iscollided(self.playerrect) != None:
                        #print("I'm Dead!")
                        deathsnd.play()
                        for i in range(255, 0, -1):
                            screen.fill( (i, i, i))
                            clock.tick(60)
                            pygame.display.flip()


                        isalive = False
                        updatelives(-1)



        def updatescore(points):
            global score
            global gamescore
            gamescore = 0
            gamescore += points
            score = myfont.render("SCORE: {0}".format(gamescore), True, (255,255,255))

        def updatelives(life):
            global lives
            global gamelives
            gamelives = 0
            gamelives += life
            lives = myfont.render(" LIVES: {0}".format(gamelives), True, (255,255,255))

        def updatelevel(lev):
            global leveltext
            leveltext = myfont.render("LEVEL {0}".format(lev), True, (200, 0, 0))


        class levelstate:
            def __init__(self):
                self.level = 0
                self.timer = time.clock()
                #self.nextspawn = 5
                self.levels = gamelevels
                self.level = None
                self.levelnum = 0
                self.segments = 0
                self.length = 0
                self.interval = 0
                self.numhc = 0
                self.restarted = True
                self.displaycount = 0


            def getlevel(self):
                if self.levelnum < len(self.levels):
                    self.segments, self.length, self.interval, self.bombers, self.housecooties = self.levels[self.levelnum]
        ##            if restarted == False:
        ##                del self.levels[0]

                else:
                    self.segments = 5
                    self.length = 12
                    self.interval = 3
                    self.bombers = True
                    self.housecooties = 3
                self.levelnum += 1




            def remhc(self):
                self.numhc -= 1

            def levelcheck(self):
                global showlevel

                if self.displaycount <=0:
                    showlevel = False
                else:
                    self.displaycount -= 1
                if time.clock() > self.timer + self.interval or self.restarted: #hacky check to see if the level is starting
                    if self.segments == 0:
                        if len(mysegs) == 0:
                            self.getlevel()
                            updatelevel(self.levelnum)
                            showlevel = True
                            self.displaycount = 120
                        else:
                            if self.numhc < self.housecooties:
                                if self.bombers:
                                    if random.randint(0,6) == 3:
                                        self.spawnbomber()
                                self.spawnhousecootie()
                                self.numhc += 1
                    elif self.segments > 0:
                        self.spawnseg()
                        self.segments -= 1
                        if self.segments == 0:
                            if self.bombers:
                                self.spawnbomber()

                    if self.restarted:
                        self.timer = time.clock() - (self.interval - 1)
                        self.restarted = False
                    else:
                        self.timer = time.clock()

            def restart(self):
                self.restarted = True
                self.levelnum -= 1



            def spawnseg(self):
                newseg = segment()
                if random.randint(0,1) == 1:
                    newseg.pos = (screenwidth + 20, -10)
                newseg.grow(self.length)
                mysegs.append(newseg)

            def spawnbomber(self):
                newseg = bomber()
                if random.randint(0,1) == 1:
                    newseg.pos = (screenwidth + 20, 30)
                    newseg.right = False
                mysegs.append(newseg)

            def spawnhousecootie(self):
                newseg = housecootie()
                if random.randint(0,1) == 1:
                    newseg.pos = (screenwidth + 20, screenheight - ceiling)
                    newseg.right = False
                mysegs.append(newseg)



        def titlescreen():
            mytitle = title
            titlerect = mytitle.get_rect()
            titlerect.center = (screenwidth / 2, 300)
            timer = time.clock()
            pygame.event.clear()
            while True:
                if time.clock() > timer + 2:
                    if mytitle == title:
                        mytitle = title2
                    else:
                        mytitle = title
                    timer = time.clock()

                ev = pygame.event.poll()
                if ev.type == pygame.QUIT:

                    pygame.quit()
                    sys.exit()
                    break
                if ev.type == pygame.KEYDOWN:
                    key = ev.dict['key']
                    #print(key)
                    if key == 27:                  # On Escape key ...
                        pygame.quit()
                        sys.exit()
                        break                      #   leave the game loop.

                    if key == 32:
                        break



                screen.fill( (0, 0, 0))
                screen.blit(mytitle, titlerect)
                screen.blit(instructions, instructrect)
                clock.tick(60)
                pygame.display.flip()

            return


        def gameover():
            titlerect = gameovertitle.get_rect()
            titlerect.center = (screenwidth / 2, 300)
            timer = time.clock()
            while time.clock() < timer + 5:
                ev = pygame.event.poll()
                if ev.type == pygame.QUIT:

                    pygame.quit()
                    sys.exit()
                    break
                if ev.type == pygame.KEYDOWN:
                    key = ev.dict['key']
                    #print(key)
                    if key == 27:                  # On Escape key ...
                        pygame.quit()
                        sys.exit()
                        break

                screen.fill( (0, 0, 0))
                screen.blit(gameovertitle, titlerect)
                screen.blit(score, scorerect)
                screen.blit(lives, livesrect)

                clock.tick(60)
                pygame.display.flip()

            return



        def quitgame():
            pygame.quit()
            sys.exit()



        def gameloop():

            #player1 = player()
            #mysegs = []
            #myshots = []

        ##myshot = shot()
        ##myshots.append(myshot)
            #mypos = (25, 300)
            #myseg=segment()
            #myseg.grow(5)
            #mysegs.append(myseg)
            #mybomb = bombseg(None, mypos)

            #mysegs.append(mybomb)

            #level.levelcheck()
            #level.spawnseg()

            while isalive:

                level.levelcheck()
                ev = pygame.event.poll()
                if ev.type == pygame.QUIT:
                    quitgame()
                    break;
                if ev.type == pygame.KEYDOWN:
                    key = ev.dict['key']
                    #print(key)
                    if key == 27:                  # On Escape key ...
                        quitgame()
                        break                      #   leave the game loop.
                    if key == ord('p'):
                        newseg=segment()
                        newseg.grow(5)
                        mysegs.append(newseg)
                    if key == ord('w') or key == 273:
                        player1.speed = (player1.speed[0], player1.speed[1]-playerspeed)
                    if key == ord('s') or key == 274:
                        player1.speed = (player1.speed[0], player1.speed[1]+playerspeed)
                    if key == ord('a') or key == 276:
                        player1.speed = (player1.speed[0] -playerspeed, player1.speed[1])
                    if key == ord('d') or key == 275:
                        player1.speed = (player1.speed[0] +playerspeed, player1.speed[1])
                    if key == 32:
                        if len(myshots) < maxshots:
                            shotsnd.play()
                            newshot = shot()
                            myshots.append(newshot)



                if ev.type == pygame.KEYUP:
                    key = ev.dict['key']
                    #print(key)
                    if key == ord('w') or key == 273:
                        player1.speed = (player1.speed[0], player1.speed[1]+playerspeed)
                    if key == ord('s') or key == 274:
                        player1.speed = (player1.speed[0], player1.speed[1]-playerspeed)
                    if key == ord('a') or key == 276:
                        player1.speed = (player1.speed[0] +playerspeed, player1.speed[1])
                    if key == ord('d') or key == 275 :
                        player1.speed = (player1.speed[0] -playerspeed, player1.speed[1])


                screen.fill( (0, 0, 0))

                if showlevel:
                    screen.blit(leveltext, levelrect)
                screen.blit(score, scorerect)
                screen.blit(lives, livesrect)
                for seg in mysegs:
                    seg.update()

                for shooted in myshots:
                    shooted.update()



                player1.update()
                clock.tick(60)
                pygame.display.flip()
                #print(player1.speed)

        while True:
            titlescreen()
            titlemusic.stop()
            music.play(-1)
            player1 = player()
            mysegs = []
            myshots = []
            level = levelstate()
            gamescore = 0
            updatescore(0)
            gamelives = playerlives
            updatelives(0)


            while gamelives:

                gameloop()
                mysegs = []
                player1.reset()
                level.restart()
                isalive = True

            gameover()
            music.stop()
            titlemusic.play(-1)

        quitgame()

    def Bullets():

        import pygame
        import random

        # Define some colors
        BLACK    = (   0,   0,   0)
        WHITE    = ( 255, 255, 255)
        RED      = ( 255,   0,   0)
        BLUE     = (   0,   0, 255)

        # --- Classes

        class Block(pygame.sprite.Sprite):
            """ This class represents the block. """
            def __init__(self, color):
                # Call the parent class (Sprite) constructor
                super().__init__()

                self.image = pygame.Surface([20, 15])
                self.image.fill(color)

                self.rect = self.image.get_rect()

        class Player(pygame.sprite.Sprite):
            """ This class represents the Player. """

            def __init__(self):
                """ Set up the player on creation. """
                # Call the parent class (Sprite) constructor
                super().__init__()

                self.image = pygame.Surface([20, 20])
                self.image.fill(RED)

                self.rect = self.image.get_rect()

            def update(self):
                """ Update the player's position. """
                # Get the current mouse position. This returns the position
                # as a list of two numbers.
                pos = pygame.mouse.get_pos()

                # Set the player x position to the mouse x position
                self.rect.x = pos[0]

        class Bullet(pygame.sprite.Sprite):
            """ This class represents the bullet . """
            def __init__(self):
                # Call the parent class (Sprite) constructor
                super().__init__()

                self.image = pygame.Surface([4, 10])
                self.image.fill(BLACK)

                self.rect = self.image.get_rect()

            def update(self):
                """ Move the bullet. """
                self.rect.y -= 3


        # --- Create the window

        # Initialize Pygame
        pygame.init()

        # Set the height and width of the screen
        screen_width = 700
        screen_height = 400
        screen = pygame.display.set_mode([screen_width, screen_height])

        # --- Sprite lists

        # This is a list of every sprite. All blocks and the player block as well.
        all_sprites_list = pygame.sprite.Group()

        # List of each block in the game
        block_list = pygame.sprite.Group()

        # List of each bullet
        bullet_list = pygame.sprite.Group()

        # --- Create the sprites

        for i in range(50):
            # This represents a block
            block = Block(BLUE)

            # Set a random location for the block
            block.rect.x = random.randrange(screen_width)
            block.rect.y = random.randrange(350)

            # Add the block to the list of objects
            block_list.add(block)
            all_sprites_list.add(block)

        # Create a red player block
        player = Player()
        all_sprites_list.add(player)

        #Loop until the user clicks the close button.
        done = False

        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()

        score = 0
        player.rect.y = 370

        # -------- Main Program Loop -----------
        while not done:
            # --- Event Processing
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Fire a bullet if the user clicks the mouse button
                    bullet = Bullet()
                    # Set the bullet so it is where the player is
                    bullet.rect.x = player.rect.x
                    bullet.rect.y = player.rect.y
                    # Add the bullet to the lists
                    all_sprites_list.add(bullet)
                    bullet_list.add(bullet)

            # --- Game logic

            # Call the update() method on all the sprites
            all_sprites_list.update()

            # Calculate mechanics for each bullet
            for bullet in bullet_list:

                # See if it hit a block
                block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)

                # For each block hit, remove the bullet and add to the score
                for block in block_hit_list:
                    bullet_list.remove(bullet)
                    all_sprites_list.remove(bullet)
                    score += 1
                    print(score)

                # Remove the bullet if it flies up off the screen
                if bullet.rect.y < -10:
                    bullet_list.remove(bullet)
                    all_sprites_list.remove(bullet)

            # --- Draw a frame

            # Clear the screen
            screen.fill(WHITE)

            # Draw all the spites
            all_sprites_list.draw(screen)

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # --- Limit to 20 frames per second
            clock.tick(60)

        pygame.quit()


    def Brick_Breaker():

        # --- Import libraries used for this program

        import math
        import pygame

        # Define some colors
        black = (0, 0, 0)
        white = (255, 255, 255)
        blue = (0, 0, 255)

        # Size of break-out blocks
        block_width = 23
        block_height = 15

        class Block(pygame.sprite.Sprite):
            """This class represents each block that will get knocked out by the ball
            It derives from the "Sprite" class in Pygame """

            def __init__(self, color, x, y):
                """ Constructor. Pass in the color of the block, 
                    and its x and y position. """
                
                # Call the parent class (Sprite) constructor
                super().__init__()
                
                # Create the image of the block of appropriate size
                # The width and height are sent as a list for the first parameter.
                self.image = pygame.Surface([block_width, block_height])
                
                # Fill the image with the appropriate color
                self.image.fill(color)
                
                # Fetch the rectangle object that has the dimensions of the image
                self.rect = self.image.get_rect()
                
                # Move the top left of the rectangle to x,y.
                # This is where our block will appear..
                self.rect.x = x
                self.rect.y = y


        class Ball(pygame.sprite.Sprite):
            """ This class represents the ball        
                It derives from the "Sprite" class in Pygame """
            
            # Speed in pixels per cycle
            speed = 10.0
            
            # Floating point representation of where the ball is
            x = 0.0
            y = 180.0
            
            # Direction of ball (in degrees)
            direction = 200

            width = 10
            height = 10
            
            # Constructor. Pass in the color of the block, and its x and y position
            def __init__(self):
                # Call the parent class (Sprite) constructor
                super().__init__()
                
                # Create the image of the ball
                self.image = pygame.Surface([self.width, self.height])
                
                # Color the ball
                self.image.fill(white)
                
                # Get a rectangle object that shows where our image is
                self.rect = self.image.get_rect()
                
                # Get attributes for the height/width of the screen
                self.screenheight = pygame.display.get_surface().get_height()
                self.screenwidth = pygame.display.get_surface().get_width()
            
            def bounce(self, diff):
                """ This function will bounce the ball 
                    off a horizontal surface (not a vertical one) """
                
                self.direction = (180 - self.direction) % 360
                self.direction -= diff
            
            def update(self):
                """ Update the position of the ball. """
                # Sine and Cosine work in degrees, so we have to convert them
                direction_radians = math.radians(self.direction)
                
                # Change the position (x and y) according to the speed and direction
                self.x += self.speed * math.sin(direction_radians)
                self.y -= self.speed * math.cos(direction_radians)
                
                # Move the image to where our x and y are
                self.rect.x = self.x
                self.rect.y = self.y
                
                # Do we bounce off the top of the screen?
                if self.y <= 0:
                    self.bounce(0)
                    self.y = 1
                    
                # Do we bounce off the left of the screen?
                if self.x <= 0:
                    self.direction = (360 - self.direction) % 360
                    self.x = 1
                    
                # Do we bounce of the right side of the screen?
                if self.x > self.screenwidth - self.width:
                    self.direction = (360 - self.direction) % 360
                    self.x = self.screenwidth - self.width - 1
                
                # Did we fall off the bottom edge of the screen?
                if self.y > 600:
                    return True
                else:
                    return False

        class Player(pygame.sprite.Sprite):
            """ This class represents the bar at the bottom that the player controls. """
            
            def __init__(self):
                """ Constructor for Player. """
                # Call the parent's constructor
                super().__init__()
                
                self.width = 75
                self.height = 15
                self.image = pygame.Surface([self.width, self.height])
                self.image.fill((white))
                
                # Make our top-left corner the passed-in location.
                self.rect = self.image.get_rect()
                self.screenheight = pygame.display.get_surface().get_height()
                self.screenwidth = pygame.display.get_surface().get_width()

                self.rect.x = 0
                self.rect.y = self.screenheight-self.height
            
            def update(self):
                """ Update the player position. """
                # Get where the mouse is
                pos = pygame.mouse.get_pos()
                # Set the left side of the player bar to the mouse position
                self.rect.x = pos[0]
                # Make sure we don't push the player paddle 
                # off the right side of the screen
                if self.rect.x > self.screenwidth - self.width:
                    self.rect.x = self.screenwidth - self.width

        # Call this function so the Pygame library can initialize itself
        pygame.init()

        # Create an 800x600 sized screen
        screen = pygame.display.set_mode([800, 600])

        # Set the title of the window
        pygame.display.set_caption('Breakout')

        # Enable this to make the mouse disappear when over our window
        pygame.mouse.set_visible(0)

        # This is a font we use to draw text on the screen (size 36)
        font = pygame.font.Font(None, 36)

        # Create a surface we can draw on
        background = pygame.Surface(screen.get_size())

        # Create sprite lists
        blocks = pygame.sprite.Group()
        balls = pygame.sprite.Group()
        allsprites = pygame.sprite.Group()

        # Create the player paddle object
        player = Player()
        allsprites.add(player)

        # Create the ball
        ball = Ball()
        allsprites.add(ball)
        balls.add(ball)

        # The top of the block (y position)
        top = 80

        # Number of blocks to create
        blockcount = 32

        # --- Create blocks

        # Five rows of blocks
        for row in range(5):
            # 32 columns of blocks
            for column in range(0, blockcount):
                # Create a block (color,x,y)
                block = Block(blue, column * (block_width + 2) + 1, top)
                blocks.add(block)
                allsprites.add(block)
            # Move the top of the next row down
            top += block_height + 2

        # Clock to limit speed
        clock = pygame.time.Clock()

        # Is the game over?
        game_over = False

        # Exit the program?
        exit_program = False

        # Main program loop
        while exit_program != True:

            # Limit to 30 fps
            clock.tick(30)

            # Clear the screen
            screen.fill(black)
            
            # Process the events in the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_program = True
            
            # Update the ball and player position as long
            # as the game is not over.
            if not game_over:
                # Update the player and ball positions
                player.update()
                game_over = ball.update()
            
            # If we are done, print game over
            if game_over:
                text = font.render("Game Over", True, white)
                textpos = text.get_rect(centerx=background.get_width()/2)
                textpos.top = 300
                screen.blit(text, textpos)
            
            # See if the ball hits the player paddle
            if pygame.sprite.spritecollide(player, balls, False):
                # The 'diff' lets you try to bounce the ball left or right 
                # depending where on the paddle you hit it
                diff = (player.rect.x + player.width/2) - (ball.rect.x+ball.width/2)
                
                # Set the ball's y position in case 
                # we hit the ball on the edge of the paddle
                ball.rect.y = screen.get_height() - player.rect.height - ball.rect.height - 1
                ball.bounce(diff)
            
            # Check for collisions between the ball and the blocks
            deadblocks = pygame.sprite.spritecollide(ball, blocks, True)
            
            # If we actually hit a block, bounce the ball
            if len(deadblocks) > 0:
                ball.bounce(0)
                
                # Game ends if all the blocks are gone
                if len(blocks) == 0:
                    game_over = True
            
            # Draw Everything
            allsprites.draw(screen)

            # Flip the screen and show what we've drawn
            pygame.display.flip()

        pygame.quit()
        
class Scroll_Events():
    def _bound_to_mousewheel(event):
        canvas.bind_all("<MouseWheel>", Scroll_Events._on_mousewheel_y)     

    def _unbound_to_mousewheel(event):
        canvas.unbind_all("<MouseWheel>") 
        
    def _on_mousewheel_y(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")     
          
    def onFrameConfigure(event):
        '''Reset the scroll region to encompass the inner frame'''
        canvas.configure(scrollregion=canvas.bbox("all"))
    
    
def main():

    root = Tk()

    root.title('MeshWare Console')
    root.resizable(True, True)
    root.configure(background = 'grey', padx = 10, pady = 10, relief = SUNKEN)
    sizex = 800
    sizey = 500
    posx  = 0
    posy  = 0
    root.geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
    
    style_main = ttk.Style()
    style_main.theme_use("default")
    style_main.configure("main.TButton",
                         foreground="black",)

    s = ttk.Style()
    s.theme_use("default")
    s.configure("TProgressbar", thickness=22)
##    s.configure('TButton', background = 'gold')
    #s.configure('TFrame', background = '#e1d8b9')

    ##style = ttk.Style()
    ##root.style.configure('TFrame', background = '#e1d8b9')
    ##root.style.configure('TButton', background = '#e1d8b9')
    ##root.style.configure('TLabel', background = '#e1d8b9', font = ('Arial', 11))
    ##root.style.configure('Header.TLabel', font = ('Arial', 18, 'bold')) 

    root.option_add('*tearOff', False)
    menubar = Menu(root)
    root.config(menu = menubar)
    file = Menu(menubar)
    edit = Menu(menubar)
    help_ = Menu(menubar)

    menubar.add_cascade(menu = file, label = 'File')
    menubar.add_cascade(menu = edit, label = 'Edit')
    menubar.add_cascade(menu = help_, label = 'Help')

    file.add_command(label = 'New', command = lambda: print('New File'))
    file.add_separator()
    file.add_command(label = 'Open...', command = lambda: print('Opening File...'))
    file.add_command(label = 'Save', command = Input_Frame.save_session)

    file.entryconfig('New', accelerator = 'Ctrl+N')
    file.entryconfig('Save', accelerator = 'Ctrl+S')

    #from PIL import Image
    #from PIL import ImageTk

    #image = Image.open("C:\\Users\\Zachary Roper\\Desktop\\MWlogo1.jpg")
    #logo = ImageTk.PhotoImage(image)
    #file.entryconfig('Open...', image = logo, compound = 'left')
    #file.entryconfig('Open...', state = 'disabled')

##    file.delete('Save')
##    save = Menu(file)
##    file.add_cascade(menu = save, label = 'Save')
##    save.add_command(label = 'Save As',command = lambda: print('Saving As...'))
##    save.add_command(label = 'Save All', command = lambda: print('Saving All...'))

    choice = IntVar()
    edit.add_radiobutton(label = 'One', variable = choice, value = 1)
    edit.add_radiobutton(label = 'Two', variable = choice, value = 2)
    edit.add_radiobutton(label = 'Three', variable = choice, value = 3)

    #scrollbar = ttk.Scrollbar(root, orient = VERTICAL, command = root.yview)
    #scrollbar.grid(row = 0, column = 1, sticky = 'ns')
    #root.config(yscrollcommand = scrollbar.set)

    logo = PhotoImage(file = 'C:\\Users\\Zachary Roper\\Desktop\
    \MeshWare\\logo_MWbadge_gold.gif').subsample(10, 10)

    headTexture = PhotoImage(file = 'C:\\Users\\Zachary Roper\
    \Desktop\\MeshWare\\head_MWtexture.gif')#.subsample(10, 10)

    Welcomeframe = ttk.Frame(root, relief = SUNKEN)
    Welcomeframe.pack(fill = BOTH)
    #Welcome = ttk.Label(Welcomeframe, image = headTexture)
    Welcome = Label(Welcomeframe, text = 'MeshWare', relief = RAISED)
    Welcome2 = Label(Welcomeframe, text = 'Welcome to the desktop platform!')

    Welcome.pack(fill = X, expand = True)
    Welcome2.pack(fill = X, expand = True)
    #Welcome2.config(padding = (0,10))
    Welcome.config(foreground = 'gold', background = 'grey')
    Welcome2.config(foreground = 'black', background = 'gold')
    #Welcome.config(wraplength = 150)
    Welcome.config(justify = CENTER)
    Welcome.config(font = ('Helvetica', 32, 'bold'))
    Welcome2.config(justify = CENTER)
    Welcome2.config(font = ('Helvetica', 8, 'bold'))


    panedwindow = ttk.Panedwindow(root, orient = HORIZONTAL)
    panedwindow.pack(fill = BOTH, expand = True)

    frame1 = ttk.Frame(panedwindow, width = 100, height = 300)
    frame2 = ttk.Frame(panedwindow, width = 900, height = 300, relief = SUNKEN)
    panedwindow.add(frame1, weight = 10)
    panedwindow.add(frame2, weight = 90)
    
    frame0 = Frame(frame1,
                   relief = SUNKEN,
                   width = 250)
    frame0.pack(fill = BOTH, expand = True)
    
    ##Pack notebook (tabbed browser)######
    notebook = ttk.Notebook(frame2)
    notebook.pack(fill = BOTH, expand = True)

    ##Tasks tab#####

    
    tab0 = ttk.Frame(notebook)
    notebook.add(tab0, text = 'Tasks')

    global tasks_tab_frame
    tasks_tab_frame = Frame(tab0)
    tasks_tab_frame.pack(fill = BOTH, expand = True)

    ##Pack task label into tasks tab
    tasks_tab_label = Label(tasks_tab_frame, text = 'Welcome to the Tasks tab', foreground = 'gold', background = 'black')
    tasks_tab_label.pack(fill = X)

    ##pack Killable frame
    global buttonframe
    buttonframe = Frame(tasks_tab_frame,
                        relief = SUNKEN)
    buttonframe.pack(fill = BOTH, expand = True)
    #ScrollCanvas(buttonframe).pack(side="top", fill="both", expand=True)
    
    load_dict = Load_Dict()
    paint_em_up = Load_Dict.Load_Button_Values(test_verb_dict)
    input_panel = Input_Frame(frame0, buttonframe)
    global canvas
    canvas = Canvas(buttonframe, borderwidth=0, background='black', bd=-50)
    frame_on_canvas = ttk.Frame(canvas)
    
    ##Pack paned window in tasks tab
    global tasks_tab_panedwindow
    tasks_tab_panedwindow = ttk.Panedwindow(frame_on_canvas, orient = HORIZONTAL)
    tasks_tab_panedwindow.pack(fill = 'x', expand = True)
    vsb = Scrollbar(buttonframe, orient="vertical", command=canvas.yview)
    hsb = Scrollbar(buttonframe, orient="horizontal", command=canvas.xview)
    canvas.configure(yscrollcommand=vsb.set)
    canvas.configure(xscrollcommand=hsb.set)
    
    ##Add panes to Task tab paned window
    global ttpw_taskpane
    ttpw_taskpane = ttk.Frame(tasks_tab_panedwindow, relief = SUNKEN)
    global ttpw_subtaskpane
    ttpw_subtaskpane = ttk.Frame(tasks_tab_panedwindow, relief = SUNKEN)

    vsb.pack(side="right", fill="y")
    hsb.pack(side="bottom", fill="x")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((0,0), window=frame_on_canvas, anchor="nw", 
                              tags="frame_on_canvas")
    

    tasks_tab_panedwindow.add(ttpw_taskpane, weight = 1)
    tasks_tab_panedwindow.add(ttpw_subtaskpane, weight = 4)
    
    frame_on_canvas.bind("<Configure>", Scroll_Events.onFrameConfigure)
    frame_on_canvas.bind('<Enter>', Scroll_Events._bound_to_mousewheel)
    frame_on_canvas.bind('<Leave>', Scroll_Events._unbound_to_mousewheel)

        
    
    ##Tasks pane

    pack_tasks = Build_Buttons.pack_buttons(ttpw_taskpane)
    
    ##Subtask frame and label packed into the subtask pane

    grid_subtasks = Build_Buttons.grid_buttons(ttpw_subtaskpane)
    

##    ##DEFCON label
##    DEFCON_label_frame = ttk.Frame(ttpw_DEFCONpane)
##    DEFCON_label_frame.pack(fill = X)
##
##    DEFCON_label = Label(DEFCON_label_frame, text = 'DEFCON', justify = 'center')
##    DEFCON_label.pack(fill = X)


    ##Schedule tab
    tab1 = ttk.Frame(notebook)
    notebook.add(tab1, text = 'Schedule')

    schedules_tab_frame = Frame(tab1)
    schedules_tab_frame.pack(fill = X)

    schedules_tab_label = Label(schedules_tab_frame, text = 'Welcome to the Schedule tab', foreground = 'gold', background = 'black')
    schedules_tab_label.pack(fill = X)

    import calendar
    import datetime

    now = datetime.datetime.now()
    this_year = now.year
    this_month = 1#now.month
    this_day = now.day
    this_hour = now.hour
    this_minute = now.minute
    this_second = now.second

    c = calendar.TextCalendar(calendar.SUNDAY)
    month_array = {}
    mo = 1
    
    for m in range(12):
        if this_month == 1:
            month_array[m] = c.formatmonth(this_year,mo)
##            print(month_array[m])
        elif this_month == 2:
            month_array[m] = c.formatmonth(this_year,mo)
        mo += 1
##    current_month_cal = c.formatmonth(this_year,this_month)
##    next_month_cal = c.formatmonth(this_year,this_month + 1)

    #calendar_frame = ttk.Frame(tab1)
    #calendar_frame.pack(fill = X)

    schedule_panes = ttk.Panedwindow(tab1, orient = HORIZONTAL)
    schedule_panes.pack(fill = BOTH, expand = True)

    sp_view_frame = ttk.Frame(schedule_panes, width = 50, relief = SUNKEN)
    sp_cal_frame = ttk.Frame(schedule_panes, width = 50, relief = SUNKEN)
    schedule_panes.add(sp_view_frame, weight = 1)
    schedule_panes.add(sp_cal_frame, weight = 3)

    ##Schedule view pane
    schedule_label_frame = ttk.Frame(sp_view_frame)
    schedule_label_frame.pack(fill = X)

    schedule_label = Label(schedule_label_frame, text = 'calendar views', justify = 'center')
    schedule_label.pack(fill = X)

    ##Schedule view button frames
    schedule_view_buttonframe0 = ttk.Frame(sp_view_frame, relief = SUNKEN)
    schedule_view_buttonframe0.pack(fill = X)
    schedule_view_buttonframe1 = ttk.Frame(sp_view_frame, relief = SUNKEN)
    schedule_view_buttonframe1.pack(fill = X)
    schedule_view_buttonframe2 = ttk.Frame(sp_view_frame, relief = SUNKEN)
    schedule_view_buttonframe2.pack(fill = X)
    schedule_view_buttonframe3 = ttk.Frame(sp_view_frame, relief = SUNKEN)
    schedule_view_buttonframe3.pack(fill = X)

    ##Schedule view buttons
    schedule_view_button0 = ttk.Button(schedule_view_buttonframe0, text = 'day')
    schedule_view_button0.pack(fill = X)
    schedule_view_button1 = ttk.Button(schedule_view_buttonframe1, text = 'week')
    schedule_view_button1.pack(fill = X)
    schedule_view_button2 = ttk.Button(schedule_view_buttonframe2, text = 'month')
    schedule_view_button2.pack(fill = X)
    schedule_view_button3 = ttk.Button(schedule_view_buttonframe3, text = 'year')
    schedule_view_button3.pack(fill = X)

    ttkcal = Calendar(sp_cal_frame, firstweekday=calendar.SUNDAY)
    ttkcal.pack(side = LEFT)

    ##Pack Months
##    count = 0
##    for r in range(3):
##        for c in range(4):
##            month_cal_frame = ttk.Frame(sp_cal_frame)
##            month_cal_frame.grid(row = r, column = c, pady = 5)
##            month_cal_label = Label(month_cal_frame, text = month_array[count], background = 'grey')
##            month_cal_label.pack(side = TOP, expand = True)
##            count += 1
            
##    current_month_cal_label = Label(sp_cal_frame, text = current_month_cal)
##    current_month_cal_label.grid(fill = X)
##    next_month_cal_label = Label(sp_cal_frame, text = next_month_cal)
##    next_month_cal_label.grid(fill = X)

    ##Progress tab
    tab2 = ttk.Frame(notebook)
    notebook.add(tab2, text = 'Progress')

    global progress_tab_frame
    progress_tab_frame = Frame(tab2)
    progress_tab_frame.pack(fill = BOTH, expand = True)

    progress_tab_label = Label(progress_tab_frame, text = 'Welcome to the Progress tab', foreground = 'gold', background = 'black')
    progress_tab_label.pack(fill = X)

    ###Killable progress pane
    global progressframe
    progressframe = Frame(progress_tab_frame,
                        relief = SUNKEN)
    progressframe.pack(fill = BOTH, expand = True)

    ##Progress paned windows
    ProgressbarPanes = ttk.Panedwindow(progressframe, orient = HORIZONTAL)
    ProgressbarPanes.pack(fill = BOTH, expand = True)

    global progresstab_taskpane
    global barsframe
    global statsframe1
    global statsframe2
    progresstab_taskpane = Frame(ProgressbarPanes, width = 100, height = 200, relief = SUNKEN)
    barsframe = Frame(ProgressbarPanes, width = 200, height = 200, relief = SUNKEN, bg = 'black')
    statsframe1 = Frame(ProgressbarPanes, width = 50, height = 200, relief = SUNKEN, bg = 'black')
    statsframe2 = Frame(ProgressbarPanes, width = 50, height = 200, relief = SUNKEN, bg = 'black')

    ProgressbarPanes.add(progresstab_taskpane, weight = 2)
    ProgressbarPanes.add(barsframe, weight = 6)
    ProgressbarPanes.add(statsframe1, weight = 1)
    ProgressbarPanes.add(statsframe2, weight = 1)

    ##Shopping tab
    tab3 = ttk.Frame(notebook)
    notebook.add(tab3, text = 'Shopping')

    ttk.Button(tab3, text = 'Buy Me!').pack()

    ##Wallet tab
    tab4 = ttk.Frame(notebook)
    notebook.add(tab4, text = 'Wallet')
    
    Balances_frame = ttk.Frame(tab4)
    Balances_frame.pack()

    Balances_label = Label(Balances_frame, text = 'Balances', foreground = 'black', background = 'gold')
    Balances_label.pack(fill=X)
    Balances_label.config(justify =CENTER)
    
    Balances = ttk.Frame(Balances_frame)
    Balances.pack(fill=X, expand=True)
    referential = {}

    balance_headers = ['Coin', 'Name', 'Balance', 'BTC Equivalent', 'Actions']
    coin_abb = ['BTC', 'ETH', 'JCH']
    coin_names = ['Bitcoin', 'Ethereum', 'Joulecache']
    coin_balances = ['50.00', '150.00', '400']
    coin_balances_btc_equiv = ['50.00', '51.00', '52.00']
    coin_actions = ['Deposit Withdraw', 'Deposit Withdraw', 'Deposit Withdraw']
    
    for value in balance_headers:
        e = Label(Balances, text = value, foreground = 'gold', background = 'black')
        e.grid(row=0, column=balance_headers.index(value), stick='nesw')
        e.config(justify=CENTER)
        e.columnconfigure(0, weight=2)
        referential[0,balance_headers.index(value)] = e
    for value in coin_abb:
        e = Entry(Balances, foreground = 'black', background = 'white')
        e.grid(row=coin_abb.index(value)+1, column=0, stick='nesw')
        e.insert(0, value)
        e.config(justify=CENTER, state=DISABLED)
        e.columnconfigure(0, weight=2)
        referential[0,coin_abb.index(value)] = e
    for value in coin_names:
        e = Entry(Balances, foreground = 'black', background = 'white')
        e.grid(row=coin_names.index(value)+1, column=1, stick='nesw')
        e.insert(0, value)
        e.config(justify=CENTER, state=DISABLED)
        e.columnconfigure(0, weight=2)
        referential[0,coin_names.index(value)] = e    
    for value in coin_balances:
        e = Entry(Balances, foreground = 'black', background = 'white')
        e.grid(row=coin_balances.index(value)+1, column=2, stick='nesw')
        e.insert(0, value)
        e.config(justify=CENTER, state=DISABLED)
        e.columnconfigure(0, weight=2)
        referential[0,coin_balances.index(value)] = e
    for value in coin_balances_btc_equiv:
        e = Entry(Balances, foreground = 'black', background = 'white')
        e.grid(row=coin_balances_btc_equiv.index(value)+1, column=3, stick='nesw')
        e.insert(0, value)
        e.config(justify=CENTER, state=DISABLED)
        e.columnconfigure(0, weight=2)
        referential[0,coin_balances_btc_equiv.index(value)] = e
    for _ in range(len(coin_actions)):
        e = Entry(Balances, foreground = 'black', background = 'white')
        e.grid(row=_+1, column=4, stick='nesw')
        e.insert(0, 'Deposit Withdraw')
        e.config(justify=CENTER, state=DISABLED)
        e.columnconfigure(0, weight=2)
        
##    e = ttk.Entry(Balances)
##    e.grid(row=row, column=column, stick="nsew")
##    referential[index] = e

    ##Game tab
    tab5 = ttk.Frame(notebook)
    notebook.add(tab5, text = 'Games')

    ttk.Button(tab5, text = 'Play Brick Breaker!', command= Games.Brick_Breaker,).pack()
    ttk.Button(tab5, text = 'Play Bullets!', command= Games.Bullets,).pack()
    ttk.Button(tab5, text = 'Play Space Cooties Must Die!', command= Games.SCMD,).pack()
    
    #add new tab ## non-functional
    tabnew = ttk.Frame(notebook)
    notebook.add(tabnew, text = '+')

        
    ##    progressbar.config(mode = 'indeterminate')
    ##    progressbar.start()
    ##    progressbar.stop()

    ##    progressbar.config(mode = 'determinate', maximum = 11.0, value = 4.2)
    ##    progressbar.config(value = 8.0)
    ##    progressbar.step()
    ##    progressbar.step(5)
    ##
    ##    value = DoubleVar()
    ##    progressbar.config(variable = value)
    ##
    ##    scale = ttk.Scale(frame2, orient = HORIZONTAL,
    ##                      length = 400, variable = value,
    ##                      from_ = 0.0, to = 11.0)
    ##    scale.pack()

    ##frame3 = ttk.Frame(panedwindow, width = 50, height = 50, relief = SUNKE
    ##panedwindow.insert(1, frame3)
    ##panedwindow.forget(1)

    ##frame = ttk.Frame(root)
    ##frame.pack()
    ##frame.config(height = 100, width = 200)
    ##frame.config(relief = RIDGE)
    ##ttk.Button(frame, text = 'Click Me').pack()
    ##frame.config(padding = (30, 15))
    ##ttk.LabelFrame(root, height = 100, width = 200, text = 'My Frame').pack()

##    task_input_frame = ttk.Frame(frame1)
##    task_input_frame.pack(fill = X)
##    #Welcome = ttk.Label(Welcomeframe, image = headTexture)
##    task_input_Label = ttk.Label(task_input_frame, text = 'Enter a task')
##    task_input_Label.pack(fill = X, expand = True)


    #e.get()
    #e.delete(0, 1)
    #e.delete(0, END)
    #e.insert(0, 'Enter your task...')

    #e.config(show = '*')
    #e.state(['disabled'])
    #e.state(['readonly'])
    #e.state(['!disabled'])

    root.iconbitmap('mw_icon.ico')
    root.mainloop()

if __name__ == "__main__": main()

   

