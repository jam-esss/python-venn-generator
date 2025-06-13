#imports
import random
import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from matplotlib import pyplot as plt
from matplotlib_venn import venn2

# File settings
__author__ = "James Pink-Gyett"
__copyright__ = "Copyright 2025, James Pink-Gyett"
root = tk.Tk()
bgcolour = "#808080"
hlcolour = "#595959"
root.title("Venn Diagram Generator")
root.geometry("600x400")
root.configure(bg=bgcolour)
root.resizable(False, False)

#

setsVar = tk.IntVar()

titleframe = tk.Frame(root, bg=bgcolour)
titleframe.pack(pady=1)

title = tk.Label(titleframe, text="Venn Diagram Generator", bg=bgcolour, font=("bold", 20))
title.pack()
sliderlabel = tk.Label(titleframe, text="How many sets (circles)?", bg=bgcolour)
sliderlabel.pack()
# Slider function is below

def on_slider_change(value):
    value = int(value)

    # If slider is 3, show widgets
    if value == 3:
        if not hasattr(root, "set3_widgets"):
            # Create and store widgets
            set3label = tk.Label(setsframe, text="Set 3", bg=bgcolour)
            set3label.grid(row=1, column=2, padx=5, pady=1)

            set3entry = tk.Entry(setsframe, width=20)
            set3entry.grid(row=2, column=2, padx=5, pady=1)

            # Store references
            root.set3_widgets = [set3label, set3entry]
    else:
        # If slider is not 3, remove the widgets
        if hasattr(root, "set3_widgets"):
            for widget in root.set3_widgets:
                widget.destroy()
            del root.set3_widgets

lengthslider = tk.Scale(titleframe, bg=bgcolour, highlightthickness="0", length="50", from_=2, to=3, orient=tk.HORIZONTAL, variable=setsVar, command=on_slider_change)
lengthslider.pack(pady=5)
#
setsframe = tk.Frame(root, bg=bgcolour)
setsframe.pack(pady=10)

setslabel = tk.Label(setsframe, text="Enter the sets below seperated by a comma (e.g: 1,2,3,4):", bg=bgcolour)
setslabel.grid(row=0, columnspan=3, padx=5, pady=1)

set1label = tk.Label(setsframe, text="Set 1", bg=bgcolour)
set1label.grid(row=1, column=0, padx=5, pady=1)
set1entry = tk.Entry(setsframe, width=20)
set1entry.grid(row=2, column=0, padx=5, pady=1)

set2label = tk.Label(setsframe, text="Set 2", bg=bgcolour)
set2label.grid(row=1, column=1, padx=5, pady=1)
set2entry = tk.Entry(setsframe, width=20)
set2entry.grid(row=2, column=1, padx=5, pady=1)
#
settotalframe = tk.Frame(root, bg=bgcolour)
settotalframe.pack(pady=10)
settotallabel = tk.Label(settotalframe, text="Total number of items in the sets (optional):", bg=bgcolour)
settotallabel.pack(pady=5)
settotalentry = tk.Entry(settotalframe, width=20)
settotalentry.pack(pady=5)
#
endtitleframe = tk.Frame(root, bg=bgcolour)
endtitleframe.pack(pady=5)

submitBtn = tk.Button(root, text="Generate Venn Diagram", bg=bgcolour, height=2, width=30, font=("bold", 10))
submitBtn.pack(pady=10)

root.mainloop()