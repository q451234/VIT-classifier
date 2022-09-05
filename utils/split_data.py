import shutil
import os,random

path = "../data/train/"
for cla in os.listdir(path):
    n = len(os.listdir(path + cla)) * 0.2
    img_list = random.sample(os.listdir(path + cla), int(n))
    for img in img_list:
        # print(img)
        shutil.move(path + cla + "/" + img, "../data/test/" + cla + "/" + img)