import cv2
import numpy as np
from sys import argv
import os
'''
This function flattens a LUT into a 64 x 4096 LUT.
@ final: The final image that we are manipulating for our output
@ img: imported image that is being turned into a 64 x 4096 LUT
@ k: counter in the image. If we have no counter, this is set to a default of 0.
'''
def flattenlut(final, img, k = 0):
    
    #8 rows per LUT
    for i in range(8):
    #copy values over from each section
    #note that numpy row/column values are reversed in comparison to a normal matrix (i, e, [vertical][horizontal])
        for y in range(0, 64):
            for x in range(0, 512):
                final[y+(k*64)][x+(i*512)][0] = img[y+(i*64)][x][0]
                final[y+(k*64)][x+(i*512)][1] = img[y+(i*64)][x][1]
                final[y+(k*64)][x+(i*512)][2] = img[y+(i*64)][x][2]

'''
This function adds an already 64 x 4096 LUT to a mutliLUT
@ final: The final image that we are manipulating for our output
@ img: imported image that is being turned into a 64 x 4096 LUT
@ k: counter in the image. If we have no counter, this is set to a default of 0.
'''
def addlut(final, img, k = 0):
    #copies the LUT completely to the final multiLUT
    #note that numpy row/column values are reversed in comparison to a normal matrix (i, e, [vertical][horizontal])
    for y in range(0, 64):
        for x in range(0, 4096):
             final[y+(k*64)][x][0] = img[y][x][0]
             final[y+(k*64)][x][1] = img[y][x][1]
             final[y+(k*64)][x][2] = img[y][x][2]

files = []
    #check if a file was passed to the LUT
if len(argv) > 1:
    filename = input("Filename of file with 512x512 LUT in top left corner: "+ argv[1])
    filename = argv[1]
else:
    choice = input("Choices\n1: Batch process multiple LUTs/512 x 512 LUTs into a single LUT\n2: Turn a 512x512 LUT into a single 64x4096 LUT\n")
    if choice == '1':
        while True:
            dirname = input("Directory of files with LUTs in them: ")
            #check for valid paths
            if os.path.isdir(dirname) == True:
                break
            else:
                print("Incorrect directory name! Try again.")
        #since our path is valid, append the file names of the files in the folder
        for entry in os.scandir(dirname):
            files.append(entry.path)
    else:
        while True:
            filename = input("Filename of .png file with 512x512 LUT in top left corner: ")
            if os.path.isfile(filename) == True:
                #since our file is valid, append our file to the list
                files.append(filename)
                break   
            else:
                print("Incorrect file name! Try again.")
        
#read image
final = np.zeros((64*len(files), 4096, 3), np.uint8)
for imgnum in range(len(files)):
    img = cv2.imread(files[imgnum])
    #grab the height and width of the current image to check if it's already a LUT
    height, width = img.shape[:2]
    if height == 64 and width == 4096:
        addlut(final, img, imgnum)
    else:
        flattenlut(final, img, imgnum)



print("LUT created as 'FinalLUT.png'!")
cv2.imwrite('FinalLUT.png', final)

