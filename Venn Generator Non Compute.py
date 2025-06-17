#imports
import random
import time
import tkinter as tk
import re
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox
from matplotlib_venn import venn2
from matplotlib_venn import venn3

# File settings
__author__ = "James Pink-Gyett"
__copyright__ = "Copyright 2025, James Pink-Gyett"
root = tk.Tk()
bgcolour = "#808080"
hlcolour = "#595959"
root.title("Venn Diagram Generator")
root.geometry("600x500")
root.configure(bg=bgcolour)
root.resizable(False, False)
setsVar = tk.IntVar()

#Title
titleframe = tk.Frame(root, bg=bgcolour)
titleframe.pack(pady=10)
title = tk.Label(titleframe, text="Venn Diagram Generator", bg=bgcolour, font=("bold", 20))
title.pack()

disclaimer = tk.Label(titleframe, text="Non compute version. (Only for visualising your calculations.)", bg=bgcolour)
disclaimer.pack()

#Slider
sliderlabel = tk.Label(titleframe, text="Number of sets", bg=bgcolour)
sliderlabel.pack(pady=10)
def on_slider_change(value):
    value = int(value)

    if value == 3:
        if not hasattr(root, "set3_widgets"):
            set3label = tk.Label(setsframe, text="Set 3", bg=bgcolour)
            set3label.grid(row=1, column=2, padx=5, pady=1)

            set3entry = tk.Entry(setsframe, width=20, validate="key", validatecommand=vcmd)
            set3entry.grid(row=2, column=2, padx=5, pady=1)

            set3namelabel = tk.Label(setsframe, text="Name (Optional)", bg=bgcolour)
            set3namelabel.grid(row=3, column=2, padx=10, pady=3)
            
            set3nameentry = tk.Entry(setsframe, width=20)
            set3nameentry.grid(row=4, column=2, padx=10, pady=3)

            root.set3_widgets = [set3label, set3entry, set3namelabel, set3nameentry]
    else:
        if hasattr(root, "set3_widgets"):
            for widget in root.set3_widgets:
                widget.destroy()
            del root.set3_widgets
lengthslider = tk.Scale(titleframe, bg=bgcolour, highlightthickness="0", length="50", from_=2, to=3, orient=tk.HORIZONTAL, variable=setsVar, command=on_slider_change)
lengthslider.pack()

#Input validation functions
def validate_input_commas(new_value):
    if new_value == "":
        return True
    pattern = r'^\d*(,\d*)*$'
    return re.fullmatch(pattern, new_value) is not None

def validate_input_numbers(new_value):
    if new_value == "":
        return True
    pattern = r'^\d+$'
    return re.fullmatch(pattern, new_value) is not None

vcmd = (root.register(validate_input_commas), '%P')
vcmd2 = (root.register(validate_input_numbers), '%P')

#Sets configuration
setsframe = tk.Frame(root, bg=bgcolour)
setsframe.pack(pady=10)

setslabel = tk.Label(setsframe, text="Enter the sets below\ne.g. 1,2,3,4", bg=bgcolour)
setslabel.grid(row=0, columnspan=3, padx=10, pady=1)

set1label = tk.Label(setsframe, text="Set 1", bg=bgcolour)
set1label.grid(row=1, column=0, padx=10, pady=5)
set1entry = tk.Entry(setsframe, width=20, validate="key", validatecommand=vcmd)
set1entry.grid(row=2, column=0, padx=10, pady=3)
set1namelabel = tk.Label(setsframe, text="Name (Optional)", bg=bgcolour)
set1namelabel.grid(row=3, column=0, padx=10, pady=3)
set1nameentry = tk.Entry(setsframe, width=20)
set1nameentry.grid(row=4, column=0, padx=10, pady=3)

set2label = tk.Label(setsframe, text="Set 2", bg=bgcolour)
set2label.grid(row=1, column=1, padx=10, pady=5)
set2entry = tk.Entry(setsframe, width=20, validate="key", validatecommand=vcmd)
set2entry.grid(row=2, column=1, padx=10, pady=3)
set2namelabel = tk.Label(setsframe, text="Name (Optional)", bg=bgcolour)
set2namelabel.grid(row=3, column=1, padx=10, pady=3)
set2nameentry = tk.Entry(setsframe, width=20)
set2nameentry.grid(row=4, column=1, padx=10, pady=3)

#Total and name configuration
settotalframe = tk.Frame(root, bg=bgcolour)
settotalframe.pack(pady=10)

settotallabel = tk.Label(settotalframe, text="Total value\n(Outside Venn diagram)", bg=bgcolour)
settotallabel.grid(row=1, column=0, pady=5, padx=10)
settotalentry = tk.Entry(settotalframe, width=20, validate="key", validatecommand=vcmd2)
settotalentry.grid(row=2, column=0, pady=5, padx=10)

namelabel = tk.Label(settotalframe, text="Name of Venn diagram\n(Optional)", bg=bgcolour)
namelabel.grid(row=1, column=1, pady=5, padx=10)
nameentry = tk.Entry(settotalframe, width=20)
nameentry.grid(row=2, column=1, pady=5, padx=10)

#End / generate
endtitleframe = tk.Frame(root, bg=bgcolour)
endtitleframe.pack(pady=5)

def generate_venn():
    set1_raw = set1entry.get()
    set2_raw = set2entry.get()
    set3_raw = None
    totaloutside = settotalentry.get()
    set1name = set1nameentry.get()
    set2name = set2nameentry.get()
    set3name = None
    pattern = r'^(\d+,)*\d+$'

    if hasattr(root, "set3_widgets"):
        set3_raw = root.set3_widgets[1].get()
        set3name = root.set3_widgets[3].get()

    if re.fullmatch(pattern, set1_raw) and re.fullmatch(pattern, set2_raw) and (set3_raw is None or re.fullmatch(pattern, set3_raw)):
        set1 = set(map(int, set1_raw.split(',')))
        set2 = set(map(int, set2_raw.split(',')))

        #3 Sets
        if set3_raw:
            set3 = set(map(int, set3_raw.split(',')))
            venn = venn3([set1, set2, set3], (set1name, set2name, set3name))

            regions = {
                '100': set1 - set2 - set3, #A only
                '010': set2 - set1 - set3, #B only
                '001': set3 - set1 - set2, #C only
                '110': (set1 & set2) - set3, #A ∩ B
                '101': (set1 & set3) - set2, #A ∩ C
                '011': (set2 & set3) - set1, #B ∩ C
                '111': set1 & set2 & set3, #A ∩ B ∩ C
            }
            for region, values in regions.items():
                label = venn.get_label_by_id(region)
                if label:
                    label.set_text(','.join(map(str, values)) if values else '')
            plt.title(nameentry.get())
        
        #2 Sets
        else:
            venn = venn2([set1, set2], (set1name, set2name))

            venn.get_label_by_id('10').set_text(','.join(map(str, set1 - set2))) #A only
            venn.get_label_by_id('01').set_text(','.join(map(str, set2 - set1))) #B only
            
            if venn.get_label_by_id('11'):
                venn.get_label_by_id('11').set_text(','.join(map(str, set1 & set2))) #A ∩ B

            plt.title(nameentry.get())
        plt.text(0, -0.8, f"Outside: {totaloutside}", ha='center', fontsize=10)
        plt.show()
    else:
        messagebox.showerror("Invalid Input", "Please enter only numbers separated by commas.\nNo trailing commas or empty elements.")

submitBtn = tk.Button(root, text="Generate Venn Diagram", bg=bgcolour, height=2, width=30, font=("bold", 10), command=generate_venn)
submitBtn.pack(pady=10)

root.mainloop()