import cv2
img_paths = [r'Project/AumentedData/train/E/4.jpg',r'Project\AumentedData\train\M\181.jpg',r'Project\AumentedData\train\R\mano_dani27.jpg', r'Project\AumentedData\train\W\W (1352).jpg',r'Project\AumentedData\train\W\mano_dani294.jpg',r'Project\AumentedData\train\W\mano_dani142.jpg',r'Project\AumentedData\train\O\mano_dani64.jpg',r'Project\AumentedData\train\I\I (599).jpg', r'Project\AumentedData\train\J\mano_dani388.jpg']

for index, img_path in enumerate(img_paths):
    img = cv2.imread(img_path)
    # img = img/255
    cv2.imshow(f'im{index}',img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(img, 5)
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    img = img/255
    cv2.imshow(f'im{index}_p',img)






while True:
    k = cv2.waitKey(100)
    if k == ord('q'):
        break