
import tkinter as tk
from tkinter import messagebox

def calculate_total_marks():
    try:
        marks = [int(entry.get()) for entry in entries]
        total_marks = sum(marks)
        messagebox.showinfo("Result", f"Total Marks: {total_marks}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

def calculate_percentage():
    try:
        marks = [int(entry.get()) for entry in entries]
        total_marks = sum(marks)
        percentage = (total_marks / (len(marks) * 100)) * 100
        messagebox.showinfo("Result", f"Percentage: {percentage:.2f}%")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Student Marks Calculator")


root.iconbitmap('Mehran_University_of_Engineering_and_Technology_logo.svg - Copy.ico')

# GUI Layout
tk.Label(root, text="Enter marks for 5 subjects:").grid(row=0, column=0, columnspan=2)

entries = []
for i in range(5):
    tk.Label(root, text=f"Subject {i+1}:").grid(row=i+1, column=0, padx=10, pady=5)
    entry = tk.Entry(root)
    entry.grid(row=i+1, column=1, padx=10, pady=5)
    entries.append(entry)

# Buttons
tk.Button(root, text="Calculate Total Marks", command=calculate_total_marks).grid(row=6, column=0, pady=10)
tk.Button(root, text="Calculate Percentage", command=calculate_percentage).grid(row=6, column=1, pady=10)

# Run the application
root.mainloop()
