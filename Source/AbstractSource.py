import datetime
import os
import requests


class AbstractSource(object):
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

    def get_image_url(self):
        raise NotImplementedError("Override this method please")
