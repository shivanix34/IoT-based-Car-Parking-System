# IoT-Based Car Parking System

## Overview

The IoT-Based Car Parking System is a modern solution designed to streamline the parking process using Internet of Things (IoT) technology. This system enhances security, efficiency, and user experience through features like QR code authentication and real-time monitoring.

### Abstract

The rapid urbanization has increased the demand for efficient and secure car parking systems. To address this, we present an IoT-based solution that includes a user-friendly application for slot booking, QR code-based entry, and minute-based billing. This system integrates IoT devices for real-time monitoring and gate control, providing effective management and enhanced user security.

### Key Features

- **User Application**: Allows users to register, log in, and book parking slots.
- **Admin Application**: Enables administrators to monitor occupancy, manage bookings, and authenticate entry using QR codes.
- **IoT Integration**: Utilizes IoT devices for real-time monitoring of parking slots and gate control.
- **QR Code Authentication**: Enhances security with unique QR codes for entry and exit.
- **Minute-Based Billing**: Calculates parking fees accurately based on actual time spent.
- **Hardware Components**: Arduino Uno, servo motors, and IR sensors for gate automation and vehicle detection.

## Implementation Details

### Methodology

1. **System Design**: Architecture planning for scalability, security, and user-friendliness.
2. **Application Development**: User and admin interfaces using Python's Kivy module.
3. **IoT Integration**: Real-time monitoring with Firebase cloud platform.
4. **Gate Control**: Arduino Uno and servo motors for automated gate operations.
5. **QR Code Generation**: Python's qr library for secure digital keys.

### Results

- Real-time slot booking and entry with QR code authentication.
- Cost-efficient operation without individual IR sensors.
- Enhanced security and user satisfaction.

### Comparison with Existing Solutions

- Improved security with QR code authentication.
- Cost efficiency through elimination of IR sensors.
- Minute-based billing for fair and transparent fee calculation.
