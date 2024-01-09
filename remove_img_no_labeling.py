import shutil
import os
import glob
import math
import numpy as np

basepath = os.path.dirname(__file__)

filesImg = []
for ext in ["*.png", "*.jpeg", "*.jpg"]:
  image_files = glob.glob(basepath + '\\' + ext)
  filesImg += image_files

for idx in np.arange(len(filesImg)):
  index = filesImg[idx].__str__().rfind('\\')
  nameFile = filesImg[idx][index + 1:-3] + 'txt'
  pathLabel = basepath + '\\' + nameFile
  if not os.path.exists(pathLabel):
    os.remove(filesImg[idx])