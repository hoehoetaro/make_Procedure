import os
import csv
import tkinter as tk

# Move to the directory where this script is located
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Get the name of the directory where this script is located
foldername = os.path.basename(os.getcwd())

# Get the thumbnail file name
thumbnail_filename = f"{foldername}_thumbnail.png"

data = []
fields = []

def create_field(default_command=None, default_element=None):
    # Define the dropdown options
    options = ['procedure', 'description', 'img', 'video', 'code']

    # Create a StringVar object to hold the selected option
    selected_option = tk.StringVar(root)
    if default_command:
        selected_option.set(default_command)
    else:
        selected_option.set(options[0])

    dropdown = tk.OptionMenu(root, selected_option, *options)
    dropdown.grid(row=len(fields)+2, column=1)
    
    new_field2 = tk.Entry(root)
    if default_element:
        new_field2.insert(0, default_element)
    new_field2.grid(row=len(fields)+2, column=2)
    
    fields.append((dropdown, selected_option, new_field2))

def add_field():
    create_field()

def remove_field():
    if len(fields) > 0:
        field_to_remove = fields.pop()
        field_to_remove[0].grid_forget()  # Hide the dropdown widget
        field_to_remove[2].destroy()  # Destroy the entry field

def export_to_csv():
    # Add predefined rows at the start
    data.append(['title', foldername])
    data.append(['thumbnail', thumbnail_filename])

    for field in fields:
        command = field[1].get()
        element = field[2].get()
        if command and element:
            data.append([command, element])

    with open('HTML_data.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['command', 'element'])  # Add headers
        writer.writerows(data)

    root.destroy()  # Close the program

root = tk.Tk()

button_add = tk.Button(root, text="Add Record", command=add_field)
button_add.grid(row=0, column=0)

button_remove = tk.Button(root, text="Remove Record", command=remove_field)
button_remove.grid(row=0, column=1)

button_export = tk.Button(root, text="Export to CSV", command=export_to_csv)
button_export.grid(row=0, column=2)

# Create headers
header1 = tk.Label(root, text="Command")
header1.grid(row=1, column=1)
header2 = tk.Label(root, text="Element")
header2.grid(row=1, column=2)

# Create initial 2 fields with default commands
create_field(default_command='procedure')
create_field(default_command='description')

root.mainloop()
