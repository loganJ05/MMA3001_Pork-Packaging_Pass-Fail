"""Automated pork packaging inspection using YOLO."""

from pathlib import Path
from ultralytics import YOLO

MODEL_PATH = "models/best.pt"

FAIL_THRESHOLD = 0.75
REVIEW_THRESHOLD = 0.25

REJECT_CLASSES = {
    "loose-meat",
    "packaging-error",
    "twisted-meat",
    "unsealed",
    "wrinkle",
}


def classify_tray(detections):
    """Classify a tray from a list of detected defects.

    Each detection contains a class name and confidence score.

    Returns:
        str: FAIL, REVIEW, or PROVISIONAL PASS.
    """
    confidence_scores = [
        d["confidence"]
        for d in detections
        if d["class"] in REJECT_CLASSES
    ]

    if any(score >= FAIL_THRESHOLD for score in confidence_scores):
        return "FAIL"

    if any(score >= REVIEW_THRESHOLD for score in confidence_scores):
        return "REVIEW"

    return "PROVISIONAL PASS"


def inspect_image(image_path):
    """Detect defects and produce an inspection decision."""
    if not Path(image_path).is_file():
        raise FileNotFoundError(image_path)

    model = YOLO(MODEL_PATH)

    results = model.predict(
        source=image_path,
        conf=REVIEW_THRESHOLD,
        device="cpu",
        verbose=False,
    )

    result = results[0]
    detections = []

    for box in result.boxes:
        class_id = int(box.cls.item())

        detections.append({
            "class": result.names[class_id],
            "confidence": float(box.conf.item()),
        })

    decision = classify_tray(detections)

    return decision, detections


if __name__ == "__main__":
    print("Starting pork packaging inspection...")
    # Find test images
    test_images = list(Path("data/test/images").glob("*.jpg"))

    # Check that images exist
    if not test_images:
        raise FileNotFoundError("No test images found")

    # Select the first image
    image = str(test_images[0])

    # Run inspection
    decision, defects = inspect_image(image)

    # Display results
    print("Inspection decision:", decision)
    print("Detected defects:", defects)
