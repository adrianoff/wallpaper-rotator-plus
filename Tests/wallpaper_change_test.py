#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import subprocess
import sys

pl = sys.platform
file_path = os.path.expanduser('~/.wallpaper-rotator-plus/wallpapers') + '/2017_11_20/original.jpg'

command = ''.join(['gsettings set org.gnome.desktop.background picture-options centered picture-uri file://', file_path])
os.system(command)

#
# command = "gconftool-2 --set \
#         /desktop/gnome/background/picture_filename \
#         --type string '%s'" % file_path
#
# subprocess.Popen(command, shell=True)
