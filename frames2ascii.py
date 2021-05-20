from image2ascii import image2ascii
import os

# path joining version for other paths
DIR = 'frame'
img_cnt = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
imgStream = ""

for i in range(img_cnt):
    # strong lag
    print(image2ascii(os.path.join(DIR, str(i)+'.jpg'), 200, False))