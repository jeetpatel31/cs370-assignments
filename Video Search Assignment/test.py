import torch
import torchvision.transforms as T
import cv2
from torchvision.models.detection import fasterrcnn_resnet50_fpn
import pandas as pd
import numpy as np
import time

# Load a pre-trained Faster R-CNN model
model = fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()

# Define the transformation
transform = T.Compose([T.ToPILImage(), T.Resize(300), T.ToTensor()])

# MS COCO label map for a subset of common classes
label_map = {
    1: "person", 2: "bicycle", 3: "car", 4: "motorcycle",
    5: "airplane", 6: "bus", 7: "train", 8: "truck",
    9: "boat", 10: "traffic light", 11: "fire hydrant",
    13: "stop sign", 14: "parking meter", 15: "bench",
    16: "bird", 17: "cat", 18: "dog", 19: "horse",
    20: "sheep", 21: "cow", 22: "elephant", 23: "bear",
    24: "zebra", 25: "giraffe", 27: "backpack", 28: "umbrella",
    31: "handbag", 32: "tie", 33: "suitcase", 34: "frisbee",
    35: "skis", 36: "snowboard", 37: "sports ball", 38: "kite",
    39: "baseball bat", 40: "baseball glove", 41: "skateboard",
    42: "surfboard", 43: "tennis racket", 44: "bottle",
    46: "wine glass", 47: "cup", 48: "fork", 49: "knife",
    50: "spoon", 51: "bowl", 52: "banana", 53: "apple",
    54: "sandwich", 55: "orange", 56: "broccoli", 57: "carrot",
    58: "hot dog", 59: "pizza", 60: "donut", 61: "cake",
    62: "chair", 63: "couch", 64: "potted plant", 65: "bed",
    67: "dining table", 70: "toilet", 72: "tv", 73: "laptop",
    74: "mouse", 75: "remote", 76: "keyboard", 77: "cell phone",
    78: "microwave", 79: "oven", 80: "toaster", 81: "sink",
    82: "refrigerator", 84: "book", 85: "clock", 86: "vase",
    87: "scissors", 88: "teddy bear", 89: "hair drier", 90: "toothbrush"
}

def detect_objects(frame):
    # Transform the frame
    frame = transform(frame)
    # Add a batch dimension
    frame = frame.unsqueeze(0)
    
    with torch.no_grad():
        prediction = model(frame)
    
    return prediction

def process_video(video_path, skip_frames=5):
    cap = cv2.VideoCapture(video_path)
    frameNum = 0
    fps = cap.get(cv2.CAP_PROP_FPS)  # Frame rate of the video
    detections_list = []  # List to store detection results
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        if frameNum % skip_frames == 0:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            detections = detect_objects(frame_rgb)[0]
            
            for i in range(len(detections['labels'])):
                score = detections['scores'][i].item()
                if score > 0.5:  # Confidence threshold
                    label_id = detections['labels'][i].item()
                    label = label_map.get(label_id, 'Unknown')
                    box = detections['boxes'][i].numpy().astype(int)
                    timestamp = frameNum / fps
                    
                    # Draw the bounding box and label on the frame
                    cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)
                    cv2.putText(frame, f'{label}: {score:.2f}', (box[0], box[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    
                    detections_list.append([
                        video_path, frameNum, timestamp, label_id, label, score, box.tolist()
                    ])
            
            # Display the frame
            cv2.imshow('Video', frame)
            # Press 'q' to quit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        
        frameNum += 1
    
    cap.release()
    cv2.destroyAllWindows()
    return pd.DataFrame(detections_list, columns=['vidId', 'frameNum', 'timestamp', 'detectedObjId', 'detectedObjClass', 'confidence', 'bbox info'])

# Adjust 'skip_frames' as needed to balance speed and detection frequency
detections_df = process_video('test2.mp4', skip_frames=50)


# To save the DataFrame to a CSV file
detections_df.to_csv('detections.csv', index=False)

# If you wish to print the DataFrame to see the results
print(detections_df.head())
