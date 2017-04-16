import cv2
import numpy as np
import sys


def compute_barcode(input_file, output_file, frame_skip, mode):
    vidcap = cv2.VideoCapture(input_file)

    print "Processing video file %s. This may take a while depending on the size of the video or the system performance..." % (input_file)

    frame_count = 0
    success = True
    barcode = None

    while success:
        success, image = vidcap.read()
        # process frames
        if frame_count % frame_skip == 0:
            if success:
                if mode == 0:
                    resized_image = cv2.resize(image, (1, 600))
                elif mode == 1:
                    average_color_per_row = np.average(image, axis=0)
                    average_color = np.average(average_color_per_row, axis=0)
                    resized_image = np.array([[average_color]*1]*600, np.uint8)
            if barcode is None:
                barcode = resized_image
            else:
                barcode = np.hstack((barcode, resized_image))
        frame_count += 1

    # save to file
    cv2.imwrite(output_file, barcode)
    print "Processing complete! Barcode image saved in %s" % (output_file)


if __name__ == '__main__':
    input_file = "input.mp4"   # CHANGE ME
    output_file = "output.jpg" # CHANGE ME
    # SAMPLING MODE:
    # 0 - shrink frame to a width of 1; 
    # 1 - fill the bar with the average color of the frame 
    sampling_mode = 1;
    # SAMPLE RATE: 
    # one bar every 50 frames, 
    frame_skip = 50  

    compute_barcode(input_file, output_file, frame_skip, sampling_mode)
