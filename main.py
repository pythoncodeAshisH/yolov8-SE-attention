from ultralytics import YOLO

# Load a model

model = YOLO('yolov8n.yaml')  # load a pretrained model (recommended for training)


# Train the model
results = model.train(data='D:\Project\pothole.yaml',batch=64, epochs=3, imgsz=640,exist_ok=True ,optimizer='SGD')