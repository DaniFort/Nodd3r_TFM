import os
import shutil
import random
import time

BASE_PATH = 'AumentedData'
SPLITS = {
    'train':0.75,
    'validation':0.15,
    'test':0.10
    }
LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',  'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'del','space']

#creamos destinos
for split in SPLITS:
    for clase in LETTERS:
        dir_path = os.path.join(BASE_PATH,split,clase )
        os.makedirs(dir_path,exist_ok=True)

t0 = time.time()
for clase in LETTERS:
    t0_partial = time.time()
    class_path = os.path.join(BASE_PATH,clase)
    imgs = os.listdir(class_path)
    random.shuffle(imgs)

    img_amount = len(imgs)
    n_train = int(img_amount*SPLITS['train'])
    n_val = int(img_amount*SPLITS['validation'])
    n_test = img_amount - n_train- n_val

    divisions ={
        'train':imgs[:n_train],
        'validation':imgs[n_train:n_val+n_train],
        'test':imgs[n_train+n_val:],
    }

    for split, files in divisions.items():
        dst_base_path = os.path.join(BASE_PATH, split,clase)
        t0_split = time.time()
        for file in files:
            src_path = os.path.join(class_path,file)
            dst_path = os.path.join(dst_base_path,file)
            shutil.move(src_path,dst_path)
        print(f'    ____ {clase} {split} moved in {time.time()-t0_split} ____')
    print(f'--- {clase} moved in {time.time()-t0_partial} -----')

print(f'****** Task done in {time.time()-t0} *******')