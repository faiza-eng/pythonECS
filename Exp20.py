import tkinter as tk

def on_click():
    label.config(text="Button Clicked!")

root = tk.Tk()
root.title("My App")
root.geometry("300x200")

label = tk.Label(root, text="Welcome to Python GUI")
label.pack(pady=20)

button = tk.Button(root, text="Click Me", command=on_click)
button.pack()

root.mainloop()