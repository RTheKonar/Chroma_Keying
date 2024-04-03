README File

Programming Language Used - Python3
External Libraries Used - OpenCV, Statistics, NumPy, Matplotlib
Note: OpenCV contains project specific functions, but we have used only functions to read, write and display images.

__________________________________________________________________

Program Files

1. Chroma.py - File containing the program for chroma keying. To be used as a library file.
2. Main.py - Remove the background of any image given by the user.
3. Plot.py - Makes the statistical plots for exploratory data analysis.
4. Accuracy.py - Measures the Accuracy of the background removal by comparing it with an online converter.
___________________________________________________________________

Directories Data/

1. Original - Original Images before editing
2. Edited - Images after background Removal using our program
3. Desired - Images after background Removal from the online software
4. Plots - Statistical Plots
5. Bg - Images where background is replaced by a different background
___________________________________________________________________

Instructions

Step 1: For all these programs, Python interpreter needs to be installed and set in environment variables. Open command prompt in the folder containing all the programs then type the following commands.

Step 2: Library OpenCV(Open Computer Vision) and Statistics are required. If they are not installed install them before using any of the programs.

>pip install opencv-python
>pip install statistics

Step 3: 

Use Main.py to remove or replace background.

Remove(white) background - >python Main.py <filename> 
Desired color background - >python Main.py <filename> <r> <g> <b>
Desired image background - >python Main.py <filename> Replace <background>

To get details of the process, add Details after the last command

To save the result, use Save command before hitting enter or run without save and click Ctrl + S on the image produced in the screen

As an example start by typing

>python Main.py Data/Original/Data1.jpg Details Save

To replace by another background type

>python Main.py Data/Original/Data1.jpg Replace Data/Original/Bg1.jpg Details Save

The Details and Save are optional arguments, they can be ommitted.

Now you can place any image(jpg, jpeg, png, bmp, webp, tiff, etc) in this directory and repeat the commands with appropriate changes.

Use Plot.py to plot the histograms.

>python Plot.py <filename>

This plots histograms of Hue, Sat, Val and 2D Histogram of Hue, Sat to show the cluster formed.

Use Accuracy.py to measure the accuracy of our program

First download the background removed image from any source that you believe gives most accurate image. Make sure the dimensions are same as the original image. We have used RemoveBg for our project.

>python Accuracy.py <our program> <desired> <original>  

Example - 

>python Accuracy.py Data/Edited/Data1_Edited.png Data/Desired/Data1_Accurate.png Data/Original/Data1.jpg
___________________________________________________________________

The Internal Documentation of the program is in Doc.txt
