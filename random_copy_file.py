#import libraries
import random
import shutil
import os

basepath = os.path.dirname(__file__)
# Creating a Training and Testing folders
os.makedirs('Training')
os.makedirs('Testing')

folders=os.listdir(basepath)

for folder in folders: # loop over the 257 folders
   contents = os.listdir(os.path.join(basepath, folder)) 
   random.shuffle(contents)  # shuffle the result
   split_point = round(0.8* len(contents))
   for img in contents[:split_point]:
       shutil.copy(os.path.join(os.path.join(basepath, folder), img), os.path.join("Training", img))
   for img in contents[split_point:]:
       shutil.copy(os.path.join(os.path.join(basepath, folder), img), os.path.join("Testing", img))