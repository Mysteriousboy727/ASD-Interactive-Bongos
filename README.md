# ASD Interactive Bongos

An interactive therapeutic tool designed to support individuals with Autism Spectrum Disorder (ASD) through engaging, sensory-responsive activities using physical bongo drums connected to a Raspberry Pi.

## Table of Contents

- [About Autism Spectrum Disorder (ASD)](#about-autism-spectrum-disorder-asd)
- [Project Overview](#project-overview)
- [Benefits](#benefits)
- [Hardware Integration](#hardware-integration)
- [System Architecture](#system-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## About Autism Spectrum Disorder (ASD)

**Autism Spectrum Disorder (ASD)** is a neurodevelopmental condition characterized by:

- **Communication Challenges**: Difficulties with verbal and non-verbal communication, social interaction, and understanding social cues
- **Sensory Processing Differences**: Heightened or reduced sensitivity to sensory stimuli (sounds, lights, textures, etc.)
- **Repetitive Behaviors**: Preference for routines and repetitive activities
- **Unique Strengths**: Many individuals with ASD have exceptional focus, attention to detail, and unique perspectives

### Why Interactive Tools Matter

Interactive, sensory-based activities can be highly beneficial for individuals with ASD by:
- Providing predictable, controllable sensory experiences
- Encouraging cause-and-effect learning
- Supporting motor skill development
- Creating opportunities for engagement and communication
- Reducing anxiety through structured, repetitive interactions

## Project Overview

The **ASD Interactive Bongos** is a Raspberry Pi-based system that transforms physical bongo drum interactions into visual and auditory feedback. When users press buttons (mapped to bongo drums), the system plays corresponding video content, creating an engaging, multi-sensory experience.

### Key Features

- 🥁 **Physical Interaction**: Large, accessible buttons mapped to bongo drums
- 🎬 **Visual Feedback**: Fullscreen video playback triggered by drum hits
- 💡 **LED Indicators**: Visual confirmation of button presses
- 🔄 **Immediate Response**: Low-latency feedback for cause-and-effect learning
- 🎯 **Simple Interface**: Minimal complexity, maximum engagement

## Benefits

### For Individuals with ASD

1. **Sensory Integration**
   - Combines tactile (button press), visual (video), and auditory (video sound) stimuli
   - Provides controlled, predictable sensory experiences
   - Helps develop sensory processing skills

2. **Motor Skills Development**
   - Encourages hand-eye coordination
   - Supports fine and gross motor skill practice
   - Provides immediate feedback for movement

3. **Cause-and-Effect Learning**
   - Clear, immediate connection between action (button press) and result (video playback)
   - Reinforces understanding of actions and consequences
   - Builds confidence through successful interactions

4. **Engagement and Motivation**
   - Interactive, game-like experience increases participation
   - Visual rewards maintain attention and interest
   - Customizable content allows for personalization

5. **Communication Support**
   - Non-verbal interaction method
   - Can be used as a communication tool or reward system
   - Encourages turn-taking and social interaction when used in groups

6. **Anxiety Reduction**
   - Predictable, structured interaction pattern
   - User-controlled experience reduces stress
   - Repetitive nature can be calming

### For Therapists and Caregivers

- **Therapeutic Tool**: Can be integrated into therapy sessions
- **Progress Tracking**: Monitor engagement and interaction patterns
- **Customizable Content**: Adapt videos to individual preferences and goals
- **Cost-Effective**: Uses affordable Raspberry Pi hardware

## Hardware Integration

### Components Required

- **Raspberry Pi** (Model 3B+ or newer recommended)
- **2x Tactile Push Buttons** (large, accessible buttons)
- **2x LEDs** (with appropriate resistors, typically 220Ω)
- **2x 220Ω Resistors** (for LED current limiting)
- **Jumper Wires** (for connections)
- **Breadboard** (optional, for prototyping)
- **Bongo Drums** (physical drums with buttons integrated)
- **Display/Monitor** (for video playback)
- **Speakers** (optional, for audio output)

### Hardware Connection Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    RASPBERRY PI                              │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  GPIO Pins (BCM Mode)                                 │  │
│  │                                                        │  │
│  │  GPIO 16 ────────────┐                                │  │
│  │  GPIO 26 ────────────┤                                │  │
│  │  GPIO 17 ────────────┤                                │  │
│  │  GPIO 27 ────────────┤                                │  │
│  │  GND ────────────────┤                                │  │
│  │  3.3V ───────────────┤                                │  │
│  └──────────────────────┼────────────────────────────────┘  │
│                         │                                    │
└─────────────────────────┼────────────────────────────────────┘
                          │
                          │
        ┌─────────────────┴─────────────────┐
        │                                   │
        ▼                                   ▼
┌───────────────┐                  ┌───────────────┐
│  LEFT DRUM    │                  │  RIGHT DRUM   │
│               │                  │               │
│  ┌─────────┐  │                  │  ┌─────────┐  │
│  │ BUTTON  │  │                  │  │ BUTTON  │  │
│  │ (GPIO17)│  │                  │  │ (GPIO27)│  │
│  └────┬────┘  │                  │  └────┬────┘  │
│       │       │                  │       │       │
│       │       │                  │       │       │
│  ┌────▼────┐  │                  │  ┌────▼────┐  │
│  │   LED   │  │                  │  │   LED   │  │
│  │ (GPIO16)│  │                  │  │ (GPIO26)│  │
│  └─────────┘  │                  │  └─────────┘  │
│               │                  │               │
└───────────────┘                  └───────────────┘
        │                                   │
        │                                   │
        └───────────┬───────────────────────┘
                    │
                    ▼
            ┌───────────────┐
            │  COMMON GND   │
            └───────────────┘
```

### Detailed Wiring Connections

#### Left Drum Circuit
```
Raspberry Pi          Left Drum Components
─────────────────────────────────────────────
GPIO 16 (OUT)  ──────► LED Anode (+)
                      LED Cathode (-) ────► 220Ω Resistor ────► GND

GPIO 17 (IN)   ──────► Button Terminal 1
3.3V           ──────► Button Terminal 2
                      (Button connects GPIO 17 to 3.3V when pressed)
```

#### Right Drum Circuit
```
Raspberry Pi          Right Drum Components
─────────────────────────────────────────────
GPIO 26 (OUT)  ──────► LED Anode (+)
                      LED Cathode (-) ────► 220Ω Resistor ────► GND

GPIO 27 (IN)   ──────► Button Terminal 1
3.3V           ──────► Button Terminal 2
                      (Button connects GPIO 27 to 3.3V when pressed)
```

### Physical Integration

The buttons and LEDs should be integrated into or mounted on the bongo drums:

1. **Button Placement**: Mount large, accessible buttons on the drum heads or sides
2. **LED Placement**: Position LEDs where they're visible but not distracting
3. **Wiring**: Route wires through the drum structure to keep them protected
4. **Power**: Ensure stable power supply for Raspberry Pi (recommended: 5V 3A power adapter)

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    USER INTERACTION                         │
│                                                             │
│              Press Left Button    Press Right Button       │
│                     │                     │                │
└─────────────────────┼─────────────────────┼────────────────┘
                      │                     │
                      ▼                     ▼
┌─────────────────────────────────────────────────────────────┐
│              RASPBERRY PI (bongos_controller.py)            │
│                                                              │
│  ┌──────────────────┐          ┌──────────────────┐         │
│  │  GPIO Handler    │          │  GPIO Handler    │         │
│  │  (Left Button)   │          │  (Right Button)  │         │
│  └────────┬─────────┘          └────────┬─────────┘         │
│           │                              │                   │
│           ▼                              ▼                   │
│  ┌──────────────────┐          ┌──────────────────┐         │
│  │  LED Controller  │          │  LED Controller  │         │
│  │  (GPIO 16)       │          │  (GPIO 26)       │         │
│  └──────────────────┘          └──────────────────┘         │
│           │                              │                   │
│           └──────────┬───────────────────┘                   │
│                      ▼                                       │
│           ┌──────────────────────┐                          │
│           │  Video Player        │                          │
│           │  (VLC Media Player)  │                          │
│           └──────────┬───────────┘                          │
│                      │                                       │
│                      ▼                                       │
│           ┌──────────────────────┐                          │
│           │  Video Files         │                          │
│           │  - left.mp4          │                          │
│           │  - right.mp4         │                          │
│           └──────────────────────┘                          │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    OUTPUT DEVICES                           │
│                                                              │
│         Display (Fullscreen Video)    Speakers (Audio)       │
└─────────────────────────────────────────────────────────────┘
```

## Installation

### Prerequisites

1. **Raspberry Pi OS** installed on your Raspberry Pi
2. **Python 3** (usually pre-installed)
3. **VLC Media Player** installed
4. **RPi.GPIO** library

### Step-by-Step Setup

1. **Update your system:**
   ```bash
   sudo apt update
   sudo apt upgrade -y
   ```

2. **Install VLC Media Player:**
   ```bash
   sudo apt install vlc -y
   ```

3. **Install Python GPIO library:**
   ```bash
   pip3 install RPi.GPIO
   ```

4. **Clone or download this repository:**
   ```bash
   git clone <repository-url>
   cd ASD-Interactive-Bongos
   ```

5. **Prepare video files:**
   - Place your video files in the project directory
   - Name them `left.mp4` and `right.mp4`
   - Ensure videos are in a format compatible with VLC

6. **Connect hardware** according to the wiring diagram above

7. **Run the controller:**
   ```bash
   python3 bongos_controller.py
   ```

## Usage

1. **Start the system:**
   ```bash
   python3 bongos_controller.py
   ```

2. **Interact with the bongos:**
   - Press the **left button** → Left LED lights up → Left video plays
   - Press the **right button** → Right LED lights up → Right video plays

3. **Stop the system:**
   - Press `Ctrl+C` to gracefully stop the program

### Customization

- **Change video files**: Replace `left.mp4` and `right.mp4` with your own videos
- **Modify GPIO pins**: Update the pin numbers in the script if using different pins
- **Adjust LED timing**: Modify the `time.sleep(0.3)` value to change LED duration
- **Add debounce time**: Adjust `bouncetime=600` to change button debounce period

## Requirements

### Software
- Python 3.6+
- RPi.GPIO library
- VLC Media Player
- Raspberry Pi OS (or compatible Linux distribution)

### Hardware
- Raspberry Pi (Model 3B+ or newer)
- 2x Tactile push buttons
- 2x LEDs (any color)
- 2x 220Ω resistors
- Jumper wires
- Breadboard (optional)
- Display/Monitor
- Speakers (optional)

## Contributing

We welcome contributions! Areas where help is needed:

- Additional sensory feedback options
- Support for more buttons/drums
- Web interface for content management
- Data logging and analytics
- Accessibility improvements
- Documentation improvements

Please feel free to submit issues, fork the repository, and create pull requests.

## License

This project is open source and available for educational and therapeutic use.

## Acknowledgments

- Designed with input from ASD therapy professionals
- Built for the autism community
- Inspired by the need for accessible, engaging therapeutic tools

---

**Note**: This tool is designed to support therapy and engagement but should be used as part of a comprehensive therapeutic approach. Consult with healthcare professionals for individualized recommendations.

