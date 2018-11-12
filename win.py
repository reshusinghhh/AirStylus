from Tkinter import *


root = Tk(className="Air Stylus")


root.configure(background='white', cursor="arrow")
root.geometry("1280x720")
root.resizable(width=True, height=True)

h = StringVar()
heading = Label(root, textvariable=h, fg='red')



h.set('AIR STYLUS')
heading.configure(font=('Ethocentric', 37))
heading.pack()



pre = StringVar()
present = Label(root, textvariable=pre)
pre.set('Presented to you by:-\nGuneet Kaur\nReshu Singh\nAmisha Rawat\nCharanjeet Kaur')
present.configure(font=('Helvetica', 15))
present.pack(side=BOTTOM)

textBox = Text(root, height=1100, width=600)
textBox.config(font=("Courier", 50))
textBox.pack()

root.mainloop()
