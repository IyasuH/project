import tkinter as tk
from tkinter import ttk, Menu, Label, CENTER
from tkinter import messagebox as msg
import command
import pandas as pd

import os
import json

class App(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.winfo_toplevel().title("Project Scrapy")

        nameL = Label(self, text="Select Material").grid(column=0, row=0)
        websiteL = Label(self, text="Select Website").grid(column=1, row=0)

        self.material = tk.StringVar()
        material_chooseCombo = ttk.Combobox(self, width=10, textvariable=self.material)
        material_chooseCombo["values"] = ("All Materials", "Cements", "Paints", "Bricks", "Tiles")
        material_chooseCombo.grid(column=0, row=1)
        material_chooseCombo.current(0)

        self.source_website = tk.StringVar()
        source_website_chooseCombo = ttk.Combobox(self, width=10, textvariable=self.source_website)
        source_website_chooseCombo["values"] = ("Jiji")
        source_website_chooseCombo.grid(column=1, row=1)
        source_website_chooseCombo.current(0)

        scrape_button=ttk.Button(self, text="Scrape", command=self.scrape_func)
        scrape_button.grid(column=2, row=1)

        self.scrape_result_tbl = ttk.Treeview(self, column=("c1", "c2", "c3", "c4"), show='headings', height=10)
        self.scrape_result_tbl.column("# 1", anchor=CENTER)
        self.scrape_result_tbl.heading("# 1", text="Item")
        self.scrape_result_tbl.column("# 2", anchor=CENTER)
        self.scrape_result_tbl.heading("# 2", text="Price(in ETB)")
        self.scrape_result_tbl.column("# 3", anchor=CENTER)
        self.scrape_result_tbl.heading("# 3", text="Description")
        self.scrape_result_tbl.column("# 4", anchor=CENTER)
        self.scrape_result_tbl.heading("# 4", text="Location")
        self.scrape_result_tbl.grid(column=0, row=2, columnspan=4)

        genrate_csv_button = ttk.Button(self, text="Generate CSV", command=self.generate_csv_func)
        genrate_csv_button.grid(column=2, row=3)

    def generate_csv_func(self):
        """
        to generate CSV file
        """
        selected_material = self.material.get()
        json_file = selected_material.replace(" ", "_").lower()+".json"
        # since csv file going to genrate from json file first lets chek upon json file
        if not os.path.exists(json_file):
            error_msg_win = tk.Tk()
            error_msg_win.overrideredirect(1)
            error_msg_win.withdraw()
            msg.showerror("Project Scrapy", message="JSON file does not exists first genrate that")
        df = pd.read_json(r'{}'.format(json_file))
        df.to_csv(r'{}.csv'.format(json_file.replace(".json", "")), index=None)
        if os.path.exists(json_file.replace(".json", "")+".csv"):
            success_msg_win = tk.Tk()
            success_msg_win.overrideredirect(1)
            success_msg_win.withdraw()
            msg.showinfo(title="Project Scrapy", message="CSV file created succesfully check you root diretory")
        else:
            error_msg_win = tk.Tk()
            error_msg_win.overrideredirect(1)
            error_msg_win.withdraw()
            msg.showerror(title="Project Scrapy", message="Something wrong happend")

    def clear_scrape_tbl(self):
        """
        clear every element of the table
        """
        for item in self.scrape_result_tbl.get_children():
            self.scrape_result_tbl.delete(item)

    def scrape_func(self):
        selected_material = self.material.get()
        print("Selected Material: ", selected_material)
        # rule for JSON files naming that they should not conatin space instaed (_) and cpital letters
        # so my input is selected_material I have to edit that according to json file naming
        json_file = selected_material.replace(" ", "_").lower()+".json"
        # since going to update it firts lets delete it
        if os.path.exists(json_file):
            command.run(['rm', json_file])

        # spider name is smiliar to json name
        spider_name=json_file.replace(".json", "")
        command.run(["scrapy","crawl", "{}".format(spider_name), "-o", "{}".format(json_file)])
        scraped_file = open(json_file)
        scraped_data = json.load(scraped_file)
        # print("scraped_data: ", scraped_data)
        # before inserting items to table first lets clear it
        self.clear_scrape_tbl()
        # then insert
        for data in scraped_data:
            self.scrape_result_tbl.insert('', 'end', values=(data["title"].replace("\n", ""), data["price"].replace("\n", "").replace("ETB", ""), data["desc"].replace("\n", ""), data["location"]))

def main():
    root = tk.Tk()
    root.resizable(True, True)
    # for creating Menu on top
    menu_bar=Menu(root)
    root.config(menu=menu_bar)
    # adding sub_menu called help_menu which going to include About and Help
    help_menu = Menu(menu_bar, tearoff=0)
    help_menu.add_command(label="About", command=about_page)
    help_menu.add_command(label="Help", command=help_page)
    menu_bar.add_cascade(label="Help", menu=help_menu)

    con = App(root)
    # con.pack(expand=1, fill="both")
    con.grid(column=0, row=0)
    root.mainloop()

def about_page():
    """
    PopUP about page
    """
    about=tk.Tk()
    about.title("About")
    about.geometry("400x200")
    about.resizable(False, False)
    desc = Label(about, text="This project is ...blah blah blah")
    exit_button = ttk.Button(about, text="Exit", command=about.destroy)
    desc.pack()
    exit_button.pack()

def help_page():
    """
    PopUP about page
    """
    help=tk.Tk()
    help.title("Help")
    help.geometry("400x200")
    help.resizable(False, False)
    desc = Label(help, text="This is Help text")
    exit_button = ttk.Button(help, text="Exit", command=help.destroy)
    desc.pack()
    exit_button.pack()


if __name__ == "__main__":
    main()
