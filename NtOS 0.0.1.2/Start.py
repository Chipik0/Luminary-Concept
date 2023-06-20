import cv2
import os
from time import sleep, time
from win32api import GetSystemMetrics
from threading import Thread
import sys
from zipfile import ZipFile
import numpy as np
from shutil import copyfile
import  filecmp
from PIL import Image

#---Articles--------------------------------------------------#|                  
XM=GetSystemMetrics(0)                                                   #|
YM=GetSystemMetrics(1)                                                    #|                        
#---------------------------------------------------------------#|

start_time = time()

zip_file = 'source.zip'
password = 'commandOrfoCompany10293811'

dirname = os.path.dirname(__file__)
os.chdir(dirname)

vir=os.path.exists('Cache/virus.txt')
if vir:
    with ZipFile(zip_file) as zf:
        zf.extractall(pwd=password.encode(), path=str(''))
        zf.close()

st=os.path.exists('Cache/notone.txt')
wallcheck=filecmp.cmp('Media/Images/backunBlur.png', 'Cache/backunBlur2.png')

if st==False or not wallcheck:
    def img3():
        image = cv2.imread('Media/Images/backunBlur.png')
        height, width, _ = image.shape
        scale_x = XM / width
        scale_y = YM / height
        scale = max(scale_x, scale_y)
        scaled_image = cv2.resize(image, None, fx=scale, fy=scale)
        cv2.imwrite('Cache/backunBlur.png', scaled_image)
        img=cv2.GaussianBlur(image, (121, 121), 99)
        cv2.imwrite('Cache/blurscreen.png', img)
        copyfile('Cache/backunBlur.png', 'Cache/backunBlur2.png')


    #-------------------------------------------------------------------------


    def colorday_():
        def get_popular_color(image_path):
            image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            pixels = image.reshape(-1, 3)
            color_counts = np.bincount(pixels[:, 0] * 65536 + pixels[:, 1] * 256 + pixels[:, 2])
            popular_color_index = np.argmax(color_counts)
            r = popular_color_index // 65536
            g = (popular_color_index % 65536) // 256
            b = popular_color_index % 256
            return (r, g, b)


        color=get_popular_color('Media/Images/backunBlur.png')
        if color==(255, 255, 255):
            color=(10,10,10)
        elif color==(0,0,0):
            color=(10,10,10)


        colortxt=open('Media/color.txt', 'w+')
        colortxt.write(str(color))
        colortxt.close()


        def replace_color(image, target_color, replacement_color):
            image2 = cv2.imread(image)
            fill_color = replacement_color
            fill_color_array = np.zeros_like(image2)
            fill_color_array[:] = fill_color
            filled_image = np.where(image2 != 0, fill_color_array, image2)
            return filled_image
        

        target_color = (255, 255, 255)
        replacement_color = color
        img=replace_color('Media/Images/materialBar.png', target_color, replacement_color)
        cv2.imwrite('Media/Images/barMaterialU.png', img)
        def convertImage():
            img = Image.open("Media/Images/barMaterialU.png")
            img = img.convert("RGBA")
            datas = img.getdata()
            newData = []
            for item in datas:
                if item[0] == 0 and item[1] == 0 and item[2] == 0:
                    newData.append((255, 255, 255, 0))
                else:
                    newData.append(item)
            img.putdata(newData)
            img.save("Media/Images/barMaterialU.png", "PNG")

    threads = [
        Thread(target = img3),
        Thread(target = colorday_),
    ]
    while True:
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        done=open('Cache/notone.txt', 'w')
        done.close()
        print("--- %s seconds ---" % (time() - start_time))
        os.startfile('source.py')
        sys.exit()
else:
    os.startfile('source.py')
    sys.exit()
