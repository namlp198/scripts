import cv2
import glob
import os
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
  image_file = sorted(glob.glob(path + "\\data\\data_new\\" + ext), key=os.path.getctime)
  filesImg += image_file

filesTxt = []
for ext in ["*.txt"]:
  txt_file = sorted(glob.glob(path + "\\data\\data_new\\" + ext), key=os.path.getctime)
  filesTxt += txt_file

i = int(input("Please enter start index: "))
tmp = i
ng = 'img'
# dir = path + "\\data\\img_renamed\\"
dir = path + "\\data\\data_new\\"

for filename in filesImg:
    os.rename(filename, dir + ng + str(i) + '.png')
    i+=1
time.sleep(5)
i = tmp
for filename in filesTxt:
    os.rename(filename, dir + ng + str(i) + '.txt')
    i+=1
