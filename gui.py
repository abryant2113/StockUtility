import tkinter as tk
import time
from stock_utility import Request
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


# method that will continue periodically sending updates regarding changes in the stock price
def my_info():
    tk.messagebox.askokcancel(title="Loop now running", message="The script will now send you periodic price updates.")
    root.destroy()
    comp = company_name.get()
    request_obj = Request(comp)

    # sleep timer is set to 300 seconds by default, but can be adjusted to fit your needs.
    while True:
        request_obj.grab_info()
        time.sleep(300)


# handles the enter keystroke event
def event_handler(event):
    my_info()

# tkinter gui
root = Tk()
root.geometry("375x180")
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

company_entry = ttk.Entry(mainframe, width=48, textvariable=company_name)
company_entry.grid(row=1, column=0, sticky=N + S + E)
company_entry.focus()

tk.Button(mainframe, text="Search", command=lambda: my_info()).grid(row=4, sticky=NSEW)

# packs in all of the widgets
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# allows the user to hit the return key instead of clicking the search button
root.bind('<Return>', event_handler)
root.mainloop()


