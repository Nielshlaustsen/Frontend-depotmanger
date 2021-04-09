import tkinter as tk
from tkinter import *
from tkinter import messagebox

root=Tk()
#def
def click():
    entered_text=textentry.get() #samler teksten fra knappen
    output.delete(0.0, END)
    try:
        password = kodeord[entered_text]
    except:
        password = "Kodeordet er forkert"
        tk.messagebox.showerror("Kodeordet er forkert", "Det indtastede kodeord er forkert")
    output.insert(END, password)

def show_vindue1():
    vindue2.grid_forget()
    vindue1.grid()

def show_vindue2():
    vindue1.grid_forget()
    vindue2.grid()

#main:
# window = Tk()
# window.title("Depot htx hjørring: forside")
# window.configure(background="white")

#Show window:
kodeord = {'andl':'Kodeordet er godkendt','niels':'Kodeordet er godkendt','jakob':'Drengen er eftersøgt'}

#create label:
vindue1 = Frame(root)
Label(vindue1, text="Skriv dit kodeord:", bg="white", fg="black", font="none 12 bold").grid(row=1,column=2, sticky=N)

#Text entry:
textentry = Entry(vindue1, width=30, bg="white")
textentry.grid(row=2, column=2, sticky=N)

def check_pass():
    if textentry.get() in list(kodeord):
        show_vindue2()
    else:
    #Button:
        tk.messagebox.showerror("Kodeordet er forkert", "Det indtastede kodeord er forkert")

Button(vindue1, text="FORTSÆT", width = 6, command=check_pass).grid(row=3, column=2, sticky=N)


#ny label:
Label(vindue1, text="\nStatus på kodeord:", bg="white", fg="black", font="none 12 bold").grid(row=4, column=2, sticky=W)

#text boks:
output = Text(vindue1, width=30, height=1, wrap=WORD, background="white")
output.grid(row=5, column=2, columnspan=1, sticky=W)
def close_window():
    window.destroy()
    exit()

#exit label:
Button(vindue1, text="Forlad", width = 7, command=close_window).grid(row=8,column=2, sticky=N)
def close_window():
    window.destroy()
    exit()

vindue2 = Frame(root)
Label(vindue2, text="Dette er vindue 2", bg="white", fg="black", font="none 12 bold").grid(row=1,column=2, sticky=N)
Button(vindue2, text="Gå tilbage til første vindue", command=show_vindue1).grid(row=3, column=2, sticky=N)

vindue1.grid()


#Label.pack()
root.mainloop()

#######SCAN_VARER#######
scan = Tk()
scan.title("Depot htx hjørring: scan")
scan.configure(background="white")
