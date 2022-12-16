import cv2
import os

# write your output name in below:
outputFileName = 'Myoutput.mp4'

if os.path.isfile(outputFileName):
    raise ValueError('This output filename already exists, please change the filename!')
else:

    # Camera Ip Address
    # The below rtsp link is for Dahua ip-camera. you should find your camera's rtsp-link.
    cameraCapture = cv2.VideoCapture("rtsp://username:password@camera_IP:rtsp_port/cam/realmonitor?channel=1&subtype=1")
    # frame rate or frames per second
    fps = 15

    # Width and height of the frames in the video stream
    size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    """Create a VideoWriter object. We should specify the output file name (eg: MyOutput.mp4). Then we should specify 
    the FourCC. Then number of frames per second (fps) and frame size should be passed. May specify isColor flag. If 
    it is True, encoder expect color frame, otherwise it works with grayscale frame. FourCC is a 4-byte code used to 
    specify the video codec. The list of available codes can be found in fourcc.org. It is platform dependent. """

    videoWriter = cv2.VideoWriter(outputFileName,
                                  cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps, size)

    success, frame = cameraCapture.read()

    # Press q to exit streaming
    while True:
        videoWriter.write(frame)
        success, frame = cameraCapture.read()
        cv2.imshow('frame', cv2.resize(frame, (1280, 720)))
        # Press Q on keyboard to stop recording
        key = cv2.waitKey(1)
        if key == ord('q'):
            cameraCapture.release()
            cv2.destroyAllWindows()
            exit(1)
