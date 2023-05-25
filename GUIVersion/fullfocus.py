import os
import tkinter as tk

window = tk.Tk()
window.title("Full Focus")
window.geometry("500x500")

image_path = "src/marvin.png"
background_image = tk.PhotoImage(file=image_path)

label = tk.Label(window, image=background_image)
label.place(x=0, y=0, relwidth=1, relheight=1)

window.mainloop()