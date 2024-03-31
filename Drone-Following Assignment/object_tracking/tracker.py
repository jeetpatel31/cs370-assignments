import cv2

def select_objects(frame):
    objects = []
    while True:
        roi = cv2.selectROI("Frame", frame, fromCenter=False, showCrosshair=True)
        if roi == (0, 0, 0, 0):
            break
        objects.append(roi)
    return objects

def track_objects(frame, rois):
    trackers = []
    for roi in rois:
        tracker = cv2.TrackerCSRT_create()
        tracker.init(frame, roi)
        trackers.append(tracker)
    return trackers

def update_trackers(trackers, frame):
    for tracker in trackers:
        success, box = tracker.update(frame)
        if success:
            p1 = (int(box[0]), int(box[1]))
            p2 = (int(box[0] + box[2]), int(box[1] + box[3]))
            cv2.rectangle(frame, p1, p2, (0, 255, 0), 2, 1)
    return frame

def main(video_path):
    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()
    if not ret:
        print("Failed to read the video")
        return
    
    trackers = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = update_trackers(trackers, frame)
        cv2.imshow("Frame", frame)

        key = cv2.waitKey(30) & 0xFF
        if key == ord('p'):
            rois = select_objects(frame)
            trackers.extend(track_objects(frame, rois))
        elif key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_path = "Drone Tracking Video.mp4"
    main(video_path)
