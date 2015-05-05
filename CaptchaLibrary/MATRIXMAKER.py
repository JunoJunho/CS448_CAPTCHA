from PIL import Image

def MATRIXMAKER(imList):
	X = ''
	for im in imList:
		pixels = im.load()
		for i in range(im.size[0]):
			for j in range(im.size[1]):
				X = X + ' %s' % str(pixels[i,j])
		X = X + '\n'
	return X
