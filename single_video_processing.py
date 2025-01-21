# import cv2
# import numpy as np
# from tensorflow.lite.python.interpreter import Interpreter

# # Paths to model and label map
# MODEL_PATH = "/Users/debtanu/Desktop/HiWi/final/model/detect.tflite"
# LABEL_MAP_PATH = "/Users/debtanu/Desktop/HiWi/final/model/labelmap.txt"

# # Load label map
# with open(LABEL_MAP_PATH, "r") as f:
#     labels = [line.strip() for line in f.readlines()]
# if labels[0] == "???":
#     del labels[0]  # Remove background label if present


# def process_single_video(video_path):
#     """Process a single video file."""
#     video_name = video_path.split("/")[-1]
#     print(f"Processing video: {video_name}")

#     # Initialize interpreter
#     interpreter = Interpreter(model_path=MODEL_PATH)
#     interpreter.allocate_tensors()

#     # Get model details
#     input_details = interpreter.get_input_details()
#     output_details = interpreter.get_output_details()
#     height, width = input_details[0]['shape'][1:3]

#     # Open video
#     video = cv2.VideoCapture(video_path)
#     imW = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
#     imH = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

#     frame_count = 0
#     total_rabbits = 0
#     frame_interval = 5  # Process every 5th frame for speed

#     while video.isOpened():
#         ret, frame = video.read()
#         if not ret:
#             print(f"Finished processing {video_name}.")
#             break

#         # Skip frames
#         if frame_count % frame_interval != 0:
#             frame_count += 1
#             continue

#         # Process frame
#         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         frame_resized = cv2.resize(frame_rgb, (width, height))
#         input_data = np.expand_dims(frame_resized / 255.0, axis=0).astype(np.float32)

#         # Perform inference
#         interpreter.set_tensor(input_details[0]['index'], input_data)
#         interpreter.invoke()

#         # Get model output
#         boxes = interpreter.get_tensor(output_details[0]['index'])[0]
#         classes = interpreter.get_tensor(output_details[1]['index'])[0]
#         scores = interpreter.get_tensor(output_details[2]['index'])[0]

#         # Ensure scores is iterable
#         if not isinstance(scores, np.ndarray):
#             scores = np.array([scores])

#         rabbit_count = 0
#         for i, score in enumerate(scores):
#             if score > 0.5:  # Confidence threshold
#                 box = boxes[i] if isinstance(boxes[i], (list, np.ndarray)) else [0, 0, 0, 0]
#                 class_idx = int(classes[i]) if isinstance(classes[i], (int, float)) else int(classes[i].flatten()[0])

#                 if class_idx < len(labels) and labels[class_idx] == "Rabbit":
#                     rabbit_count += 1

#         frame_count += 1
#         total_rabbits += rabbit_count

#     video.release()
#     return video_name, frame_count, total_rabbits

# #python single_video_processing.py --video /Users/debtanu/Desktop/HiWi/final/testappvideos/CH01-20240318-115642-134732-001000000000.mp4


import cv2
import numpy as np
from tensorflow.lite.python.interpreter import Interpreter

# Paths to model and label map
MODEL_PATH = "/Users/debtanu/Desktop/HiWi/final/model/detect.tflite"
LABEL_MAP_PATH = "/Users/debtanu/Desktop/HiWi/final/model/labelmap.txt"

# Load label map
with open(LABEL_MAP_PATH, "r") as f:
    labels = [line.strip() for line in f.readlines()]
if labels[0] == "???":
    del labels[0]  # Remove background label if present


def process_single_video(video_path):
    """Process a single video file."""
    video_name = video_path.split("/")[-1]
    print(f"Processing video: {video_name}")

    # Initialize interpreter
    interpreter = Interpreter(model_path=MODEL_PATH)
    interpreter.allocate_tensors()

    # Get model details
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    height, width = input_details[0]['shape'][1:3]

    # Open video
    video = cv2.VideoCapture(video_path)
    imW = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    imH = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    frame_count = 0
    total_rabbits = 0
    frame_interval = 5  # Process every 5th frame for speed

    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            print(f"Finished processing {video_name}.")
            break

        # Skip frames
        if frame_count % frame_interval != 0:
            frame_count += 1
            continue

        # Process frame
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_resized = cv2.resize(frame_rgb, (width, height))
        input_data = np.expand_dims(frame_resized / 255.0, axis=0).astype(np.float32)

        # Perform inference
        interpreter.set_tensor(input_details[0]['index'], input_data)
        interpreter.invoke()

        # Get model output
        try:
            boxes = interpreter.get_tensor(output_details[0]['index'])[0]
            classes = interpreter.get_tensor(output_details[1]['index'])[0]
            scores = interpreter.get_tensor(output_details[2]['index'])[0]

            # Ensure scores and classes are iterable
            if not isinstance(scores, np.ndarray):
                scores = np.array([scores])
            if not isinstance(classes, np.ndarray):
                classes = np.array([classes])

        except Exception as e:
            print(f"Error during inference: {str(e)}")
            continue

        rabbit_count = 0
        for i, score in enumerate(scores):
            try:
                if score > 0.5:  # Confidence threshold
                    class_idx = int(classes[i]) if isinstance(classes[i], (int, float)) else int(classes[i].flatten()[0])
                    if class_idx < len(labels) and labels[class_idx] == "Rabbit":
                        rabbit_count += 1

            except Exception as e:
                print(f"Error processing detection: {str(e)}")
                continue

        frame_count += 1
        total_rabbits += rabbit_count

    video.release()
    return video_name, frame_count, total_rabbits

