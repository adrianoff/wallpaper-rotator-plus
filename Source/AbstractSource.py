import datetime
import os
from abc import ABC
from abc import abstractmethod

import requests

from PIL import Image
import cv2


class AbstractSource(ABC):
    def __init__(self, wallpapers_dir):
        self.wallpapers_dir = wallpapers_dir

    def download_picture(self, url):
        day_dir_name = datetime.datetime.now().strftime("%Y_%m_%d")
        day_dir_name_path = self.wallpapers_dir + '/' + day_dir_name

        if not os.path.exists(day_dir_name_path):
            os.mkdir(day_dir_name_path)

        wallpaper_file_path = day_dir_name_path + '/original.jpg'

        with open(wallpaper_file_path, "wb") as file:
            response = requests.get(url)
            file.write(response.content)
            file.close()

    def get_current_original(self):
        day_dir_name = datetime.datetime.now().strftime("%Y_%m_%d")
        day_dir_name_path = self.wallpapers_dir + '/' + day_dir_name
        wallpaper_file_path = day_dir_name_path + '/original.jpg'

        return wallpaper_file_path

    def get_current_wallpaper(self):
        day_dir_name = datetime.datetime.now().strftime("%Y_%m_%d")
        day_dir_name_path = self.wallpapers_dir + '/' + day_dir_name
        wallpaper_file_path = day_dir_name_path + '/wallpaper.jpg'

        return wallpaper_file_path

    @abstractmethod
    def get_image_url(self):
        pass

    def is_current_image_exists(self):
        file_name = self.get_current_original()

        return os.path.isfile(file_name)

    def resize(self):
        day_dir_name = datetime.datetime.now().strftime("%Y_%m_%d")
        day_dir_name_path = self.wallpapers_dir + '/' + day_dir_name

        blured_file_path = day_dir_name_path + '/blured.jpg'
        img = cv2.imread(self.get_current_original())
        dst = cv2.blur(img, (150, 150))
        cv2.imwrite(blured_file_path, dst)

        day_dir_name = datetime.datetime.now().strftime("%Y_%m_%d")
        day_dir_name_path = self.wallpapers_dir + '/' + day_dir_name
        blured_file_path = day_dir_name_path + '/blured.jpg'

        blured_resized_file_path = day_dir_name_path + '/blured_resized.jpg'
        blured_img = Image.open(blured_file_path)
        blured_resized_img = blured_img.resize((1920, 1080))
        blured_resized_img.save(blured_resized_file_path, 'JPEG')

        img = Image.open(self.get_current_original(), 'r')
        img_w, img_h = img.size

        background = Image.open(blured_resized_file_path)
        bg_w, bg_h = background.size
        offset = (int((bg_w - img_w) / 2), int((bg_h - img_h) / 2))

        wallpaper_final_file_path = day_dir_name_path + '/wallpaper.jpg'
        background.paste(img, offset)
        background.save(wallpaper_final_file_path, 'JPEG')