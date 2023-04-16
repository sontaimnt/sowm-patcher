from os import system , chdir
from os.path import isdir , isfile
from shutil import copy

patches = ["sowm-autostart.diff" , "sowm-border.diff" , "sowm-key-move-resize.patch" , "sowm-polybar.diff" , "sowm-rounded-corners.patch" , "sowm-winsplit.diff" , "sowm-wintitle.diff"]
user_patches = []

# check for patch folder and validate it

patch_dir = str(input("enter the directory containing patches:- "))
patch_folder_exists = isdir(patch_dir)

print("checking if the directory is valid...")
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

# now clone sowm from source

print("now cloning sowm")
if isfile("/usr/bin/git") == True:
    if system("git clone https://github.com/dylanaraps/sowm") == 0:
        print("cloning was sucessful")
        pass
    else:
        raise OSError("error: git clone was unsucessful")
else:
    raise FileNotFoundError("error: git not found")

# now display the patch list

print("enter the name of the patch you want to apply:- ")
for i in range(0 , len(patches)):
    print(patches[i])
print("note:- in order to apply multiple patches use the following format:- sowm-wintitle.diff , sowm-polybar.diff")
patches = str(input("patch name:- "))

# check if user entered patches are valid

user_patches.append(patches)
print(patches)
for i in range(0 , len(user_patches)):
    if isfile(user_patches[i]) == True:
        pass
    else:
        raise ValueError("error: user specified patches are not there")

# now copy to sowm build dir.. it should be in patches dir
for i in range(0 , len(user_patches)):
    copy(user_patches[i], "sowm/")

# now patch the specified patches
for i in range(0 , len(user_patches)):
    if system(f"patch -p1 < {user_patches[i]}") == 0:
        pass
    else:
        raise OSError("error: patching failed")

# build sowm
if system("sudo make install") == 0:
    raise OSError("error: compiling/installing sowm failed")
else:
    pass
