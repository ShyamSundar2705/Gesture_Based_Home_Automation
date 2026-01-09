# Gesture-Based Multi-Appliance Automation System (Camera-Based)

A real-time **camera-based gesture-controlled home automation system** that enables users to control multiple electrical appliances such as a fan and light using **hand gestures captured through a camera**.  
The system uses **Python (OpenCV + MediaPipe)** for gesture recognition and an **ESP32 microcontroller** for appliance control, communicating through serial/Wi-Fi.

---

## 📌 Project Overview

Traditional home automation systems rely on physical switches, mobile applications, or voice assistants. These approaches often require internet connectivity, smartphones, or accurate speech recognition, which may not be reliable in all environments.

This project implements a **vision-based gesture control system** where a camera captures hand gestures, processes them using computer vision techniques, and sends corresponding control commands to an ESP32 microcontroller.  
The ESP32 acts as a **fog-layer device**, executing appliance control locally for low latency and reliable operation.

---

## 🎯 Key Features

- Camera-based hand gesture recognition (no physical gesture sensor)
- Touchless and intuitive appliance control
- Real-time hand tracking using computer vision
- Fog-layer processing using ESP32 for fast response
- Controls multiple appliances (fan and light)
- LCD-based real-time status display
- Low-cost and scalable architecture
- Works without continuous internet dependency

---

## 🛠️ Hardware Components Used

- ESP32 Dev Board  
- USB Camera / Laptop Webcam  
- 16×2 LCD with I2C Module  
- 4-Channel Relay Module  
- 12V DC Fan  
- IRFZ44N MOSFET  
- Flyback Diode (1N4007)  
- 12V 2A Power Adapter  
- Jumper wires and breadboard  

---

## 💻 Software & Tools

### Gesture Recognition (PC Side)
- Python 3.x  
- OpenCV  
- MediaPipe  
- PySerial (for communication with ESP32)

### Embedded Control (ESP32 Side)
- Arduino IDE  
- Embedded C/C++  
- ESP32 Board Package  
- LiquidCrystal_I2C Library  

---

## ⚙️ System Architecture & Working

1. The **camera** captures live video of the user’s hand.
2. **Python (OpenCV + MediaPipe)** tracks hand landmarks and identifies gestures.
3. Recognized gestures are converted into control commands (e.g., `FAN_ON`, `LIGHT_OFF`).
4. Commands are sent to the **ESP32 via Serial or Wi-Fi**.
5. ESP32 processes commands locally (fog computing).
6. Relays and MOSFETs switch appliances accordingly.
7. LCD displays real-time appliance status.

---

## 🧠 Gesture Mapping

| Gesture | Action |
|--------|--------|
| Hand Up | Fan ON |
| Hand Down | Fan OFF |
| Hand Left | Light ON |
| Hand Right | Light OFF |
| Open Palm / Wave | Turn OFF all appliances |


---

## 🔒 Safety & Reliability

- Electrical isolation using relay modules  
- Flyback diode protection for DC motor  
- Gesture validation and threshold filtering in Python  
- Command verification on ESP32 to prevent false triggers  
- Local processing reduces latency and network dependency  

---

## 🚀 Future Enhancements

- AI-based gesture classification using deep learning
- Fan speed control using PWM
- Mobile app + dashboard integration
- Cloud logging and analytics (Firebase / MQTT)
- Voice + gesture hybrid control
- Multi-room automation with multiple ESP32 nodes

---

