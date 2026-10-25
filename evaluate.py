
"""Evaluate pork packaging inspection decisions."""

from pathlib import Path
import pandas as pd

from tray_inspection import inspect_image


def evaluate_images():
    """Inspect all test images and save the results."""

    image_folder = Path("data/test/images")
    output_folder = Path("results")

    output_folder.mkdir(exist_ok=True)

    image_files = sorted(
        p for p in image_folder.iterdir()
        if p.suffix.lower() in {".jpg", ".jpeg", ".png"}
    )

    records = []

    for image_path in image_files:

        decision, defects = inspect_image(str(image_path))

        records.append({
            "image": image_path.name,
            "decision": decision,
            "detected_defects": len(defects),
            "highest_confidence": max(
                (d["confidence"] for d in defects),
                default=0.0
            )
        })

    df = pd.DataFrame(records)

    df.to_csv(
        output_folder / "inspection_results.csv",
        index=False
    )

    print(df["decision"].value_counts())
    print("Results saved successfully.")


if __name__ == "__main__":
    evaluate_images()
