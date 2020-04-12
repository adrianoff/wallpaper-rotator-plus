import os
from abc import ABC
from abc import abstractmethod

import requests

from PIL import Image, ImageDraw, ImageFont
import cv2


class AbstractSource(ABC):
    def __init__(self, wallpapers_dir, screen_width, screen_height):
        self.wallpapers_dir = wallpapers_dir
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.picture_name = None
        self.painter_name = None

    def download_picture(self, url):
        wallpaper_file_path = self.wallpapers_dir + '/original.jpg'

        with open(wallpaper_file_path, "wb") as file:
            response = requests.get(url, timeout=(5, 30))
            file.write(response.content)
            file.close()

    def get_current_original(self):
        wallpaper_file_path = self.wallpapers_dir + '/original.jpg'

        return wallpaper_file_path

    def get_current_wallpaper(self):
        wallpaper_file_path = self.wallpapers_dir + '/wallpaper.jpg'

        return wallpaper_file_path

    @abstractmethod
    def get_image_info(self):
        pass

    def is_current_image_exists(self):
        file_name = self.get_current_original()

        return os.path.isfile(file_name)

    def resize(self):
        max_width = self.screen_width
        max_height = self.screen_height

        blurred_file_path = self.wallpapers_dir + '/blurred.jpg'
        # noinspection PyUnresolvedReferences
        img = cv2.imread(self.get_current_original())
        # noinspection PyUnresolvedReferences
        dst = cv2.blur(img, (150, 150))
        # noinspection PyUnresolvedReferences
        cv2.imwrite(blurred_file_path, dst)

        blurred_resized_file_path = self.wallpapers_dir + '/blurred_resized.jpg'
        blurred_img = Image.open(blurred_file_path)
        blurred_resized_img = blurred_img.resize((max_width, max_height))
        blurred_resized_img.save(blurred_resized_file_path, 'JPEG')

        img = Image.open(self.get_current_original(), 'r')
        width, height = img.size

        if width > max_width or height > max_height:
            ratio = min(max_width / width, max_height / height)
            width = int(width * ratio)
            height = int(height * ratio)

            img = img.resize((width, height))

        background = Image.open(blurred_resized_file_path)
        bg_w, bg_h = background.size
        offset = (int((bg_w - width) / 2), int((bg_h - height) / 2))

        wallpaper_final_file_path = self.wallpapers_dir + '/wallpaper.jpg'
        background.paste(img, offset)

        if self.picture_name is not None and self.painter_name is not None:
            draw = ImageDraw.Draw(background)
            font_size = 16
            unicode_font = ImageFont.truetype("../Resources/DejaVuSans.ttf", font_size)
            draw.text((100, max_height-120), self.painter_name + '. ' + self.picture_name + '.', font=unicode_font)

        background.save(wallpaper_final_file_path, 'JPEG')
