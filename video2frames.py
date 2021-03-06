import cv2
import os

def video_to_frames(video, path_output_dir):
    # extract frames from a video and save to directory as 'x.png' where 
    # x is the frame index
    vidcap = cv2.VideoCapture(video)
    count = 0
    while vidcap.isOpened():
        success, image = vidcap.read()
        if success:
            cv2.imwrite(os.path.join(path_output_dir, '%d.jpg') % count, image)
            count += 1
        else:
            break
    cv2.destroyAllWindows()
    vidcap.release()


if os.path.exists('frame'):
    video_to_frames('youtube\青蛙撞奶.mp4', 'frame')
else:
    os.mkdir('frame')
    video_to_frames('youtube\青蛙撞奶.mp4', 'frame')
