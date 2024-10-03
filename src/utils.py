import os
from PIL import Image


def load_thumbnails_from_folder(folder_path):
    thumbnails = {}

    # list all files in the folder
    for filename in os.listdir(folder_path):
        # check if file is an image
        if filename.endswith((".png", ".jpg", ".jpeg")):
            image_path = os.path.join(folder_path, filename)

            img = Image.open(image_path)

            img.thumbnail((100, 100))

            thumbnails[image_path] = img

    return thumbnails
