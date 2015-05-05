from PIL import Image


def Toggle(b_inChar):
    if b_inChar == True:
        return False
    else:
        return True


# im.size[0]==200==column==x
# im.size[1]==50 ==rows==y
def Get_xe(im, pixels, xe):
    #initial value
    b_inChar = False
    for x in range(im.size[0]):
        n_cnt = 0;
        for y in range(im.size[1]):
            n_cnt += 1
            #let's find where character starts
            if (pixels[x, y][2] > 0):
                #if iter looks for a way in a char, do it here.
                if ( b_inChar == False ):
                    b_inChar = Toggle(b_inChar)
                    xe.append(x)
                #if iter hits blue, no matter what it goes back to top
                break
        #It gets here, no blue pixel in this ith column
        if (n_cnt == im.size[1]):
            #So, if it's looking for a way out:
            if b_inChar == True:
                b_inChar = Toggle(b_inChar)
                xe.append(x)
            #if it's looking for a way in:
            elif b_inChar == False:
                #Needs to be taken care of in the 2nd FOR. So,
                pass


class BREAK_2(Exception): pass


def Get_ye(im, pixels, xe, ye):
    for n in range(len(xe) / 2):
        LEFTX = xe[2 * n]
        RIGHTX = xe[2 * n + 1]
        b_inChar = False
        #Top Down Approach!
        try:
            for y in range(im.size[1]):
                for x in range(LEFTX, RIGHTX):
                    if (pixels[x, y][2] > 0):
                        ye.append(y)
                        #break 2
                        raise BREAK_2
        except BREAK_2:
            pass
        #Bottom Up Approach
        try:
            for y in range(im.size[1] - 1, -1, -1):
                for x in range(LEFTX, RIGHTX):
                    if (pixels[x, y][2] > 0):
                        ye.append(y)
                        #break 2
                        raise BREAK_2
        except BREAK_2:
            pass


def CROPPER(im):
    xe = []  #vertical_edges [x0, x1, x2, ... ]
    ye = []  #horizontal_edges [ y0, y1, y2, ... ]
    crList = []
    pixels = im.load()

    #Get x,y Edges in xe, ye lists
    Get_xe(im, pixels, xe)
    Get_ye(im, pixels, xe, ye)

    try:
        for i in range(len(xe) / 2):
            box = (xe[2 * i], ye[2 * i], xe[2 * i + 1], ye[2 * i + 1])
            crList = crList + [im.crop(box)]

        return crList

    except:
        print xe, len(xe)
        print ye, len(ye)
