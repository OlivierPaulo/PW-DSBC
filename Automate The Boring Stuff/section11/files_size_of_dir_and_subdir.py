import os

def navigation_folder(folder_path):
    total_size = 0
    for f in os.listdir(folder_path):             # => for each element in the working directory
        if os.path.isdir(os.path.join(folder_path,f)):                        # => check if element is a directory                           
            total_size += navigation_folder(os.path.join(folder_path,f))      # if yes, sum the call back to the function with sub directories          
        else:
            #print(os.path.getsize(os.path.join(folder_path,f)))                                                                 # else element is a file
            total_size += os.path.getsize(os.path.join(folder_path,f))        # sum the size of the files in final directory
    return total_size                                                         # return total size

size = navigation_folder(os.getcwd())
To = 1000000000000
Go = 1000000000
Mo = 1000000
ko = 1000

if size / To > 1 :
    print(f"{str(round(size / To,2))} To")
elif size / Go > 1 :
    print(f"{str(round(size / Go,2))} Go")
elif size / Mo > 1 :
    print(f"{str(round(size / Mo,2))} Mo")
elif size / ko > 1 :
    print(f"{str(round(size / ko,2))} ko")
else:
    print(f"{str(round(size,2))} octets")

