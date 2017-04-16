Originally created by Jyotiska Khasnabish. Changed by me.

# movie-barcode

This python script can create a barcode given a movie or a video file. [Example](http://i.imgur.com/Xjhqn3s.jpg).

## Usage


The following parameters can be changed in source:

1. input_file - Name of the video file you want to transform into a barcode

2. output_file - Default output file is named "output.jpg" and can be changed. 

3. frame_skip - This parameter sets how many frames should be skipped between each target frame used to create to the barcode image. Default value is 50 and this should be changed to higher value for longer videos. Ideal value is 90 for a 2 hour long video.

4. sample_mode - In default mode (0) each bar is a frame that has been shrunk to a one unit wide rectangle. In mode 1 the color of the bar is the average color of all the pixels in the frame.  
