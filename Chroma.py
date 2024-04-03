from statistics import mode

# Converts a color from RGB to HSV.
def hsv(col):
    r=int(col[2])
    g=int(col[1])
    b=int(col[0])
    Cmax = max(r,g,b)
    Cmin = min(r,g,b)
    d= Cmax-Cmin

    if d==0:
        H=0
    elif Cmax==r:
        H= 60 * (((g-b)/d)%6)
    elif Cmax==g:
        H= 60 * (((b-r)/d + 2)%6)
    else:
        H= 60 * (((r-g)/d + 4)%6)

    if Cmax==0:
        S=0
    else:
        S= d/Cmax

    V= Cmax/255
    return [H,S,V]

class Image:
    def __init__(self,data):
        self.rgbData= data
        self.dimensions()
        self.toHSV()
        self.components()
        self.centre()

    def dimensions(self):
        self.x= len(self.rgbData)
        self.y= len(self.rgbData[0])

    def toHSV(self):
        self.hsvData= [[hsv(self.rgbData[i][j]) for j in range(self.y)] for i in range(self.x)]

    def components(self):
        self.h= [self.hsvData[i][j][0] for i in range(self.x) for j in range(self.y)]
        self.s= [self.hsvData[i][j][1] for i in range(self.x) for j in range(self.y)]
        self.v= [self.hsvData[i][j][2] for i in range(self.x) for j in range(self.y)]

    def centre(self):
        self.ch= mode(self.h)
        self.cs= mode(self.s)
        self.cv= mode(self.v)

    def details(self):
        print("Dimensions: \t\t\t",self.y,"x",self.x)
        print("Modal values of H, S, V: \t", self.ch, self.cs, self.cv)

    def similar(self,col):
        return abs(self.ch - col[0])<25 and abs(self.cs - col[1])<0.8 and abs(self.cv - col[2]) < 0.35 

    def chroma(self,bg=None,col=None,overwrite=True):
        if not overwrite:
            buffer=img.copy()
        if (bg is None) and not col:
            col=[255,255,255]
        for i in range(self.x):
            for j in range(self.y):
                if self.similar(self.hsvData[i][j]):
                    if overwrite:
                        if bg is not None:
                            self.rgbData[i][j]=bg[i][j]
                        else:
                            self.rgbData[i][j]=col
                    else:
                        if bg:
                            buffer[i][j]=bg[i][j]
                        else:
                            buffer[i][j]=col
        if not overwrite:
            return buffer
