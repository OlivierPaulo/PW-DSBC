import shutil
import send2trash
import os
from collections import defaultdict
import notify2

home = os.path.expanduser("~")
down_folders = [os.path.join(home,"Downloads"),os.path.join(home,"Téléchargements")]
#print(down_folders)


extension_dict = {}
folders_path = {}

files_type = ['image','video','word_doc','excel_doc','iso_file','archive','text','music','pogramming','cal','doc']

extension_dict['image'] = ['png','bmp','jpg','jpeg']
folders_path['image'] = os.path.join(home,"Images")

extension_dict['video'] = ['avi','mkv','mp4','flv','mpg','mpeg']
folders_path['video'] = os.path.join(home,"Vidéos")

extension_dict['word_doc'] = ['doc','docx','odt']
folders_path['word_doc'] = os.path.join(home,"Documents","Word Docs")

extension_dict['excel_doc'] = ['xls','xlsx','ods','csv']
folders_path['excel_doc'] = os.path.join(home,"Documents","Excel Docs")

extension_dict['doc'] = ['pdf']
folders_path['doc'] = os.path.join(home,"Documents")

extension_dict['iso_file'] = ['iso']    
folders_path['iso_file'] = os.path.join(home,"Documents","ISO")

extension_dict['archive'] = ['zip','rar','gz']    
folders_path['archive'] = os.path.join(home,"Documents","Archives")

extension_dict['text'] = ['txt','rtf']    
folders_path['text'] = os.path.join(home,"Documents","Texts")

extension_dict['music'] = ['mp3','flac','wav']    
folders_path['music'] = os.path.join(home,"Musique")

extension_dict['programming'] = ['py','bat','c','java','htm','html','js','json']    
folders_path['programming'] = os.path.join(home,"Documents","Programming")

extension_dict['cal'] = ['ical','ics']    
folders_path['cal'] = os.path.join(home,"Documents","Calendar")

file_dictionnary = defaultdict(dict)

for file_type in files_type:
    if file_type in folders_path.keys():
        file_dictionnary[file_type]['ext'] = extension_dict[file_type]
        file_dictionnary[file_type]['path'] = folders_path[file_type]

#print(file_dictionnary)

for down_folder in down_folders:
    for folder, subfolders, files in os.walk(down_folder):
        for file in files:
            for keys,values in file_dictionnary.items():
                if file.rsplit(sep='.')[-1] in file_dictionnary[keys].get('ext'):
                    if file in os.listdir(folder):
                        try:
                            shutil.move(os.path.join(folder,file),file_dictionnary[keys].get('path'))
                            print(f"{os.path.join(folder,file)} as {keys} has been move to {file_dictionnary[keys].get('path')}")
                        except shutil.Error:
                            print(f"Warning : This file {file} probably exist in destintation folder {file_dictionnary[keys].get('path')}")

remain_files_list = []
notify2.init("Notification Cleaning Download Folders")
n_message = ""
summary = "Clean Download Folders"
n = notify2.Notification(summary, message=n_message, icon=f"{os.path.join(folders_path['programming'],'Python','python.png')}")

for down_folder in down_folders:
    for folder, subfolders, files in os.walk(down_folder):
        remain_files_list += files

if len(remain_files_list) > 0:
    message = f"The are still {len(remain_files_list)} files in \"Downloads\" and/or \"Téléchargements\" :\n"
    #print(f"The are still {len(remain_files_list)} files in \"Downloads\" and/or \"Téléchargements\" :")
    for file in remain_files_list:
        #print(f"- {file}")
        message += f"- {file}"
    n.update(summary,message)
else:
    #print(f"No more files inside \"Downloads\" neither inside \"Téléchargements\"")
    message = f"No more files inside \"Downloads\" neither inside \"Téléchargements\""
    n.update(summary,message)

n.show()