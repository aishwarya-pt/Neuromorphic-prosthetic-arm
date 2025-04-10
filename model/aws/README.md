
# Neuromorphic Prosthetic Arm Prototype

This project simulates an adaptive threshold learning model for EMG-based prosthetic control and integrates AWS for cloud storage. The ML model classifies signals like "open hand" or "close fist" and adjusts its threshold dynamically based on feedback.

## Features
- Simulated EMG data
- Adaptive learning algorithm
- AWS S3 integration for storing results

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Add AWS credentials
3. Run: `python main.py`

## Future Scope
- Real EMG sensor integration
- Frontend-backend interface using Flask
- Real-time adaptive learning

