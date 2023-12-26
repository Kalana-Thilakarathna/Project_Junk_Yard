import os
import shutil
from tkinter import messagebox
from tqdm import tqdm
import datetime
import psutil

def get_system_startup_time():
    boot_time_timestamp = psutil.boot_time()
    boot_time = datetime.datetime.fromtimestamp(boot_time_timestamp)
    return boot_time.date()

def read_last_execution_date(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read().strip()
    return None

def write_last_execution_date(file_path, date):
    with open(file_path, 'w') as file:
        file.write(date)
        
        
last_execution_file = "last_execution_date.txt"
system_startup_date = get_system_startup_time()
last_execution_date = read_last_execution_date(last_execution_file)

if last_execution_date != str(system_startup_date):

    try:    
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        unwanted_dirs = ["JunkYard","Potato Model","Project_Junk_Yard","Results"]

        file_extensions_dict = {
            "document": [
            ".pdf", ".docx", ".xlsx", ".pptx", ".txt", ".csv", ".rtf", ".html", ".xml", 
            ".doc", ".xls", ".ppt", ".mpp", ".doc", ".docm", ".dot", ".dotm", ".xls", 
            ".xlsm", ".xlt", ".xltm", ".ppt", ".pptm", ".pot", ".potm", ".pub", ".vsd", ".vsdx"
            ],
            "video": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".m4v", ".3gp"],
            "audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a", ".ape", ".alac"],
            "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".svg"],
            "compressed": [".zip", ".rar", ".tar", ".gz", ".bz2", ".7z", ".xz", ".lzh", ".z", ".tar.gz", ".tar.bz2"]
        }

        #check if there is jy folder or dont create a one
        print(f"Desktop Path: {desktop_path}")
        directs = os.listdir(desktop_path)
        counter = 0
        for direct in directs:
            counter = counter + 1
            if (direct == "JunkYard"):
                print("its their")
                continue
            else:
                if counter == len(directs):
                    try:
                        jy_path = os.path.join(desktop_path,"JunkYard")
                        os.makedirs(jy_path)
                        print("dir created")
                    except FileExistsError:
                        print("file is already thier")     
                        
        #subfolder  creator 
        from datetime import date, timedelta
        current_date = date.today()
        yesterday = current_date - timedelta(days=1)
        subfolder_path = os.path.join(jy_path,str(yesterday))
        os.makedirs(subfolder_path)
        video_path = os.path.join(subfolder_path,'Video')
        audio_path = os.path.join(subfolder_path,'Audio')
        images_path = os.path.join(subfolder_path,'Images')
        document_path = os.path.join(subfolder_path,'Document')
        compressed_path = os.path.join(subfolder_path,'Compressed')
        other_path = os.path.join(subfolder_path,'Other')
        os.makedirs(other_path)
        folder_path = os.path.join(subfolder_path,'Folder')
        os.makedirs(folder_path)
        paths = {"video":video_path,"audio":audio_path, "images":images_path, "document":document_path, "compressed":compressed_path}
        for i in paths:
            print(i)
            os.makedirs(paths.get(i))

                        
        #checker and mover
        from pathlib import Path
        directs = os.listdir(desktop_path)
        for direct in directs:
        #for direct in tqdm(directs, desc="Organizing Files", unit="file"):
            filepath = os.path.join(desktop_path,direct)
            counter = 0
            
            if os.path.isfile(filepath):
                file_type = Path(filepath).suffix
                extension_counter = 0
                
                for dict_key in file_extensions_dict:
                    extension_counter += 1
                    extensions_list = file_extensions_dict.get(dict_key)
                    
                    for extention in extensions_list:
                        if extention == file_type:
                            shutil.move(filepath,paths.get(dict_key))
                        else:
                            continue
                        
                if extension_counter == len(file_extensions_dict):
                    try:
                        shutil.move(filepath,other_path)
                    except Exception as generic_error:
                        print(generic_error) 
                
            else:
                for i in unwanted_dirs:
                    if i == direct:
                        continue
                    counter += 1
                if counter >= len(unwanted_dirs):
                    shutil.move(filepath, folder_path)
            print()
    except Exception as generic_error:
        messagebox.showerror("Error", f"An error occurred: {str(generic_error)}")
    write_last_execution_date(last_execution_file, str(system_startup_date))
else:
    messagebox.showerror("Error", "An error occurred: The script is already run for the day")
