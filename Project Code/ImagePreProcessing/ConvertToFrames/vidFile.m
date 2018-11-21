movFiles = dir('*.mp4'); 
numFiles = length(movFiles);

for i = 1:2
    workingDir = pwd;
    %mkdir(workingDir,erase(num2str(movFiles(i).name),'.mp4'));
    myVid = VideoReader(movFiles(i).name);
    count = 1;
    while hasFrame(myVid)
       img = readFrame(myVid);
       img = imrotate( img , -90 );
       filename = strcat(num2str(count), '.jpg'); %[sprintf('%03d',count) '.jpg'];
       fullname = fullfile(pwd,filename);
       imwrite(img,fullname)
       count = count+1;
    end
end

% name = 'video.mp4';
% myVid1 = VideoReader(name);
% myVid1.VideoFormat
% img1 = readFrame(myVid1);
% temp = img1(1:300, 1:300, 1:3);
% image(temp)
