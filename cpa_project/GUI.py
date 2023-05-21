import tkinter as tk
from tkinter import ttk, Entry, CENTER
import time

win = tk.Tk()

win.title("Scrapy")
win.geometry("400x250")

s = ttk.Style()
s.theme_use('clam')

ttk.Label(win, text="Material Name").grid(column=0, row=0)

# here combobox to choose the material to be scraped
material = tk.StringVar()
material_choose = ttk.Combobox(win, width=10, textvariable=material)
material_choose["values"] = ("All Materials", "Cement")
material_choose.grid(column=0, row=1)
material_choose.current(0)


# scarpe_lst = [["Item", "Price", "Desc", "Loc"]]
scarpe_lst =[]

def scrape_func():
    """
    function that scarpes choosen material and update the list
    """
    # function
    material_ = material.get()
    print("choose material: ", material_)
    # change the scarpe lst values
    scarpe_lst.clear()
    scarpe_lst.append(["Dangote ppc", "1500", "C-25 PPC ", "Addis"])
    # Table(win)
    gen_table()
    time.sleep(1)

scarpe_action = ttk.Button(win, text="Scrape", command=scrape_func)
scarpe_action.grid(column=1, row=1)

tree = ttk.Treeview(win, column=("c1", "c2", "c3", "c4"), show='headings', height=5)
tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="Item")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Price")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="Desc")
tree.column("# 4", anchor=CENTER)
tree.heading("# 4", text="Locat")


def gen_table():
    """
    Genrates Entry matrix which actually looks like a table
    """

    print("scarpe_list: ", scarpe_lst)
    # Insert the data in Treeview widget
    tree.delete('')
    for i in range(len(scarpe_lst)):
        tree.insert('','end', values=(scarpe_lst[i][0], scarpe_lst[i][1], scarpe_lst[i][2], scarpe_lst[i][3]))
    tree.grid(column=0, row=2, columnspan=4)
    # for i in range(len(scarpe_lst)):
    #     # total_columns to be 4(name, price, desc, location)
    #     for j in range(len(scarpe_lst[0])):
    #         e =Entry(win, width=30, fg="blue", font=('Arial', 12, 'bold'))
    #         e.grid(column=j, row=i+2, columnspan=3)
    #         e.insert(tk.END, scarpe_lst[i][j])
    

# t=Table(win)
win.mainloop()