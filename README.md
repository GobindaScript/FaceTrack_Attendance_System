# FaceTrack_Attendance_System
A real-time face recognition system using OpenCV and KNN for automatic attendance management.

# 🎯 FaceTrack-Attendance-System

A real-time face recognition-based attendance system using OpenCV, NumPy, scikit-learn, and Haar cascades.

## 📸 Features

- Live face detection via webcam
- Real-time face recognition using KNN algorithm
- Attendance tracking and CSV log generation
- Background interface for improved UI
- Data storage using `pickle` for efficient model training

## 📁 Project Structure

FaceTrack-Attendance-System/
│
├── data/ # Stores names.pkl and faces_data.pkl
├── Attendance/ # Stores attendance logs by date
├── background.png # Background image for GUI
├── Register_Face.py # Script to capture and save facial data
├── Attendance.py # Script to run attendance system
├── README.md # This file
└── requirements.txt # Python dependencies


## 🛠️ Installation

1. Clone the repo:
```bash
git clone https://github.com/YOUR-USERNAME/FaceTrack-Attendance-System.git
cd FaceTrack-Attendance-System

2.Install dependencies:
pip install -r requirements.txt

3.Run the model Register_Face.py:
python Register_Face.py
(100 scan requred for  face recognition)

4.Start the attendance system:
python Attendance.py

5.click 'o' for take Attendance.

6.clik 'q' for Exit.

7.Now Click on Attendance folder to track your attandance logs by date.
