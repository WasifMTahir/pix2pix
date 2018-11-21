import cv2
import os

image_folder = 'Images'
video_name = 'video.avi'
img_type = ".jpg"

images = [img for img in os.listdir(image_folder) if img.endswith(img_type)]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, -1, 10, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()