from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename


compiler = Tk()
compiler.title('My Favorite IDE')

# Function to save a file
def save_as():
	path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
	with open(path, 'w') as file:
		code = editor.get('1.0', END)
		file.write(code)

# Function to open a file
def open_file():
	path = askopenfilename(filetypes=[('Python Files', '*.py')])
	with open(path, 'r') as file:
		code = file.read()
		editor.delete('1.0', END)
		editor.insert('1.0', code)

# Function that executes command
def run():
	code = editor.get('1.0', END)
	# print(code)
	exec(code)

# Adding a menu bar to the frame
menu_bar = Menu(compiler)

# Adding a run menu to the menu bar that calls the run func
run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run', menu=run_bar)

# Adding a file menu to the menu bar that calls the file func
file_bar = Menu(menu_bar, tearoff=0)
file_bar.add_command(label='Open', command=open_file)
file_bar.add_command(label='Save', command=exit)
file_bar.add_command(label='Save As', command=save_as)
file_bar.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu=file_bar)



compiler.config(menu=menu_bar)

editor = Text()
editor.pack()
compiler.mainloop()


