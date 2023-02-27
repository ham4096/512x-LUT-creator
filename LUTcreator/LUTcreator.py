import cv2
import numpy as np
if argv[0] is not "":
    filename = input("Filename of file with 512x512 LUT in top left corner: ")
else:
    filename = argv[0]
    print("Now working on file '"+ filename + "'.")
#read image
img = cv2.imread(filename)
#create a new array to represent final
final = np.zeros((64, 4096, 3), np.uint8)
#8 rows per LUT
for i in range(8):
    #copy values over from each section
    for x in range(0, 64):
        for y in range(0, 512):
            final[x][y+(i*512)][0] = img[x+(i*64)][y][0]
            final[x][y+(i*512)][1] = img[x+(i*64)][y][1]
            final[x][y+(i*512)][2] = img[x+(i*64)][y][2]

print("4096 x 64 LUT created as 'FinalLUT.png'!")
cv2.imwrite('FinalLUT.png', final)

