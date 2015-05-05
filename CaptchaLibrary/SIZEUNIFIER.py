from PIL import Image
def SIZEUNIFIER(imList, xNew, yNew):
	suList = []
	for imOld in imList:
		imNew = Image.new('L',(xNew, yNew), 255)
		xOld, yOld = imOld.size
		imOld.copy()
		xOff = (xNew-xOld)/2
		yOff = (yNew-yOld)/2
		box = (xOff, yOff, xOff+xOld, yOff+yOld)
		imNew.paste(imOld, box)
		suList = suList + [ imNew ]
	return suList
