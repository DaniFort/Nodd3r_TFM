import cv2

with open('no_detected.txt','r')as file:
    imgs = file.readlines()
for i in imgs:
    print(i)
    img = cv2.imread(i.strip())
    cv2.imshow('ie',img)
    cv2.waitKey(1)
    a = input('B para borrar')
    if a == 'b':
        with open('must_delete.txt','a') as file:
            file.write(i)