import os
import csv
import tkinter as tk

# Move to the directory where this script is located
os.chdir(os.path.dirname(os.path.realpath(__file__)))

data = []
fields = []

def create_field(default_command=None, default_element=None):
    # Define the dropdown options
    options = ['procedure', 'description', 'img', 'video','code']  # You can change this list according to your needs

    # Create a StringVar object to hold the selected option
    selected_option = tk.StringVar(root)
    if default_command:
        selected_option.set(default_command)  # Use the default command if provided
    else:
        selected_option.set(options[0])  # Use the first option as default

    dropdown = tk.OptionMenu(root, selected_option, *options)
    dropdown.grid(row=len(fields)+2, column=1)
    
    new_field2 = tk.Entry(root)
    if default_element:
        new_field2.insert(0, default_element)
    new_field2.grid(row=len(fields)+2, column=2)
    
    fields.append((dropdown, selected_option, new_field2))  # Add the OptionMenu widget itself to the fields list

def add_field():
    create_field()

def remove_field():
    if len(fields) > 0:
        field_to_remove = fields.pop()
        field_to_remove[0].grid_forget()  # Hide the dropdown widget
        field_to_remove[2].destroy()  # Destroy the entry field

def export_to_csv():
    # Add predefined rows at the start
    data.append(['title', 'foldername'])
    data.append(['thumbnail', 'filename_thumbnail.png'])

    for field in fields:
        command = field[1].get()  # Now represents command
        element = field[2].get()  # Now represents element
        if command and element:  # Check if both fields are non-empty
            data.append([command, element])

    with open('HTML_data.csv', 'w', newline='', encoding='utf-8') as f:  # Updated file name
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
create_field(default_command='procedure', default_element='foldername')
create_field(default_command='description', default_element='filename_thumbnail.png')

root.mainloop()
