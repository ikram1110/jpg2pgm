# from PIL import Image
# import os
# import glob
#
# def jpg2pgm(jpg_file, pgm_dir):
#     jpg = Image.open(jpg_file)
#     jpg = jpg.resize((92,112), Image.BILINEAR)
#     name = (str)(os.path.join(pgm_dir, os.path.splitext(os.path.basename(jpg_file))[0])) + ".pgm"
#     jpg.save(name)
#
# for jpg_file in glob.glob('jpg/*.jpg'):
#     jpg2pgm(jpg_file, 'pgm/')

import cv2
import os
import glob

def jpg2pgm(jpg_file, pgm_dir):
    img = cv2.imread(jpg_file, cv2.IMREAD_GRAYSCALE)
    name = (str)(os.path.join(pgm_dir, os.path.splitext(os.path.basename(jpg_file))[0])) + '.pgm'
    cv2.imwrite(name, img, (cv2.IMWRITE_PXM_BINARY, 0))

for jpg_file in glob.glob('jpg/20/*.jpg'):
    jpg2pgm(jpg_file, 'pgm/20/')