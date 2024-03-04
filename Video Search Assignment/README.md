Name of the assignment : Video Search Assignment 

================================================

Date of submission : 03/03/2024

================================================

JUST WANTED TO PUT THIS OUT HERE AT THE BEGINNING:

I wanted to update you on my progress with the project, specifically regarding the setup of Docker and PostgreSQL. Unfortunately, I encountered significant challenges in getting them to work properly. However, I've managed to find a workaround that I believe will suffice for the time being.

To address the requirements of sections 2.2 and 2.3, I selected a video from the initial tasks, trimmed it to approximately 10 seconds, and successfully executed the code on local machines. it did worked and i was able to commit it onto the git as well so I hope youll understand. I have explained the rest of the codes in the README. Thanks

================================================

Instructions on how to run the code :

Step 1: Video library (10 points)
= 
Install the required libraries by running pip install pytube youtube_transcript_api in your terminal or command prompt

Save the code to a Python file, for example, download_youtube.py

Run the code by opening your terminal or command prompt, navigating to the directory containing the saved file, and executing python download_youtube.py

The code will create a directory named downloaded_videos (if it doesn't already exist), download the highest resolution streams of the videos specified by their IDs in the main function into this directory, and attempt to download their transcripts as text files

Step 2: Video indexing pipeline (90 points)

2.1 Preprocess the video (15 points)
= 
Initiate installation protocols for required Python packages:
Execute "pip install opencv-python-headless numpy matplotlib" in your terminal matrix

Before activation, ensure video file matrix is present in same directory as script, or provide absolute path to video file matrix in video_src variable

Activate script by:
Accessing terminal matrix

Navigating to directory containing Python file receptacle

Executing "python video_process_display.py"

Script will display processed video frame matrices one by one:

Original frame matrix

Resized frame matrix

RGB converted frame matrix

Normalized frame matrix

Cycling will continue through every step frames until termination of video matrix

2.2 Detecting objects (25 points)
=
necessary libraries. Install PyTorch, torchvision, OpenCV (cv2), Pandas, and Numpy by running pip install torch torchvision opencv-python pandas numpy in your command line or terminal.

The code assumes you have a video file named test2.mp4 in your working directory. You can change the video_path variable in the process_video function call at the end of the script to point to the path of your video file.

Run the script by executing python object_detection.py in your terminal or command line. The script processes the video, detects objects frame by frame (skipping a specified number of frames for efficiency), saves images of detected objects in a directory named detected_objects, and finally, outputs a CSV file named detections.csv containing details of the detected objects.

2.3 Embedding model (30 points)
=
Install the Python Imaging Library (Pillow) and NumPy by running pip install Pillow numpy in your command line or terminal.

Before running the script, create a directory named detected_objects in the same directory as your script and populate it with the images you want to process. The script is set to read images from this directory.

Run the script by executing python image_deconstruction.py in your terminal or command line. The script will process each image in the detected_objects directory, creating deconstructed and reconstructed versions. 

The deconstructed images will be saved in a new directory named deconstructed, and the reconstructed images (with gaps between the segments) will be saved in another new directory named reconstructed_with_gaps.
To test the functionality, check the deconstructed and reconstructed_with_gaps directories after running the script to ensure the images have been processed and saved correctly.

Each original image will have two new versions: one where its 3x3 grid has been randomly shuffled and saved in the deconstructed directory, and another where the original grid is reconstructed with gaps between segments, saved in the reconstructed_with_gaps directory.


================================================

Instructions on how to run any tests (if applicable):

Step 1: Video library (10 points)
= 
if you need to test its functionality, you can manually verify that the videos and their transcripts are correctly downloaded to the downloaded_videos folder.

Step 2: Video indexing pipeline (90 points)

2.1 Preprocess the video (15 points)
= 
To test its functionality, you could manually verify that it processes and displays frames as described, by observing the output for each frame processed. To further ensure it's working correctly, you might modify the parameters like newSize and step to see the effects on the output, or try it with different video files to confirm it works across various video formats and resolutions.


2.2 Detecting objects (25 points)
= 
To test the code, you could verify the output by checking the detected_objects directory for saved images of detected objects and reviewing the detections.csv file for accuracy and completeness of the detection data. Additionally, you might adjust the skip_frames parameter to process more or fewer frames and observe the impact on detection performance and processing time.

2.3 Embedding model (30 points)
=
Test teh effectiveness by comparing the original images in the detected_objects directory with their processed versions in the deconstructed and reconstructed_with_gaps directories, ensuring the images have been appropriately shuffled and reconstructed as described.
================================================

Instructions on how to run any notebook (if applicable) : N/A