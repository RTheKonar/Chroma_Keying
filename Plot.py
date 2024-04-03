import sys
import cv2 as cv
from Chroma import Image
import matplotlib.pyplot as plt
import numpy as np


if len(sys.argv)>1:
	img = Image(cv.imread(sys.argv[1]))
	plt.subplot(2, 2, (1,2))
	plt.hist(img.h,density=True,bins=360)
	plt.title("Hue")
	plt.subplot(2,2,3)
	plt.hist(img.s,density=True,bins=50)
	plt.title("Sat")
	plt.subplot(2,2,4)
	plt.hist(img.v,density=True,bins=50)
	plt.title("Val")

	fig = plt.figure()
	ax = fig.add_subplot(projection='3d')
	hist, xedges, yedges = np.histogram2d(img.h, img.s, bins=50)

	xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
	xpos = xpos.ravel()
	ypos = ypos.ravel()
	zpos = 0

	dx = dy = 0.25 * np.ones_like(zpos)
	dz = hist.ravel()

	ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average')

	plt.show()


	'''cv.imshow("Original",img.rgbData)
	img.chroma(overwrite=True)
	cv.imshow("Edited",img.rgbData)
	cv.waitKey(0)
	cv.destroyAllWindows()'''