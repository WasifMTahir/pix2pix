# pix2pix
Stick Figure to Human Body Generation using pix2pix
***********Step 0***********
MATLAB R2016a must be installed.
Python must be installed.
Pip must be installed.
Following libraries must be installed in python, using the following commands:
1) pip install pillow
2) pip install numpy
3) pip install opencv-python

# ***********Step 1***********
Open Folder "Project Code" and then go to "ImagePreProcessing" folder. All future references up till "Step 8" are to folders and files within the "ImagePreProcessing" folder.

# ***********Step 2***********
Go to the folder "ConvertToFrames".
Delete any previous images or video in the folder.
Paste video file in mp4 format with name "video.mp4".
Open and run the vidFile.m MatLab file.
This will generate a number of frames in the folder. Look at the last image with the highest number to get the frame count.

# ***********Step 3***********
In folder "ConvertToFrames", open "fixImg.py" and enter the frame count into total_Frames variable value
Run "fixImg.py"
This will set the images to the appropriate size.

# ***********Step 4***********
In folder "CreateWhites", delete all current images.
Open "create.py" and enter the frame count into total_Frames variable value
Run "create.py"
This will generate a number of white images in the folder.

# ***********Step 5***********
You can find the folder "OpenPose" in the Google Drive Link provided in the text file "OpenPoseLink.txt" in the "ImagePreProcessing" folder. Download this folder.
In folder "OpenPose", go to folder "PoseGen", and delete all images in the following folders: "Inputs", "Outputs_KeyPoints", "Outputs_Skeleton" and "Outputs_Sticks"
Copy all images in the "ConvertToFrames" folder into "OpenPose\PoseGen\Inputs" folder.
Open "OpenPoseImage.py" and enter the frame count into total_Frames variable value
Run "OpenPoseImage.py"
This will generate the relevant skeletons in the "Outputs_Sticks" folder. It should take approx 7 sec/frame.

# ***********Step 6***********
In folder "Concatenate", go to folder "Sticks". Delete all current images.
Then, copy all images in the folder "OpenPose\PoseGen\Outputs_Sticks", and paste them into this.

# ***********Step 7***********
In folder "Concatenate", go to folder "Images". Delete all current images.
Then, copy all images in the folder "CreateWhites", and paste them into this.

# ***********Step 8***********
In folder "Concatenate\Concat" delete all current images.
Now, open "concat.py" and enter the frame count into total_Frames variable value
Then run "concat.py"
This will generate the relevant images in the "Concat" folder.
These are the images you will use as input.

# ***********Step 9************
Run pix2pix.ipynb
Replace the variables imgdir, traindir, testdir according ti your own image directories


# ***********Step 10***********
Now, go to folder "New Video".
Delete all images in the folder "Images". Paste the resulting images.
Open the code "createMovie.py" and set change the image_type variable to the type of images that you just pasted into the folder "Images".
Run the code "createMovie.py".
Click "OK" in the menu which pops up.
A new file by the name "video.avi" will be created. Run this in a software capable of running .avi files, like VLC Player or Windows Media Player (NOT the default "Movies and TV" software for Windows)
This will be the new video of the indian performing the same poses.
