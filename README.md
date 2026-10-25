# MMA3001_Pork-Packaging_Pass-Fail


# Project Overview
This project develops a machine-learning system that determines whether a pork rasher tray should pass or fail quality inspection based on detected packaging defects.

# Engineering Problem
The problem being addressed in this project is an automated model which detects whether an output pork rasher tray is classified as acceptable or defective, a pass/fail model.

# Dataset
Pork Rasher Error (Packaging) – Roboflow, by Helio. 

The dataset contains five annotated defect classes:
- Loose meat
- Packaging error
- Twisted meat
- Unsealed
- Wrinkle

# Computational Method
The project uses YOLO object detection to identify packaging defects. A Python function converts detected defects into PASS or FAIL decisions.

# Project Files
- `train.py` – Trains the YOLO model.
- `tray_inspection.py` – Performs image inspection and produces PASS/FAIL results.
- `evaluate.py` – Evaluates model performance.
- `tests/` – Contains automated tests.
- `results/` – Contains evaluation results and graphs.
- `docs/` – Contains code documentation.

# Installation
Install the required packages:

`python -m pip install -r requirements.txt`

Download and extract the dataset into `data/`, ensuring the paths in `data.yaml` are correct.

# Evaluation
The system will be evaluated using defect recall, false acceptance rate, false rejection rate, accuracy and processing time.

# Limitations
The system only identifies defects represented by the training data. It does not replace comprehensive food-safety inspection.

# AI Acknowledgement
AI assistance used during development will be disclosed and critically evaluated in the project report.