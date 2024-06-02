import random,sys
import tkinter
from tkinter import IntVar, Tk, Checkbutton

win = Tk()
Top = tkinter.Toplevel(win)
width,height=220,675

def center_window(width, height):
    # get screen width and height
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    # calculate position x and y coordinates
    x = round((screen_width/2) - (width/2))
    y = round((screen_height/2) - (height/2))
    win.geometry(f'{width}x{height}+{x}+{y}')
    Top.geometry(f'{width}x{height}+{x}+{y}')
    
center_window(width,height)
win.title("Hitman, World of Assassination")
if sys.platform == 'win32':
    win.attributes("-toolwindow",0)
win.attributes("-alpha",0.0)
title_bar = tkinter.Frame(Top, bg='black', relief='raised', bd=2,highlightthickness=0,height=50)
title_name = tkinter.Label(title_bar, text='World Of Assassination', fg='grey',bg='black')
title_name.pack(side='left',expand=1, fill='both')
close_button = tkinter.Button(title_bar, text='X', command= win.destroy,bg = "red",padx = 1,pady = 1,activebackground='red',bd = 0,font="bold",fg='white',highlightthickness=0)
window = tkinter.Canvas(Top, bg='#2e2e2e',highlightthickness=0)
title_bar.pack(expand=0, fill='x')
close_button.pack(side='right')
#window.pack(expand=True, fill='both')
frame = tkinter.Frame(Top,bg='black')
frame.pack(side='top', anchor='w')
def start_move(event):
    global lastx, lasty
    lastx = event.x_root
    lasty = event.y_root
def move_window(event):
    global lastx, lasty
    deltax = event.x_root - lastx
    deltay = event.y_root - lasty
    x = Top.winfo_x() + deltax
    y = Top.winfo_y() + deltay
    Top.geometry("+%s+%s" % (x, y))
    lastx = event.x_root
    lasty = event.y_root

def change_on_hovering(event):
    global close_button
    close_button['bg']='red'
def return_to_normalstate(event):
    global close_button
    close_button['bg']='#2e2e2e'

def onRootIconify(event): 
    Top.withdraw()
win.bind("<Unmap>", onRootIconify)
def onRootDeiconify(event): 
    Top.deiconify()
win.bind("<Map>", onRootDeiconify)

title_name.bind("<ButtonPress-1>", start_move)
title_name.bind('<B1-Motion>', move_window)
close_button.bind('<Enter>',change_on_hovering)
close_button.bind('<Leave>',return_to_normalstate)

Top.lower()
Top.attributes("-topmost",0)
Top.overrideredirect(True)

class buttons:
    def __init__(self):
        self.cities = [ 
    'Paris 🇫🇷',
    'Sapienza 🇮🇹',
    'Marrakesh 🇲🇦',
    'Bangkok 🇹🇭',
    'Colorado 🇺🇸',
    'Hokkaido 🇯🇵',
    'Hawke\'s Bay 🇳🇿',
    'Miami 🇺🇸',
    'Santa Fortuna 🇨🇴',
    'Whittleton Creek 🇺🇸',
    'Mumbai 🇮🇳',
    'Isle of Sgàil 🏴󠁧󠁢󠁳󠁣󠁴󠁿',
    'New York 🇺🇸',
    'Haven Island 🇲🇻',
    'Dubai 🇦🇪',
    'Dartmoor 🏴󠁧󠁢󠁥󠁮󠁧󠁿',
    'Berlin 🇩🇪',
    'Chongqing 🇨🇳',
    'Mendoza 🇦🇷',
    'Ambrose Island 🇮🇳'
	]
        self.varint = dict()
    def citylist(self):
        for city in self.cities:
            self.varint[city] = IntVar()
            city = Checkbutton(frame, text=city, variable=self.varint[city],bg='black', fg='grey').pack(side='top',anchor='w')
        self.Result = tkinter.Label(Top,text='',font=('1942 report', 13),bg='black',fg='light grey') #'#f00ba3
        self.Result.pack(expand=True)
        Top.config(bg='black')
        copyframe = tkinter.Frame(Top, bg='black')
        copyframe.pack(side='bottom', anchor='s')
        okbutton = tkinter.Button(copyframe,text='OK',command=lambda: self.test(),bg='black',fg='grey')
        
        copyright = tkinter.Label(copyframe,text="Dofain@2024", font=('Helvetica', 7), bg='black', fg='dark grey').pack(side='bottom', anchor='s', fill='both', pady=2)
        okbutton.pack(side='bottom',anchor='s', before=copyright, fill='both')
    def test(self):
        choices = []
        greet = ['Congratulation 47,','Have a safe trip,','You know\nthe drill 47,','I\'ll let you\nhandle this 47,','Safe Journey 47,','Time to\nvisit someone 47,']
        try:
            for city in self.varint.keys():
                if self.varint[city].get():
                    choices.append(city)
            gothere = f'{random.choice(greet)}\nYour next stop:\n {random.choice(choices)}'
        except IndexError:
            gothere = f'Don\'t be a fool 47,\nyou know you have\nto go somewhere...'
        self.Result.config(text=gothere)

def main():
    buttons().citylist()
    Top.mainloop()

if __name__ == "__main__":
    main()