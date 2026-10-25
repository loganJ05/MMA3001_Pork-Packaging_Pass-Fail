
"""Generate preliminary inspection labels from Roboflow annotations."""

from pathlib import Path
import pandas as pd

IMAGE_FOLDER = Path("data/test/images")
LABEL_FOLDER = Path("data/test/labels")

records = []

# Find all test images
image_files = sorted(
    p for p in IMAGE_FOLDER.iterdir()
    if p.suffix.lower() in {".jpg", ".jpeg", ".png"}
)

for image_path in image_files:

    label_path = LABEL_FOLDER / f"{image_path.stem}.txt"

    if not label_path.exists():
        actual = "REVIEW"

    elif label_path.read_text().strip():
        # At least one annotated defect
        actual = "FAIL"

    else:
        # No annotated defects
        actual = "PASS"

    records.append({
        "image": image_path.name,
        "actual": actual
    })

ground_truth = pd.DataFrame(
    records,
    columns=["image", "actual"]
)

ground_truth.to_csv("ground_truth.csv", index=False)

print("Ground-truth table generated:")
print(ground_truth["actual"].value_counts())

print("\nSaved to ground_truth.csv")
