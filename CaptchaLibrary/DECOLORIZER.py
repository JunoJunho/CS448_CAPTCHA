from PIL import Image
from PIL import ImageOps

#dc_im_List = DC(cr_im_List)
#usage : PNG2grayBMP.PNG2grayBMP('','')
def DECOLORIZER(imList):
	dcList = []
	for im in imList:
		im = im.convert('RGB')
		pixels = im.load()

		#bg color - from Black to White
		for i in range(im.size[0]):
			for j in range(im.size[1]):
				if pixels[i,j]==(0,0,0):
					pixels[i,j] = (255,255,255)
		#pdb.set_trace()
		#set grayscale
		dcList = dcList + [ ImageOps.grayscale(im) ]

	return dcList
