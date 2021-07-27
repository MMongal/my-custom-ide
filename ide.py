from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess

# author: MM

compiler = Tk()
compiler.title('My Favorite IDE')

file_path = ''

# Set the file path
def set_file_path(path):
	global file_path
	file_path = path

# Function to save a file and set the file path
def save_as():
	if file_path == '':
		path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
	else:
		path = file_path
	with open(path, 'w') as file:
		code = editor.get('1.0', END)
		file.write(code)
		set_file_path(path)

# Function to open a file and set the file path
def open_file():
	path = askopenfilename(filetypes=[('Python Files', '*.py')])
	print('Open file path: ' , path)
	with open(path, 'r') as file:
		code = file.read()
		editor.delete('1.0', END)
		editor.insert('1.0', code)
		set_file_path(path)

### Old run function that executes command ###
# def run():
# 	code = editor.get('1.0', END)
# 	print(code)
# 	exec(code)

# A run function that uses the subprocess to execute python 
# given a python file (file_path)
# captures the output and error from the process
# and passes them to the code_output to be displayed
def run():
	command = f'python3 {file_path}'
	process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	output, error = process.communicate()
	code_output.delete(1.0, END)
	code_output.insert(1.0, output)
	code_output.insert(1.0, error)


# Adding a menu bar to the frame
menu_bar = Menu(compiler)

# Adding a file menu to the menu bar that calls the file func
file_bar = Menu(menu_bar, tearoff=0)
file_bar.add_command(label='Open', command=open_file)
file_bar.add_command(label='Save', command=save_as)
file_bar.add_command(label='Save As', command=save_as)
file_bar.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu=file_bar)

# Adding a run menu to the menu bar that calls the run func
run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run', menu=run_bar)

compiler.config(menu=menu_bar)

# text area used as an editor to type the code
editor = Text()
editor.pack()

# text area added below editor, used for output
code_output = Text(height=10)
code_output.pack()

compiler.mainloop()


