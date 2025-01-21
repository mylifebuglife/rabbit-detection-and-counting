# Automated Rabbit Detection and Counting in Rabbit Farms Using Deep Learning

## Overview

This project is a comprehensive AI-based system designed to detect and count rabbits in a farm environment using advanced object detection techniques. The primary goal is to provide an automated solution for real-time monitoring of rabbit populations to enhance farm management.

The system leverages TensorFlow Lite for efficient real-time detection and counting. Key features include:
- Detecting and counting rabbits in video footage.
- Tracking movements of rabbits across farm sections separated by barriers.
- Exporting results to a CSV file for reporting and analysis.

**Read the full Documentation here:** [Automated Rabbit detection and counting in Rabbit farms](https://dg-ai.gitbook.io/ai-rabbit-classification)

---

## Features

1. **Real-Time Rabbit Detection**:
   - Detect and count rabbits in each frame of video footage.
   - Visualize detection results with bounding boxes and confidence scores.

2. **Batch Processing**:
   - Process multiple video files simultaneously.
   - Export aggregated results to CSV for farm management.

3. **Cross-Platform Compatibility**:
   - Applications built for both macOS (.dmg) and Windows (.exe).

4. **Scalability**:
   - Handle large datasets using optimized cloud resources.

---


## Getting Started

### Prerequisites

Before running the project, ensure the following are installed on your system:

- Python 3.9 or higher
- TensorFlow Lite
- LabelImg (optional, for annotating custom datasets)
- Supported Operating Systems: macOS, Windows, or Linux

---

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/rabbit-detection-and-counting.git
   cd rabbit-detection-and-counting
   ```
2.  **Setup a virtual environment **:
	```bash
	python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
```
3.  **Install Dependencies **:
```bash
pip install -r requirements.txt
```
4.  **(Optional) Install LabelImg: If you want to annotate additional data, install the LabelImg tool:**:
```bash
pip install labelImg
```
---
**Running with Conda**

**Create a Conda environement**
```bash
conda create --name rabbit_env python=3.9 -y
conda activate rabbit_env
```
**Install Dependencies: Install the required libraries from the requirements.txt file:**
```bash
pip install -r requirements.txt
```
**Run the Application from Command Line: Launch the app directly from the terminal:**
```bash
python app.py
```
##How to Run
**Single Video Processing**
Process a single video file and generate a rabbit count:
```bash
python single_video_processing.py --input_video path/to/video.mp4 --output_folder path/to/output
```
**Batch Video Processing**
Process multiple videos from a folder and generate a summary CSV:
```bash
python batch_processing.py --input_folder path/to/video/folder --output_csv path/to/output.csv
```
**Run the app**
Launch the application and interact through the GUI:
```bash
python app.py
```

##Contributing
Contributions are welcome! Please follow these steps:

**Fork this Repository:**
Click on the "Fork" button in the top right corner of this repository.

**Clone Your Fork:**
```bash
git clone https://github.com/yourusername/rabbit-detection-and-counting.git
```
**Create a branch**
```bash
git checkout -b feature-branch
```
**Submit a pull request**
Once your changes are tested, submit a pull request.

##Notes for Future Development
- Improve model accuracy using larger datasets and more advanced architectures.
- Explore real-time anomaly detection for farm management.
- Integrate the system with IoT devices for a fully automated farm monitoring solution.


