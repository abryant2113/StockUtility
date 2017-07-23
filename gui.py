import tkinter as tk
from stock_utility import Request
from tkinter import *
from tkinter import ttk


def my_info():
    my_obj = Request()
    my_obj.set_name(company_name.get())
    pps.set(my_obj.price)
    lb.insert(END, my_obj.name + "   " + my_obj.price)

# handles the enter keystroke event
def event_handler(event):
    my_info()

# tkinter gui
root = Tk()
root.geometry("375x300")
root.title("StockUtility V1.0")
root.resizable(width=False, height=False)

mainframe = tk.Frame(width=500, height=500)
mainframe.grid(sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

company_name = StringVar()
pps = StringVar()

img = PhotoImage(file="stock.png")
panel = tk.Label(mainframe, image=img)
panel.grid(row=0, sticky=NSEW)

tk.Label(mainframe, text="Company").grid(row=1, column=0, sticky=N + S + W)
tk.Label(mainframe, text="Price").grid(row=2, column=0, sticky=N + S + W)

company_entry = ttk.Entry(mainframe, width=8, textvariable=company_name)
company_entry.grid(row=1, column=0, sticky=N + S + E)
company_entry.focus()

tk.Label(mainframe, textvariable=pps).grid(row=2, column=0, sticky=N + S + E)
tk.Button(mainframe, text="Search", command=lambda: my_info()).grid(row=4, sticky=NSEW)

# stores the contents from the portfolio file in a set for listbox access
#lit = stock_utility.Utility.read_file_contents
#list = {}

# creates the listbox that will contains our current portfolio data
lb = Listbox(mainframe, height=5, width=50)
lb.grid(row=5, column=0, sticky=NSEW)

# adds all of our recent searches from the "portfolio.txt" file into our listbox.
#for s in lit:
 #   lb.insert(END, str(s))

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.bind('<Return>', lambda: event_handler())

root.mainloop()


