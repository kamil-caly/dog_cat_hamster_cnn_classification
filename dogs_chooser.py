import os
import random
import shutil

# Ścieżka do foldera zawierającego wszystkie podfoldery z obrazami
main_folder = "./Images"

# Wybór 12 losowych zdjęć z każdego podfoldera
for folder_name in os.listdir(main_folder):
    folder_path = os.path.join(main_folder, folder_name)
    if os.path.isdir(folder_path):
        image_files = [file for file in os.listdir(folder_path) if file.endswith('.jpg')]
        if len(image_files) > 12:
            chosen_images = random.sample(image_files, 12)
        else:
            chosen_images = image_files
        for image_name in chosen_images:
            source_path = os.path.join(folder_path, image_name)
            destination_path = os.path.join("./correct_img", image_name)
            shutil.copy(source_path, destination_path)

