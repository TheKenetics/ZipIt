import sys, tkinter, zipit_cmd

"""
Plan:
	Choose folder to zip subfolders
	After picked, have list of folders that will be zipped
	Click button to zip all subfolders

	Additional features
		Have checkmarks next to items to select which folders should be zipped
		Have another text box that takes a string, and will select/deselect items based on startswith, endswith, and contains

frame = tkinter.Frame(root, width=100, height=100)
frame.pack()
frame.pack(side=tkinter.BOTTOM)



label = tkinter.Label(frame, text="asd", bg="black", fg="white")
label.pack(side=tkinter.LEFT, fill=tkinter.X/Y)

button = tkinter.Button(frame, text="asd", fg="red", command=funcname)
button.bind("<Button-1>", funcname) # left mouse button click
<Button-2> Middle click
<Button-3> Right click
button.pack()
button.pack(side=tkinter.LEFT)

entry = tkinter.entry(frame)
entry.pack(side=tkinter.LEFT)
entry.grid(row=0, column=0, sticky=tkinter.N/E/S/W, rowspan=2, columnspawn=2)
sticky aligns things within cells, so sticky=E right aligns

checkbox = tkinter.Checkbutton(frame, text="asd")
checkbox.pack(side=LEFT)

menu = tkinter.Menu(root)
root.config(menu=menu)

submenu = tkinter.Menu(menu)
menu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Do Something..." command=funcname)


frame.quit function to quit
"""

def main():
	root = tkinter.Tk()

	

	root.mainloop()

if __name__ == "__main__":
	main()
