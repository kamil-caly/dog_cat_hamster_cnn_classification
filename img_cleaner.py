from PIL import Image
import os

def remove_corrupted_images(folder_path):
    img_to_remove = []

    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg'):
            image_path = folder_path + '/' + filename
            size = os.stat(image_path).st_size
            if size <= 0:
                img_to_remove.append(image_path)

    for img in img_to_remove:
         os.remove(img)


# Ścieżka do folderu ze zdjęciami
folder_path = 'D:/Users/EL_kammex/PyCharm_projects/cnn-klasyfikacja_wieloklasowa/cats/img'
remove_corrupted_images(folder_path)
# 2687 files