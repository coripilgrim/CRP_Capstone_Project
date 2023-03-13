import tkinter as tk
from tkinter import filedialog

#Create a tkinter window and name it.
window = tk.Tk()
window.title("File Copier and Renamer")
window.geometry("400x300")

#Define the function to the handle folder selection
def select_folder1():
    folder_path = filedialog.askdirectory()
    print("Selected folder:", folder_path)

def select_folder2():
    folder_path = filedialog.askdirectory()
    print("Selected folder:", folder_path)

def crp():
    print("Your copies have been made.")
    close_button = tk.Button(window, text="Close",command=window.destroy)
    close_button.pack()

#Create a button to browse for first folder.
browse_button = tk.Button(window, text="Select old folder",command=select_folder1)
browse_button.pack(padx=10, pady=10)

#Create a button to browse for second folder.
browse_button = tk.Button(window, text="Select new folder",command=select_folder2)
browse_button.pack(padx=10, pady=10)

#Add a widget for old text entry.
label = tk.Label(text="Enter text to remove from filename.")
label.pack()
old_text = tk.Entry()
old_text.pack()
label = tk.Label(text="Enter text to add to filename.")
label.pack()
new_text = tk.Entry()
new_text.pack()

#Add a button to initiate copy and paste.
big_green_button = tk.Button(
    text="Copy, rename, and paste files.",
    bg="green",
    fg="white",
    command=crp
    )
big_green_button.pack(padx=10, pady=10)

#Main loop
window.mainloop()
