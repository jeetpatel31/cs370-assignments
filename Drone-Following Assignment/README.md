Name of the assignment : Drone-Following Assignment

================================================

Date of submission : 04/03/2024

================================================

Instructions on how to run the code :

## Object Detection:

To run this code, ensure you have Python installed on your system with the necessary libraries: OpenCV for handling video and image operations, and FilterPy for implementing the Kalman Filter. Install these libraries by running pip install opencv-python filterpy in your command line. Save the code into a file, let's say tracker.py, and make sure you have the video file it references, Cyclist and vehicle Tracking - 2.mp4, in the same directory or adjust the video_path variable to point to its location. Run the script by opening a terminal, navigating to the directory containing your script, and executing python tracker.py. The script initiates video playback, This setup is designed to demonstrate object tracking in a video using Kalman Filters, offering a practical glimpse into computer vision applications. This is the little sample demo.


https://github.com/jeetpatel31/cs370-assignments/assets/96985261/3c45f36e-9e11-4e9c-8ec7-869a1e766780


https://github.com/jeetpatel31/cs370-assignments/assets/96985261/2648378f-d9f3-4c15-904f-971f16c97c2b


https://github.com/jeetpatel31/cs370-assignments/assets/96985261/07cb07a1-b02e-4b16-b64c-500bf6279213

## Kalman Filter:

Same thing as before make sure all the libraries are up to date and installed. You'll also need the YOLO configuration files (yolov3.cfg), weights (yolov3.weights), and the class labels (coco.names), placed in the same directory as your script or adjust the paths in the code to where you've stored them. Make sure the video file you want to track objects in, noted as "Cyclist and vehicle tracking - 1.mp4" in the code, is accessible and correctly named in the script. Run the script, the video will play, selections will be tracked throughout the video, displaying their paths with lines. Press 'q' to exit the video playback. This is a little sample demo.

https://github.com/jeetpatel31/cs370-assignments/assets/96985261/e8e67872-4dd1-4cc2-9548-000decb285c2

## Extra Bonus:

Place the YOLO configuration file yolov3.cfg and the weight file yolov3.weights in the same directory as your script, or adjust the file paths in the load_model function accordingly. The same goes for the video file, here named extra.mp4. Once everything is set up, The program will open a window showing the first frame of the video; The script will track the object across the video frames,

https://github.com/jeetpatel31/cs370-assignments/assets/96985261/96f1a479-a145-4120-ac50-63aed383c4ea

================================================


Instructions on how to run any tests (if applicable):

## Object Detection:

For testing the functionality of the tracking system, you'd typically prepare a set of test videos containing various scenarios relevant to your tracking objectives, such as different lighting conditions, occlusions, and object movements.

## Kalman Filter /  Extra Bonus::

I would say do the same thing as object detection


================================================

Instructions on how to run any notebook (if applicable) : N/A

