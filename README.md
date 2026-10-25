# MMA3001_Pork-Packaging_Pass-Fail


# Project Overview
This project develops a machine-learning system that determines whether a pork rasher tray should pass or fail quality inspection based on detected packaging defects.

The system uses a YOLO object detection model trained on images of pork rasher packaging. This model identifies defects within the packaging and applies pre-determined confidence thresholds to provide a pass/fail/review decision.

This project aims to provide a more efficient for of product inspection, with the use of machine learning to improve quality control.

# Engineering Problem
The problem being addressed in this project is an automated model which detects whether an output pork rasher tray is classified as acceptable or defective, a pass/fail model.

Manual inspection is a very time consuming task and can often result in a high degree of human error. automated inspection and machine learning can provide a solution by detecting defects in packaging.

This project focuses on developing a computational method which determines if a package is defective and determines whether it should be rejected, accepted or subjected to a further review.

# Dataset
Dataset: Pork Rasher Error (Packaging)

Source: Roboflow Universe, by Helio

Link: https://universe.roboflow.com/helio-2aqe0/pork-rasher-error-packaging

Licence: CC BY 4.0, as displayed on the dataset page.

This dataset includes many RGB images of pork rasher trays with object detection, along with bounding box annotation. This dataset provides 1955 individual RGB images of various trays including defecting and non-defective.

The dataset contains five annotated defect classes:
- Loose meat
- Packaging error
- Twisted meat
- Unsealed
- Wrinkle

This training dataset was downloaded in the YOLOv8 format.

# Computational Method
The project uses YOLO object detection to identify packaging defects. A Python function converts detected defects into PASS or FAIL decisions.

The pretrained model was fine tuned using the provided pork rasher tray dataset

Training settings:
Epochs: 30
Input image size: 640
Batch size: 8
Random seed: 42
Training environment: Google Collab
Processing device: Cloud GPU

After training was complete, the best performing model was saved as "best.pt"

# Inspection Decision System
This system uses 3 possible outcomes:

Provisionary Pass: No defect with >25% confidency
Fail: Detects defect with >75% confidence
Review: At least one detected defect between 25% and 75% confidence

# Repository Structure
The datasets and trained model weights are stored locally and excluded from Github repository.

# Installation and Setup
Requirements:
- Python 3.10 or a compatible version
- Ultralytics YOLO
- PyTorch
- OpenCV
- NumPy
- Pandas
- Matplotlib
- scikit-learn
- pytest
- pdoc

Installation: 
Clone the GitHub repository and open it in VS Code.
Create a Python virtual environment:
python -m venv .venv

Activate the environment and install the required dependencies:
python -m pip install -r requirements.txt

Download the pork packaging dataset and extract it into the data/ folder.

The trained YOLO model (models/best.pt) is provided in the repository. Allowing fro users to run the inspection without need for retraining. The original untrained dataset is excluded due to its size.

Ensure that data.yaml references the correct directories and class names.

# Running the project
Training:
To train the YOLO model locally, run:
python train.py

The training notebook in notebooks/ documents the Google Colab training process.

The trained model weights are saved as best.pt.

For local inspection, place the trained model at:
models/best.pt

Inspecting a pork tray:
Run:
python tray_inspection.py

The output includes the inspection result, detected defect classes and respective confidence scores.

Evaluating the model:
Run:
python evaluate.py

This processes the provided test images and saves the inspection decisions to:
results/inspection_results.csv

Generate the annotation-derived reference labels using:
python generate_ground_truth.py

Compare predictions against the reference labels using:
python compare_results.py

The comparison is saved in the results folder.

# Results and Validation
The inspection system was evaluated using 76 images from the provided test dataset.

The evaluation compared predicted inspection decisions against labels derived from the original Roboflow dataset annotations.

Performance Summary:
- Total evaluated images : 76
- Annotated defective images : 75
- Automatically rejected : 6
- Sent for manual review : 62
- Provissionarly passed : 8
- Defect capture rate : 89.33%
- False acceptance rate : 10.67%
- Manual review rate : 81.58%

With a high rate of packages being sent for manual review, this model should not be seen as a standalone tool to automatically identify and sort defective from non-defective. However, this should be used as a tool to be used alongside manual inspectors to achieve the highest quality of products.

Validation Limitation:
he reference labels were generated from object-detection annotations rather than independently verified industrial inspection outcomes. There was only 1 image provided which passes inspection, this leaves much room for error in accurately determining a passing package.

# Automated Testing
Automated unit tests were developed to verify the inspection-decision function.

The tests examine:
- Fail classification for high-confidence defects.
- Review classification for medium-confidence defects.
- Provisional pass when no defect is detected above the screening threshold.
- Correct handling of the 75% decision boundary.

To run the tests:
python -m pytest tests/test_inspection.py -v

Test reports are stored in the tests folder.

# Limitations
- The model can only identify defects represented in its training data.
- Lighting variations, reflections and overlapping meat may reduce detection accuracy.
- The confidence scores describe individual defect detections, not the probability that an entire tray is acceptable.
- Some defective trays may receive a provisional PASS.
- The system requires manual review for a large proportion of images.
- The available test data contains very few annotation-derived acceptable trays.
- The model was evaluated using an existing dataset rather than a physical production-line system.

# Documentation
HTML documentation for the Python source code was generated using pdoc.

The documentation is available in docs. It describes the project functions, inputs, outputs and implementation.

# AI usage
AI tool, ChatGPT, was used in the process of completing this project. AI was utilised to assist with debugging code, areas in development of code, aswell as inquiries regarding documentation and project organisation.



