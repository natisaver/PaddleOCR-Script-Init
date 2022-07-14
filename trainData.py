import os
import sys
import glob
import json
from PIL import Image
import random

# change to directory of the script
os.chdir(sys.path[0])

# image file types allowed
endings = ['.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif']

# get the script parent path
script_path = sys.path[0]

# create train directory
create_train_path = os.path.join(script_path, "rec_gt_train")
filepath = os.path.join(create_train_path, "rec_gt_train.txt")
if not os.path.exists(create_train_path):
    os.mkdir(create_train_path)
    print("train folder created")      
    with open(filepath, 'w') as f1:
        f1.write("")
    print("train txt created")

# create validation directory
create_valid_path = os.path.join(script_path, "rec_gt_valid")
filepath2 = os.path.join(create_valid_path, "rec_gt_valid.txt")
if not os.path.exists(create_valid_path):
    os.mkdir(create_valid_path)
    print("valid folder created")     
    with open(filepath2, 'w') as f2:
        f2.write("")
    print("valid txt created")   

# for each image i
for ends in endings:
    with open(filepath2, 'a') as f2:
        with open(filepath, 'a') as f1:
            for i in glob.glob('*'+ends):
                file_name = os.path.splitext(i)[0]
                
                # validation set
                with open(file_name+".json", "r") as g:
                    data = json.load(g)
                if random.random() < 0.3:
                    for idx, row in enumerate(data):
                    #     im = Image.open(i)
                    #     cropped = im.crop(row['box'])
                    #     cropped.save(f"{create_valid_path}/{file_name}_{idx}{ends}")
                        f2.write(f"{create_valid_path}/{file_name}_{idx}{ends}" + '\t' + row['text']+'\n')
                
                # training set
                else:
                    for idx, row in enumerate(data):
                        # im = Image.open(i)
                        # cropped = im.crop(row['box'])
                        # cropped.save(f"{create_train_path}/{file_name}_{idx}{ends}")
                        f1.write(f"{create_valid_path}/{file_name}_{idx}{ends}" + '\t' + row['text']+'\n')





 