#import libraries
import random
import shutil
import os
import glob
import math
import numpy as np

basepath = os.path.dirname(__file__)
filesImgPath = basepath + "\\datasets\\train\\images\\"
filesLabelPath = basepath + "\\datasets\\train\\labels\\"

filesImg = []
for ext in ["*.png", "*.jpeg", "*.jpg"]:
  image_files = glob.glob(filesImgPath + ext)
  filesImg += image_files

nb_val = math.floor(len(filesImg)*0.2)
rand_idx = np.random.randint(0, len(filesImg), nb_val)
nb_test = math.floor(len(filesImg)*0.1)
rand_idx_test = np.random.randint(0, len(filesImg), nb_test)

for idx in np.arange(len(filesImg)):
   if(idx in rand_idx):
      index = filesImg[idx].__str__().rfind('\\')
      fileLabel = filesImg[idx][index + 1:-3] + "txt"
      srcLabelPath = filesLabelPath + fileLabel
      shutil.copy(filesImg[idx], basepath + "\\datasets\\valid\\images\\")
      shutil.copy(srcLabelPath, basepath + "\\datasets\\valid\\labels\\")

for idx in np.arange(len(filesImg)):
   if(idx in rand_idx_test):
      index = filesImg[idx].__str__().rfind('\\')
      fileTest = filesImg[idx][index + 1:-3] + 'txt'
      srcTestPath = filesLabelPath + fileTest
      shutil.copy(filesImg[idx], basepath + "\\datasets\\test\\images\\")
      shutil.copy(srcTestPath, basepath + "\\datasets\\test\\labels\\")


# shutil.copy(os.path.join(os.path.join(basepath, folder), img), os.path.join("Testing", img))