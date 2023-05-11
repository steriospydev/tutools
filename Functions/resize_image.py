from PIL import Image
"""
  Requirements:
    pillow
"""

imgs = ['exam.jpg']

def convert_to(img:str, basewidth: int) -> None:	
	image = Image.open(img)
	wper = (basewidth / float(image.size[0]))
	hsize = int((float(image.size[1]) * float(wper)))
	new = image.resize((basewidth, hsize), Image.ANTIALIAS)
	new.save(f'{img}x{basewidth}.jpg')
