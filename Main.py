import sys
import cv2 as cv
from Chroma import Image

if len(sys.argv)>1:
	commands= sys.argv.copy()
	img = Image(cv.imread(commands[1]))
	cv.imshow("Original",img.rgbData)
	if "Details" in commands:
		details= True
		commands.remove("Details")
	else:
		details= False
	if "Save" in commands:
		save= True
		commands.remove("Save")
	else:
		save= False
	if "Replace" in commands:
		bg= cv.imread(commands[commands.index("Replace")+1])
		img.chroma(bg=bg)
	elif len(commands) == 5:
		img.chroma(col=[commands[4],commands[3],commands[2]])
	else:
		img.chroma()
	if details:
		img.details()
	if save:
		cv.imwrite("Edited.png",img.rgbData)
	cv.imshow("Edited",img.rgbData)
	cv.waitKey(0)
	cv.destroyAllWindows()
