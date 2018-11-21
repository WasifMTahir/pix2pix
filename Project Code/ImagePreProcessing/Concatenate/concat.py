import sys
import numpy as np
from PIL import Image

total_frames = 4

total_frames += 1

for i in range(1,total_frames):
	image_guy = 'Images\\' + str(i) + '.png'
	image_stick = 'Sticks\\' + str(i) + '.png'
	image_final = 'Concat\\' + str(i) + '.jpg'
	list_im = [image_guy, image_stick]
	imgs    = [ Image.open(i) for i in list_im ]
	imgs_new = []
	# coords = (180, 0, 450, 360)
	# for i in imgs:
	# 	imgs_new.append(i.crop(coords))
	# imgs = imgs_new
	# pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
	min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
	imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )

	# save that beautiful picture
	imgs_comb = Image.fromarray(imgs_comb)
	imgs_comb.save( image_final )
	
	# images = map(Image.open, [image_guy, image_stick])
	# widths, heights = zip(*(i.size for i in images))

	# total_width = sum(widths)
	# max_height = max(heights)

	# new_im = Image.new('RGB', (total_width, max_height))

	# x_offset = 0
	# for im in images:
	#   new_im.paste(im, (x_offset,0))
	#   x_offset += im.size[0]

	# new_im.save(image_final)