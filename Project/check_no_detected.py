import cv2

with open('current.txt','r')as file:
    current = int(file.read())
    new_current = current
    
with open('no_detected_f.txt','r')as file:
    imgs = file.readlines()

for i in range(current, len(imgs)):
    image_path = imgs[i]
    img = cv2.imread(image_path.strip())
    cv2.imshow('ie',img)
    cv2.waitKey(1)
    a = input('B para borrar')

    if a == 'b':
        with open('must_delete_f.txt','a') as file:
            file.write(image_path)
        with open('current.txt','w')as file:       
            new_current = new_current+1
            file.write(str(new_current))
    elif a =='f':
        break
    else:
        with open('current.txt','w')as file:       
            new_current = new_current+1
            file.write(str(new_current))