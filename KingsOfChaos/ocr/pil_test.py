from PIL import Image
import urllib

im = Image.open('letters/letter1.png', 'r')
pix_val = list(im.getdata())
#print pix_val
o = []
o.append(pix_val)

im2 = Image.open('letters/letter2.png', 'r')
pix_val2 = list(im2.getdata())
#print pix_val2
o.append(pix_val2)

print (pix_val==pix_val2)

print len(o)


#urllib.urlretrieve("http://www.kingsofchaos.com/ads/recruit.img?e0e3d8&uniqid=gb93na2h", "local-filename.jpg")