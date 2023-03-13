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

#Create a button to browse for first folder.
browse_button = tk.Button(window, text="Select old folder",command=select_folder1)
browse_button.pack(padx=20, pady=20)

#Create a button to browse for second folder.
browse_button = tk.Button(window, text="Select new folder",command=select_folder2)
browse_button.pack(padx=20, pady=20)

#Add a widget for old text entry.
label = tk.Label(text="Enter old text to remove.")
label.pack()
old_text = tk.Entry(window)
label = tk.Label(text="Enter old text to remove.")
label.pack()
new_text = tk.Entry(window)

#Add a button to initiate copy and paste.
big_green_button = tk.Button(
    text="Copy, rename, and paste files.",
    bg="red")
#big_green_button = crp

#Main loop
window.mainloop()
