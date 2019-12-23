from tkinter import *
from PIL import ImageTk, Image
import os
from functools import partial
## Set Taskbar Icon
import ctypes
import matplotlib.pyplot as plt
myappid = 'galaxy.bird.flappy.1' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

root = Tk()
root.iconbitmap(r'./assets/ICON.ico')
root.title("Super Angry Flappy Bird")

label = Label(root)


def toggle(tog):
	tog[0] = not tog[0]
	
	def toggle2():
		variable = True
		image = plt.imread("./assets/cover.jpg")
		img = Image.fromarray(image)
		imgtk = ImageTk.PhotoImage(image=img)
		label.imgtk = imgtk
		label.configure(image=imgtk)
		tog[0] = not tog[0]
	image = plt.imread("./assets/information.jpg")
	img = Image.fromarray(image)
	imgtk = ImageTk.PhotoImage(image=img)
	label.imgtk = imgtk
	label.configure(image=imgtk)
	HELP.config(text='CLOSE' if tog[0] else 'INFORMATION',command = toggle2)
	
	




HELP = Button(root, text="INFORMATION", bg="RED",fg="WHITE",width = 85,
                       command=partial(toggle, [False]))

HELP.pack()

label.pack()
frame = Frame(root)
frame.pack()

image = plt.imread("./assets/cover.jpg")
img = Image.fromarray(image)
imgtk = ImageTk.PhotoImage(image=img)
label.imgtk = imgtk
label.configure(image=imgtk)



def sel():
	if(var.get()==1):
		selection = "You selected Native Flappy Bird Mode"
		first_args = "-native"
	if(var.get()==2):
		selection = "You selected Super Mario Mode"
		first_args = "-mario"
	if(var.get()==3):
		selection = "You selected Angry Bird Mode"
		first_args = "-angry"
	label2.config(text = selection)
   
def sel2():
	if(CheckVar1.get()==1):
		selection = "Debugging Mode is ON"
		second_args = "-debug"
		label3.config(text = selection)
	else:
		selection = "Debugging Mode is OFF"
		second_args = ""
		label3.config(text = selection)

def run():
	#label4.config(text = "STARTING PLEASE WAIT...")
	command_to_execute = "python flappy.py"
	first_args = ""
	second_args = ""
	if(var.get()==0):
		first_args = "-native"
	if(var.get()==1):
		first_args = "-native"
	if(var.get()==2):
		first_args = "-mario"
	if(var.get()==3):
		first_args = "-angry"
	if(CheckVar1.get()==1):
		second_args = "-debug"
	if(CheckVar1.get()==0):
		second_args = ""
	final_command_to_execute = command_to_execute+" "+first_args+" "+second_args
	label4.config(text = "Command Executed: "+final_command_to_execute)
	os.system('start cmd /c '+final_command_to_execute)

#root = Tk()

var = IntVar()
R1 = Radiobutton(frame, text="Native Flappy Bird", variable=var, value="1",width = 25,
                  command=sel)
R1.pack( side = LEFT )
R2 = Radiobutton(frame, text="Super Mario", variable=var, value="2",width = 25,
                  command=sel)
R2.pack( side = LEFT )
R3 = Radiobutton(frame, text="Angry Bird", variable=var, value="3",width = 25,
                  command=sel)
R3.pack( side = LEFT)


bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )
CheckVar1 = IntVar()
C1 = Checkbutton(bottomframe, text = "Debug", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 20,command=sel2)
C1.pack()



Submit = Button(bottomframe, text="START", fg="green",width = 25,command=run)
Submit.pack( side = RIGHT)


label2 = Label(root)
label2.pack()
label.configure(text="Default is Native Flappy Bird Mode")
label3 = Label(root)
label3.pack()
label.configure(text="Debugging Mode is OFF")
label4 = Label(root)
label4.pack()





root.update()
frame.update()
root.mainloop()