import urllib2
import Image
#url=http://cafe442.daum.net/_c21_/Captcha.jpg
#cw_outFileName='./crawlerPOOL/Wed Nov 28 22:22:58 2012.png'
def CRAWLER(url, cw_outFileName):
	response = urllib2.urlopen(url)
	f=open( cw_outFileName, "wb")
	f.write( response.read() )
	f.close()
	cw_im = Image.open(cw_outFileName)
	return cw_im
