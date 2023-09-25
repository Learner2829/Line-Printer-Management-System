import customtkinter as ctk
import tkinter.messagebox as tkmsgbox
import json
import os
import glob
import shutil
from datetime import date
from settings import SettingsWindow
from student_choose import StudentsWindow
from process_all import process_all_files_user
from PIL import ImageTk

root = ctk.CTk() #set root window
ctk.set_appearance_mode("Light") #theme = light
# root.attributes("-alpha", 0.9) # transparency
root.minsize(600, 370) #set mninimum size of window
root.title("Line Printer Management System") # title of program
#logo icon
root.wm_iconbitmap()
root.iconphoto(False, ImageTk.PhotoImage(file=("logo.ico")))
# functions

def open_settings():
    settings_window = SettingsWindow(root) #display settings window
    # settings_window.wm_attributes("-topmost", True) # always on top of all windows
    
#connect to server for z drive
def connect_server():
    try:
        os.system("net use Z: \\\\" + ip_entry.get())
    except:
        tkmsgbox.showerror("Z error", "Z dive exists or can't be created")

# remover server , z drive
def disconnect_server():
    os.system("net use Z: /delete")

# copy all files from user print folder
def copy_specific_files(source_folder, destination_folder, extensions):
    # Ensure the source folder exists
    if not os.path.exists(source_folder):
        print(f"Source folder '{source_folder}' does not exist.")
        return

    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Loop through all files in the source folder
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        # Check if it's a file (not a subfolder) and copy it if its extension is in the list of extensions
        if os.path.isfile(source_path):
            file_extension = os.path.splitext(filename)[1].lower()
            if file_extension in extensions:
                destination_path = os.path.join(destination_folder, filename)
                shutil.copy2(source_path, destination_path)
                # print(f"Copied '{source_path}' to '{destination_path}'")

# def copy_to():
#     try:
#         if len(user_entry.get()) <= 3:
#             tkmsgbox.showwarning("User", "Please enter user")
#             return

#         with open('settings.settings', 'r') as settings_file:
#             settings_data = json.load(settings_file)
#             # print(settings_data)
#             data_path = settings_data['default_data_folder']
#             kermit_path = settings_data['kermit_path']
#             source_directory = os.path.join(data_path, user_entry.get(), "print", sub_entry.get())
#             destination_directory = kermit_path

#             if not os.path.exists(source_directory):
#                 tkmsgbox.showwarning("Source Directory Error", f"Source directory '{source_directory}' does not exist.")
#                 return

#             if not os.path.exists(destination_directory):
#                 tkmsgbox.showwarning("Destination Directory Error", f"Destination directory '{destination_directory}' does not exist.")
#                 return
            
#             # source_folder = "C:/Users/Rohit/Desktop/test_Print/data/mcs2106/print/dbms"
#             # destination_folder = "C:/Users/Rohit/Desktop/test_Print/kermit"
#             source_folder = source_directory
#             destination_folder = destination_directory
#             allowed_extensions = {'.txt', '.c', '.cpp'}
#             # print(source_folder, destination_folder, allowed_extensions)
            
#             copy_specific_files(source_folder, destination_folder, allowed_extensions)
#             process_all_files_user(user_entry.get(), destination_folder)
#             tkmsgbox.showinfo("Copied", "Copied to kermit and print started")

#     except Exception as e:
#         tkmsgbox.showerror("Error", f"An error occurred while copying files: {str(e)}")


# top frame
top_frame = ctk.CTkFrame(root, fg_color="#ebebeb") # color will transparent to merge with background
top_frame.pack(anchor=ctk.N, padx = 15, pady = 15, fill = ctk.X)

#settings button to open settings as inner seperate window
settings_btn = ctk.CTkButton(top_frame, text="⏣", font=('', 30), width = 30, command=open_settings)
settings_btn.pack(side = ctk.RIGHT)

# today's date
today = date.today().strftime("%d-%m-%Y") # formatting date
today_display = ctk.CTkLabel(top_frame, text = today)
today_display.pack(side = ctk.LEFT)

# all main inputs in central frame
central_frame = ctk.CTkFrame(root, fg_color="#ebebeb") # central widget for every entries
central_frame.pack(padx=50, pady=50)

# ip
ip_label = ctk.CTkLabel(central_frame,text="IP: ") # declaring inside of central frame
ip_entry = ctk.CTkEntry(central_frame) # entry for ip address
ip_label.grid(row = 0, column = 0, pady = 5, padx = 10) #setting positions, margins
ip_entry.grid(row = 0, column = 1, pady = 5, padx = 10)

# user
# user_label = ctk.CTkLabel(central_frame,text="User: ")
# user_entry = ctk.CTkEntry(central_frame)
# user_label.grid(row = 1, column = 0, pady = 5, padx = 10)
# user_entry.grid(row = 1, column = 1, pady = 5, padx = 10)

# course
courses = ["select course","mcs1", "mcs2", "mcs3", "mca"]

def main_dropdown_selected(event):
    selected = course_entry.get()
    sub_entry = ctk.CTkComboBox(central_frame, values=subjects[selected])
    sub_entry.grid(row = 2, column = 1, pady = 5, padx = 10)
    # tkmsgbox.showinfo("hi", selected)

    # selected_main_option = course_entry.get()
    # if selected_main_option in subjects:
    #     subjects['values'] = subjects[selected_main_option]
    #     # subjects.current(0)

course_label = ctk.CTkLabel(central_frame, text="Course: ")
course_entry = ctk.CTkComboBox(central_frame, values=courses, command=main_dropdown_selected)
course_label.grid(row = 1, column = 0, pady = 5, padx = 10)
course_entry.grid(row = 1, column = 1, pady = 5, padx = 10)

# sub
subjects = {
    "select course": ["select a course"],
    "mcs1": ["fop", ""],
    "mcs2": ["ap", "dbms"],
    "mcs3": ["oocp", "dbms2"],
    "mca": ["s1", "s2"]
}
sub_label = ctk.CTkLabel(central_frame, text="Subject: ")
sub_label.grid(row = 2, column = 0, pady = 5, padx = 10)

# buttons
btn_frame = ctk.CTkFrame(root, fg_color="#ebebeb")
btn_frame.pack(anchor=ctk.SE, padx = 15, pady = 15)

connect_btn = ctk.CTkButton(btn_frame, text="Connect", command=connect_server, width=90)
connect_btn.grid(row=0, column=0, padx = 15, pady = 15)

disconnect_btn = ctk.CTkButton(btn_frame, text="Disconnect", command=disconnect_server, width=110)
disconnect_btn.grid(row=0, column=1, padx = 15, pady = 15)

print_btn = ctk.CTkButton(btn_frame, text="Print", width=80, command=StudentsWindow)
print_btn.grid(row=0, column=2, padx = 15, pady = 15)

# combobox = ctk.CTkOptionMenu(btn_frame, values = ["hi", "hello"])
# combobox = ctk.CTkOptionMenu(btn_frame, values=["hi", "hello"])
# combobox.grid(row = 1, column = 0)

# inserting ip
try:
    with open('settings.settings', 'r') as settings_file:
        settings_data = json.load(settings_file)
        # print(settings_data)
        ip_entry.insert(0, settings_data['default_ip'])
        data_path = settings_data['default_data_path']
        kermit_path = settings_data['kermit_path']

        print(data_path, kermit_path)

except:
    # print("doesn't exist")
    pass

root.mainloop() # run window