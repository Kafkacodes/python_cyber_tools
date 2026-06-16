import os 
import time

file_path = input("Enter the file path: ")
if os.path.exists(file_path):
    file_name = os.path.basename(file_path)
    print(f"File name: {file_name}")
    print("File exists.")
    file_size = os.path.getsize(file_path)
    print(f"File size: {file_size} bytes.")
    
    creation_time = os.path.getctime(file_path)
    modification_time = os.path.getmtime(file_path)
    
    print(f"Creation time: {time.ctime(creation_time)}")
    print(f"Modification time: {time.ctime(modification_time)}")
else:    print("File does not exist.")

if os.path.isdir(file_path):
    print("It's a directory.")
else:
    print("It's a file.")

    file_extension = os.path.splitext(file_path)[1]
    print(f"File extension: {file_extension}")
        