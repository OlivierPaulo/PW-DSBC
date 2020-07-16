import shutil
import send2trash
import os

## Walking into Folder and SubFolders and files inside them.
for folder, subfolders, files in os.walk(os.getcwd()):
    print(f"Folder : {folder}")
    print(f"SubFolders : {subfolders}")
    print(f"Files : {files}")
