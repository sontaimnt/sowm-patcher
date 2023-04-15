from os import system , chdir
from os.path import isdir , isfile

patches = ["sowm-autostart.diff" , "sowm-border.diff" , "sowm-key-move-resize.patch" , "sowm-polybar.diff" , "sowm-rounded-corners.patch" , "sowm-winsplit.diff" , "sowm-wintitle.diff"]

# check for patch folder and validate it
patch_dir = str(input("enter the directory containing patches:- "))
patch_folder_exists = isdir(patch_dir)

if patch_folder_exists == True:
    chdir(patch_dir)
    for i in range(0 , len(patches)):
        if isfile(patches[i]) == True:
            continue
        else:
            raise FileNotFoundError(patches[i]," not found")
            exit(1) 
    pass
else:
    raise FileNotFoundError(patch_dir," not found")

# check for sowm copy... if not found then clone from git
