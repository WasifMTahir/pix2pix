from PIL import Image

total_frames = 44

total_frames += 1

for i in range(1,total_frames):
	img = Image.new('RGB', (270, 360), color = 'white')
	img.save(str(i) + '.png')
	# image_guy = image_path + str(i) + '.jpg'
	# im1 = Image.open(image_guy)
	# im2 = im1.resize((270, 360), Image.ANTIALIAS)
	# im2.save(str(i) + '.jpg')