#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cv2
import os
import numpy as np
from PIL import Image

file_path = os.path.expanduser('~/.wallpaper-rotator-plus/wallpapers') + '/2017_11_20/original.jpg'
#
# img = cv2.imread(file_path)
# # kernel = np.ones((3, 3), np.float32)/10
# #
# # dst = cv2.filter2D(img, -1,kernel)
#
# dst = cv2.blur(img, (150, 150))
#
#
# cv2.imwrite(os.path.expanduser('~/.wallpaper-rotator-plus/wallpapers') + '/2017_11_22/_original.jpg', dst)
#
# img = Image.open(os.path.expanduser('~/.wallpaper-rotator-plus/wallpapers') + '/2017_11_22/_original.jpg')
#
# new_img = img.resize((1920, 1080))
# new_img.save(os.path.expanduser('~/.wallpaper-rotator-plus/wallpapers') + '/2017_11_22/__original', 'JPEG')
#
# img = Image.open(os.path.expanduser('~/.wallpaper-rotator-plus/wallpapers') + '/2017_11_22/original.jpg')
# width, height = img.size
# new_height = 1080
# new_width = new_height * width / height
#
# new_img = img.resize((int(new_width), int(new_height)))
# new_img.save(os.path.expanduser('~/.wallpaper-rotator-plus/wallpapers') + '/2017_11_22/___original', 'JPEG')



img = cv2.imread(file_path)
dst = cv2.blur(img, (150, 150))
cv2.imwrite(os.path.expanduser('~/.wallpaper-rotator-plus/wallpapers') + '/2017_11_20/blured.jpg', dst)

img = Image.open(os.path.expanduser('~/.wallpaper-rotator-plus/wallpapers') + '/2017_11_20/blured.jpg')
new_img = img.resize((1920, 1080))
new_img.save(os.path.expanduser('~/.wallpaper-rotator-plus/wallpapers') + '/2017_11_20/blured_resized.jpg', 'JPEG')


img = Image.open(os.path.expanduser('~/.wallpaper-rotator-plus/wallpapers') + '/2017_11_20/original.jpg', 'r')
img_w, img_h = img.size

background = Image.open(os.path.expanduser('~/.wallpaper-rotator-plus/wallpapers') + '/2017_11_20/blured_resized.jpg')
bg_w, bg_h = background.size
offset = (int((bg_w - img_w) / 2), int((bg_h - img_h) / 2))

background.paste(img, offset)
background.save(os.path.expanduser('~/.wallpaper-rotator-plus/wallpapers') + '/2017_11_20/wallpaper.jpg', 'JPEG')