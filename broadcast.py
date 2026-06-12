import pyvirtualcam
import cv2 as cv
import supervision as sv
from PIL import Image
from rfdetr import RFDETRSmall

def stream(cap):

    CHECKPOINT_PATH = r"content\output\checkpoint_best_total.pth"

    CLASS_NAMES = [
    "1", "10", "11", "12", "13", 
    "14", "15", "2", "3", "4", 
    "5", "6", "7", "8", "9", 
    "Empty", "Board"
]
    model = RFDETRSmall(pretrain_weights=CHECKPOINT_PATH)

    box_annotator = sv.BoxAnnotator()
    label_annotator = sv.LabelAnnotator()

    # Initialize Insta360 webcam
    ret, frame = cap.read()
    if ret:
        height, width = frame.shape[:2]

    # Initialize virtual camera device
    with pyvirtualcam.Camera(width=width, height=height, fps=30, fmt=pyvirtualcam.PixelFormat.BGR) as cam:
        print(f'Sending frames to: {cam.device}')
        
        while True:
            # Check that frames are actually being sent
            ret, frame = cap.read()
            if not ret: 
                break

            rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            pil_image = Image.fromarray(rgb_frame)
            detections = model.predict(pil_image, threshold=0.5)

            labels = []
            for class_id, confidence in zip(detections.class_id, detections.confidence):
                class_name = CLASS_NAMES[int(class_id - 1)]
                labels.append(f"{class_name} {confidence:.2f}")

            annotated_frame = frame.copy()
            annotated_frame = box_annotator.annotate(annotated_frame, detections)
            annotated_frame = label_annotator.annotate(annotated_frame, detections, labels)

            print(f"Sending frames to: {cam.device}")
            cam.send(annotated_frame)
            cam.sleep_until_next_frame()
