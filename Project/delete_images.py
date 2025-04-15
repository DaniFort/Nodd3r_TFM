import os
with open('must_delete.txt','r')as file:
    for img_path in file.readlines():
        path = img_path.strip()
        if os.path.exists(path):
            os.remove(path)