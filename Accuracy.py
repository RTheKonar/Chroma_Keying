import cv2 as cv
import sys
import matplotlib.pyplot as plt

#def isEqual(list1,list2)

def Compare(Result, Desired, Original, Background=None):
	x= len(Result)
	y= len(Result[0])
	n=x*y
	erased=0
	mismatch=0
	undershoot=0

	for i in range(x):
		for j in range(y):
			if all(Original[i][j] != Result[i][j]):
				erased+=1
			if all(Result[i][j] != Desired[i][j]):
				mismatch+= 1
				if all(Original[i][j]== Result[i][j]):
					undershoot+= 1	
	
	overshoot= mismatch - undershoot
	print("Dimensions: \t\t\t\t\t",x,"x",y)
	print("Number of pixels in image:\t\t\t",n)
	print("Number of pixels Erased: \t\t\t",erased,"\t({:.2f}%)".format(erased/(n)*100))
	print("Number of mismatch: \t\t\t\t",mismatch,"\t({:.2f}%)".format(mismatch/n*100))
	print("Number of background pixels not removed: \t",undershoot,"\t({:.2f}%)".format(undershoot/mismatch*100))
	print("Number of foreground pixels removed: \t\t",overshoot,"\t\t({:.2f}%)".format(overshoot/mismatch*100))
	print("Accuracy:\t\t\t\t\t",str((1-mismatch/n)*100)+"%")

if(len(sys.argv)>1):
	Result= cv.imread(sys.argv[1])
	Desired= cv.imread(sys.argv[2])
	Original= cv.imread(sys.argv[3])
	Compare(Result, Desired, Original)