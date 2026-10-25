
from ultralytics import YOLO

def train_model():
    """Train a YOLO model to identify pork packaging defects."""

    model = YOLO("yolo11n.pt")

    model.train(
        data="data/data.yaml",
        epochs=30,
        imgsz=640,
        batch=8,
        seed=42,
        project="results",
        name="training"
    )

if __name__ == "__main__":
    train_model()
