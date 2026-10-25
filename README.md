# AI-Based Personalized and Portable Adaptive Climate Control System

## Overview

The **AI-Based Personalized and Portable Adaptive Climate Control System** is an engineering major project that combines face recognition, voice-controlled operation, environmental sensing, web technologies, and hardware control to provide personalized indoor comfort.

The system uses a pre-trained FaceNet model and MTCNN-based face detection to recognize registered users through the laptop's built-in camera. It retrieves the recognized user's stored temperature preference from an SQLite database and sends the corresponding command to the connected hardware.

Voice commands are captured through the laptop's built-in microphone and processed using Python speech-recognition libraries. A Flask web application provides user registration, face-recognition video streaming, and climate-control operations.

## Key Features

- **Face Recognition:** Uses MTCNN for face detection and alignment and FaceNet embeddings for identity matching.
- **Personalized Temperature Settings:** Retrieves registered users' temperature preferences from SQLite.
- **Voice Control:** Accepts spoken commands through the laptop's built-in microphone.
- **Web Application:** Uses Flask to provide user registration, camera streaming, and control endpoints.
- **Environmental Sensing:** Integrates temperature, humidity, and air-quality sensors.
- **Heating and Cooling:** Supports heater and cooler control through connected electronics.
- **Hardware Communication:** Sends control data to the connected microcontroller through serial communication.
- **Unknown-Face Handling:** Identifies faces that do not match the registered identities.

## Technologies Used

### Software

- Python
- Flask
- OpenCV
- TensorFlow 1.x compatibility interface
- FaceNet
- MTCNN
- NumPy
- scikit-learn
- SpeechRecognition
- sounddevice
- SQLite
- PySerial
- HTML, CSS, and JavaScript, where implemented

### Hardware

- Laptop built-in camera
- Laptop built-in microphone
- DHT11 temperature and humidity sensor
- MQ-135 air-quality sensor
- Peltier cooling module
- PTC ceramic heater
- Relay module
- OLED display
- Microcontroller and supporting electronic components

## System Workflow

1. A user registers through the Flask web application.
2. The application creates a face dataset for the registered user.
3. MTCNN detects and aligns faces from the live camera feed.
4. FaceNet generates embeddings representing the detected faces.
5. The system compares the embeddings with stored identity embeddings.
6. When a registered user is recognized, the application retrieves their temperature preference from SQLite.
7. The preference is sent through serial communication to the connected hardware.
8. The voice-recognition component processes spoken commands to control the heater or cooler.
9. The web interface displays the camera feed and recognition status.

## Face Recognition Method

The recognition pipeline uses a pre-trained FaceNet model stored as a TensorFlow `.pb` graph.

- **Face detection:** MTCNN locates faces and facial landmarks.
- **Face alignment:** Detected faces are prepared for embedding generation.
- **Feature extraction:** FaceNet converts each face into a numerical embedding.
- **Identity matching:** The system calculates pairwise distances and compares them against a configured threshold of `1.0`.
- **User lookup:** The matched identity is used to retrieve the registered user's information and temperature preference.

The FaceNet model is loaded from the `20170512-110547/20170512-110547.pb` file.

## Voice Control

The voice-recognition component records audio using the laptop's built-in microphone and processes the recording using SpeechRecognition.

| Recognized command | Serial data |
|---|---|
| Heater 1 / Heater One | `A` |
| Heater 2 / Heater Two | `B` |
| Cooler | `C` |
| Stop / Exit / End | `D` |

The script records five-second audio segments at a sampling rate of 16 kHz. Recognized commands are sent through a serial connection configured for COM3 at 9600 baud.

Speech transcription uses Google's speech-recognition service with the `en-US` language setting.

## Database Management

SQLite stores user registration information, including:

- User ID
- Name
- Phone number
- Email address
- Temperature preference
- Password field

The registered user ID is associated with the corresponding face dataset, enabling the application to link recognition results with stored preferences.

## Applications

- Smart classrooms and laboratories
- Personal workspaces and office cubicles
- Personalized climate-control systems
- AI-enabled embedded systems
- Computer-vision-based automation

## Future Enhancements

- Improve recognition reliability across different lighting conditions.
- Strengthen user authentication and password security.
- Improve voice recognition in noisy environments.
- Incorporate sensor-driven adaptive temperature decisions.
- Add remote monitoring and mobile application support.
- Optimize energy consumption and hardware safety.

## Project Status

Engineering major project integrating pre-trained FaceNet-based face recognition, MTCNN face detection, voice-command processing, a Flask web application, SQLite database management, and serial hardware control.

## Contributors

Engineering Major Project


## Project Screenshots

![Home Page](screenshots/home-page.png)
### Home Page<img width="1600" height="766" alt="Home Page" src="https://github.com/user-attachments/assets/f6c0aa55-3074-40b1-8cf9-33b1af49caeb" />

### Face Recognition
![Face Recognition](screenshots/face-recognition.png)
<img width="1581" height="743" alt="Face Recognition" src="https://github.com/user-attachments/assets/e3c92208-1bd0-447c-8053-2ff364790c48" />


### User Registration
![User Registration](screenshots/user-registration.png)
<img width="1600" height="763" alt="User Registration" src="https://github.com/user-attachments/assets/ef76f8a9-f123-456a-bd65-d7a362c01149" />


### Hardware Prototype
![Hardware Prototype](screenshots/hardware-prototype.jpg)
<img width="1280" height="960" alt="Hardware Prototype png" src="https://github.com/user-attachments/assets/af9cda24-f558-4538-9a62-a5b6e842025a" />
