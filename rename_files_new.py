import cv2
import glob
import os
import numpy as np
import pathlib
import time

# img = cv2.imread("images\\ng 2.jpg")
# cv2.imshow("Image", img)
# cv2.waitKey(0)
#1. Load Dataset

# way 1: 
# path = pathlib.Path().absolute().__str__()
# way 2:
# path = os.path.dirname(__file__) or os.path.abspath(__file__)
# way 3:
# path = pathlib.Path().cwd().__str__()
# way 4:
# path = os.getcwd()
path = os.path.dirname(__file__)

filesImg = []
for ext in ["*.png", "*.jpeg", "*.jpg"]:
  image_file = sorted(glob.glob(path + "\\renamed\\" + ext), key=os.path.getctime)
  filesImg += image_file

i = int(input("Please enter start index: "))
tmp = i
ng = 'img'
# dir = path + "\\data\\img_renamed\\"
dir = path + "\\renamed\\"

for idx in np.arange(len(filesImg)):
   os.rename(filesImg[idx], dir + ng + str(i) + '.png')
   fileTxt = filesImg[idx][:-4] + '.txt'
   os.rename(fileTxt,  dir + ng + str(i) + '.txt')
   i+=1