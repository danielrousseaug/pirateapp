import tkinter as tk
from webscrapper import search
import webbrowser

COLOR = "#ffa200"

def query(var):
    newVar = search(var)
    label['text'] = newVar[0]

def linkopen(var, num):
    new = 1
    url = search(var)[1][num]
    webbrowser.open(url,new=new)

# innit tkinter
root = tk.Tk()
root.attributes('-alpha', 0.85)

# bckg color
color = tk.Label(root, background='#000000')
color.place(x=0,y=0,relwidth=1,relheight=1)

# set icon and name
root.iconbitmap("pirateicon.ico")
root.title('Pirate App')

# set size
canvas =  tk.Canvas(root, height="770", width="740", background="#000000",bd="0")
canvas.pack()


# frame
frame = tk.Frame(root, bg='#000000', bd=0, highlightthickness=0 )
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# buttonframe
buttonframe = tk.Frame(frame, bg="#000000", bd=10, highlightthickness=1,highlightcolor=COLOR,highlightbackground=COLOR )
buttonframe.place(relheight=0.5, relwidth=0.5, relx=0.25)

# button in frame
button = tk.Button(buttonframe, highlightthickness=1, highlightcolor=COLOR,highlightbackground=COLOR,cursor="dot", text="Search the Seven Seas", activebackground="#000000", activeforeground="#000000", bg="#000000", bd="0", fg=COLOR, command=lambda: query(entry.get() ))
button.place(relheight=1, relwidth=1, relx=0)

# entry
entry_label = tk.Label(frame,font=30,highlightthickness=0, bd=0, bg="#FFFFFF", fg="#FFFFFF")
entry_label.place(relwidth=0.5, relheight=0.3, rely=0.6, relx=0.25)

# entryframe
entryframe = tk.Frame(entry_label, bg="#000000", bd=1, highlightthickness=1,highlightcolor=COLOR,highlightbackground=COLOR )
entryframe.place(relwidth=1, relheight=1, rely=0, relx=0)

entry = tk.Entry(entryframe, font=40, bd='0', bg="#000000", fg="#FFFFFF")
entry.place(relheight=1, relwidth=1, relx=0)

# lower frame
lower_frame = tk.Frame(root, bg="#000000", bd=10, highlightthickness=1,highlightcolor=COLOR,highlightbackground=COLOR)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

# midle label
label = tk.Label(lower_frame, bg="#000000", justify='left', bd='0', anchor="nw", fg="#FFFFFF")
label.place(relwidth=1, relheight=1)

# download buttons
button1frame = tk.Frame(root, bg="#000000", bd=0, highlightthickness=1,highlightcolor=COLOR,highlightbackground=COLOR )
button1frame.place(relheight=0.12, relwidth=0.125, relx=0.875, rely=0.25)

button1 = tk.Button(button1frame,  highlightthickness=1,highlightcolor=COLOR,highlightbackground=COLOR, cursor="dot", text="Download 1", activebackground=COLOR, background="#000000",foreground=COLOR, bd="0", command=lambda: linkopen(entry.get(), 0) )
button1.place(relheight=1, relwidth=1, relx=0)

button2frame = tk.Frame(root, bg="#000000", bd=0, highlightthickness=1,highlightcolor=COLOR,highlightbackground=COLOR )
button2frame.place(relheight=0.12, relwidth=0.125, relx=0.875, rely=0.37)

button2 = tk.Button(button2frame,  highlightthickness=1,highlightcolor=COLOR,highlightbackground=COLOR, cursor="dot", text="Download 2", activebackground=COLOR, background="#000000",foreground=COLOR, bd="0", command=lambda: linkopen(entry.get(), 1) )
button2.place(relheight=1, relwidth=1, relx=0)

button3frame = tk.Frame(root, bg="#000000", bd=0, highlightthickness=1,highlightcolor=COLOR,highlightbackground=COLOR )
button3frame.place(relheight=0.12, relwidth=0.125, relx=0.875, rely=0.49)

button3 = tk.Button(button3frame,  highlightthickness=1,highlightcolor=COLOR,highlightbackground=COLOR, cursor="dot", text="Download 3", activebackground=COLOR, background="#000000",foreground=COLOR, bd="0", command=lambda: linkopen(entry.get(), 2) )
button3.place(relheight=1, relwidth=1, relx=0)

button4frame = tk.Frame(root, bg="#000000", bd=0, highlightthickness=1,highlightcolor=COLOR,highlightbackground=COLOR )
button4frame.place(relheight=0.12, relwidth=0.125, relx=0.875, rely=0.61)

button4 = tk.Button(button4frame,  highlightthickness=1,highlightcolor=COLOR,highlightbackground=COLOR, cursor="dot", text="Download 4", activebackground=COLOR, background="#000000",foreground=COLOR, bd="0", command=lambda: linkopen(entry.get(), 3) )
button4.place(relheight=1, relwidth=1, relx=0)

button5frame = tk.Frame(root, bg="#000000", bd=0, highlightthickness=1,highlightcolor=COLOR,highlightbackground=COLOR )
button5frame.place(relheight=0.12, relwidth=0.125, relx=0.875, rely=0.73)

button5 = tk.Button(button5frame,  highlightthickness=1,highlightcolor=COLOR,highlightbackground=COLOR, cursor="dot", text="Download 5", activebackground=COLOR, background="#000000",foreground=COLOR, bd="0", command=lambda: linkopen(entry.get(), 4) )
button5.place(relheight=1, relwidth=1, relx=0)


root.mainloop()