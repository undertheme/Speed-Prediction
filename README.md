# Speed Estimation of Vehicles using YOLOv8

## Overview
This project utilizes **YOLOv8** for object detection and tracking to estimate the speed of vehicles in real-time. The system identifies and tracks vehicles across frames and calculates their speed based on the displacement over time.

## Features
- **Vehicle Detection**: Identifies various types of vehicles (cars, trucks, motorcycles, buses, etc.).
- **Object Tracking**: Tracks vehicles across frames to maintain continuity.
- **Speed Estimation**: Computes vehicle speed based on frame rate and pixel displacement.
- **Real-time Processing**: Optimized for high FPS tracking and inference.
- **Demo Video**: A sample video demonstrating the results is included.

## Technology Stack
- **YOLOv8**: Object detection and tracking
- **DeepSORT**: Multi-object tracking
- **OpenCV**: Video processing
- **Python**: Main programming language
- **NumPy & Pandas**: Data processing

## Installation
```bash
# Clone the repository
git clone https://github.com/MoizAhmed2517/Speed-Estimation.git
cd Speed-Estimation

# Install dependencies
pip install -r requirements.txt
```

## Results
The model successfully detects and tracks vehicles, estimating their speed based on movement across frames. A sample output video is included in the repository.

## Video Demonstration
[![Demo Video](https://img.icons8.com/fluency/48/play-button-circled.png)](https://drive.google.com/file/d/1fZqHCEhWtDdsjWRp9N7AVQd7Ab7CRc_3/view?usp=sharing))

> Click the play button above to watch the demo.

## Contributing
Feel free to fork the repository and open pull requests for improvements!

## License
This project is licensed under the MIT License.

## Contact
For queries, reach out via ahmedmoiz962@gmail.com or create an issue in the repository.

---

### **SEO Optimized Keywords**
YOLOv8 speed estimation, vehicle tracking, real-time object tracking, AI-based traffic monitoring, deep learning for traffic analysis, computer vision speed detection, real-time vehicle speed tracking.
