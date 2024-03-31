import cv2
import numpy as np
from filterpy.kalman import KalmanFilter

def initialize_kalman_filter():
    kf = KalmanFilter(dim_x=4, dim_z=2)
    kf.F = np.array([[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]])
    kf.H = np.array([[1, 0, 0, 0], [0, 1, 0, 0]])
    kf.R *= 10
    kf.P *= 1000
    kf.Q = np.eye(kf.dim_x) * 0.01
    return kf

def select_objects(frame):
    objects = []
    print("Select objects and press ENTER or SPACE when done. Press 'c' to cancel the current selection.")
    while True:
        roi = cv2.selectROI("Frame", frame, fromCenter=False, showCrosshair=True)
        if roi == (0, 0, 0, 0):
            break
        kf = initialize_kalman_filter()
        objects.append([roi, kf, [], None])
    cv2.destroyAllWindows()
    return objects

def track_objects(frame, objects):
    for object in objects:
        roi = object[0]
        tracker = cv2.TrackerCSRT_create()
        tracker.init(frame, roi)
        object[3] = tracker

def update_trackers(objects, frame):
    for object in objects:
        tracker = object[3]
        success, box = tracker.update(frame)
        if success:
            p1 = (int(box[0]), int(box[1]))
            p2 = (int(box[0] + box[2]), int(box[1] + box[3]))
            cv2.rectangle(frame, p1, p2, (0, 255, 0), 2)
            center = (p1[0] + (p2[0] - p1[0]) // 2, p1[1] + (p2[1] - p1[1]) // 2)
            object[2].append(center)
            object[1].update(np.array([[center[0]], [center[1]]]))

def main(video_path):
    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()
    if not ret:
        print("Failed to read the video")
        return
    
    objects = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        update_trackers(objects, frame)
        cv2.imshow("Frame", frame)

        key = cv2.waitKey(30) & 0xFF
        if key == ord('p'):
            selected_objects = select_objects(frame)
            objects.extend(selected_objects)
            track_objects(frame, selected_objects)
        elif key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_path = "Cyclist and vehicle Tracking - 2.mp4"
    main(video_path)
