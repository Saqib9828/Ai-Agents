import cv2
import torch

# Load pre-trained YOLO model for object detection
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')


def scan_kitchen_video():
    # Open webcam (0 for default camera)
    cap = cv2.VideoCapture(0)

    detected_items = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Perform object detection
        results = model(rgb_frame)

        # Extract labels of detected objects
        labels = results.names
        detections = results.pred[0]

        # Filter and collect detected items relevant to kitchen
        for *box, conf, cls in detections:
            item = labels[int(cls)]  # Get item name from class
            if item not in detected_items:
                detected_items.append(item)

        # Show frame with bounding boxes (optional)
        annotated_frame = results.render()[0]
        cv2.imshow('Kitchen Object Detection', annotated_frame)

        # Break on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return detected_items


# Call function to get detected items
if __name__ == "__main__":
    items = scan_kitchen_video()
    print("Detected Items:", items)
