import tkinter as tk
#declare var
window = tk.Tk()

window.title("Reshu's App")

window.geometry("400x400")

# LABEL
title = tk.Label(text="Hello World,Welcome to my app :D", font=("Times New Roman", 20))
title.grid(column=0, row=0)

#Button
button1=tk.Button(text="Click me!", bg="pink")
button1.grid(column=0, row=1)

#Entry Field
entry_field1 = tk.Entry()
entry_field1.grid(column=0, row=2)

#Text Field
text_field = tk.Text(master=window, height=10, width=30)
text_field.grid()


window.mainloop()