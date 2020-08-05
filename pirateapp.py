import tkinter as tk
from webscrapper import search
import webbrowser

def query(var):
    newVar = search(var)
    label['text'] = newVar[0]

def linkopen(var, num):
    new = 1
    url = search(var)[1][num]
    webbrowser.open(url,new=new)

# innit tkinter
root = tk.Tk()

# set icon and name
root.iconbitmap("pirateicon.ico")
root.title('Pirate App')

# set size
canvas =  tk.Canvas(root, height="770", width="740")
canvas.pack()

background_image = tk.PhotoImage(file='backdrop.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


# frame
frame = tk.Frame(root, bg='#000000', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# button in frame
button = tk.Button(frame, cursor="dot", text="Search the seven seas", activebackground="#FFFFFF", activeforeground="#FFFFFF", bg="#fca311", bd="0", fg="#FFFFFF", command=lambda: query(entry.get() ))
button.place(relheight=0.5, relwidth=0.3, relx=0.35)

# entry
entry_label = tk.Label(frame, font=40, bd='1', bg="#FFFFFF", fg="#FFFFFF")
entry_label.place(relwidth=0.5, relheight=0.3, rely=0.6, relx=0.25)

entry = tk.Entry(entry_label, font=40, bd='1', bg="#000000", fg="#FFFFFF")
entry.place(relwidth=1, relheight=1, rely=0, relx=0)

# lower frame
lower_frame = tk.Frame(root, bg="#000000", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

# midle label
label = tk.Label(lower_frame, bg="#000000", justify='left', bd='0', anchor="nw", fg="#FFFFFF")
label.place(relwidth=1, relheight=1)

# download buttons
button1 = tk.Button(root, cursor="dot", text="Download 1", activebackground="#FFFFFF", background="#000000",foreground="#FFFFFF", bd="0", command=lambda: linkopen(entry.get(), 1) )
button1.place(relheight=0.1, relwidth=0.125, relx=0.875, rely=0.25)

button2 = tk.Button(root, cursor="dot", text="Download 2", activebackground="#FFFFFF", background="#000000",foreground="#FFFFFF", bd="0", command=lambda: linkopen(entry.get(), 2))
button2.place(relheight=0.1, relwidth=0.125, relx=0.875, rely=0.35)

button3 = tk.Button(root, cursor="dot", text="Download 3", activebackground="#FFFFFF", background="#000000",foreground="#FFFFFF", bd="0", command=lambda: linkopen(entry.get(), 3))
button3.place(relheight=0.1, relwidth=0.125, relx=0.875, rely=0.45)

button4 = tk.Button(root, cursor="dot", text="Download 4", activebackground="#FFFFFF", background="#000000",foreground="#FFFFFF", bd="0", command=lambda: linkopen(entry.get(), 4))
button4.place(relheight=0.1, relwidth=0.125, relx=0.875, rely=0.55)

button4 = tk.Button(root, cursor="dot", text="Download 5", activebackground="#FFFFFF", background="#000000",foreground="#FFFFFF", bd="0", command=lambda: linkopen(entry.get(), 5))
button4.place(relheight=0.1, relwidth=0.125, relx=0.875, rely=0.65)


root.mainloop()