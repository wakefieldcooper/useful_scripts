import sys
import argparse
import cv2
import os


# path_in_real = 'C:/Users/enqui/AppData/Local/Programs/Python/Python36/Thesis/New Dataset/combined.mp4'
# path_out_real_training = 'C:/Users/enqui/AppData/Local/Programs/Python/Python36/Thesis/New Dataset/real/training'
# path_out_real_test = 'C:/Users/enqui/AppData/Local/Programs/Python/Python36/Thesis/New Dataset/real/test'
path_in_fake = 'C:/Users/enqui/AppData/Local/Programs/Python/Python36/Thesis/IMG_1780.MOV'
path_out_fake_training = 'C:/Users/enqui/AppData/Local/Programs/Python/Python36/Thesis/tomove/fake'
path_out_fake_test = 'C:/Users/enqui/AppData/Local/Programs/Python/Python36/Thesis/New Dataset/test/fake'


vidcap_real = cv2.VideoCapture(path_in_fake)
success, image = vidcap_real.read()
count = 0
success = True
video_length = int(vidcap_real.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
print("Number of frames: ", video_length)


print("Converting the video...\n")
while success:
    while count <= video_length:
        sucess, image = vidcap_real.read()
        if not success:
            break
        cv2.imwrite(os.path.join(path_out_fake_training, "frame{:d}.jpg".format(count)), image)
        count += 1
        if count % 1000 == 0:
            print("Still converting...\n")
    # print("Starting on validation set")
    # while count > 0.8*video_length and count < video_length:
    #     sucess, image = vidcap_real.read()
    #     if not success:
    #         break
    #     cv2.imwrite(os.path.join(path_out_fake_test, "frame{:d}.jpg".format(count)), image)
    #     count += 1
    #     if count % 1000 == 0:
    #         print("Still converting...\n")

    print("Completed")
    break
