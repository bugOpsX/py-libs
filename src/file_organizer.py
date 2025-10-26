import os
import shutil
from datetime import datetime

def organize_by_extension(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            ext = filename.split('.')[-1] if '.' in filename else 'no_extension'
            ext_folder = os.path.join(folder_path, ext)
            os.makedirs(ext_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(ext_folder, filename))

def organize_by_date(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            creation_time = os.path.getctime(file_path)
            date_folder = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d')
            date_folder_path = os.path.join(folder_path, date_folder)
            os.makedirs(date_folder_path, exist_ok=True)
            shutil.move(file_path, os.path.join(date_folder_path, filename))

if __name__ == "__main__":
    folder = input("Enter folder path: ")
    method = input("Sort by (extension/date): ").strip().lower()
    
    if method == "extension":
        organize_by_extension(folder)
    elif method == "date":
        organize_by_date(folder)
    else:
        print("Invalid option! Choose 'extension' or 'date'.")

