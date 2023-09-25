import customtkinter as ctk
import tkinter.messagebox as tkmsgbox
import json
import os
import glob
import shutil


class StudentsWindow(ctk.CTkToplevel):
    def __init__(self, subject, course, master=None ):
        super().__init__(master)

    
    
    def copy_to():
        try:
            if len(user_entry.get()) <= 3:
                tkmsgbox.showwarning("User", "Please enter user")
                return

            with open('settings.settings', 'r') as settings_file:
                settings_data = json.load(settings_file)
                # print(settings_data)
                data_path = settings_data['default_data_folder']
                kermit_path = settings_data['kermit_path']
                source_directory = os.path.join(data_path, user_entry.get(), "print", sub_entry.get())
                destination_directory = kermit_path

                if not os.path.exists(source_directory):
                    tkmsgbox.showwarning("Source Directory Error", f"Source directory '{source_directory}' does not exist.")
                    return

                if not os.path.exists(destination_directory):
                    tkmsgbox.showwarning("Destination Directory Error", f"Destination directory '{destination_directory}' does not exist.")
                    return
            
                # source_folder = "C:/Users/Rohit/Desktop/test_Print/data/mcs2106/print/dbms"
                # destination_folder = "C:/Users/Rohit/Desktop/test_Print/kermit"
                source_folder = source_directory
                destination_folder = destination_directory
                allowed_extensions = {'.txt', '.c', '.cpp'}
            # print(source_folder, destination_folder, allowed_extensions)
            
                copy_specific_files(source_folder, destination_folder, allowed_extensions)
                process_all_files_user(user_entry.get(), destination_folder)
                tkmsgbox.showinfo("Copied", "Copied to kermit and print started")

        except Exception as e:
            tkmsgbox.showerror("Error", f"An error occurred while copying files: {str(e)}")

