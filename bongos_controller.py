import RPi.GPIO as GPIO
import time
import subprocess
import os

# ==============================
# GPIO SETUP (BCM numbering)
# ==============================
LEFT_LED = 16
RIGHT_LED = 26
LEFT_BUTTON = 17
RIGHT_BUTTON = 27

# ==============================
# VIDEO FILES (LOCAL)
# ==============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LEFT_VIDEO = os.path.join(BASE_DIR, "left.mp4")
RIGHT_VIDEO = os.path.join(BASE_DIR, "right.mp4")

GPIO.setmode(GPIO.BCM)

GPIO.setup(LEFT_LED, GPIO.OUT)
GPIO.setup(RIGHT_LED, GPIO.OUT)

GPIO.setup(LEFT_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RIGHT_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("✅ Raspberry Pi Bongos Controller Running")
print("LEFT button  → LEFT video")
print("RIGHT button → RIGHT video\n")

# ==============================
# HELPER: PLAY VIDEO
# ==============================
def play_video(video_path):
    subprocess.Popen([
        "vlc",
        "--play-and-exit",
        "--fullscreen",
        video_path
    ])

# ==============================
# CALLBACKS
# ==============================
def left_button_pressed(channel):
    print("🟥 LEFT BUTTON PRESSED → Playing LEFT video")
    GPIO.output(LEFT_LED, GPIO.HIGH)
    play_video(LEFT_VIDEO)
    time.sleep(0.3)
    GPIO.output(LEFT_LED, GPIO.LOW)

def right_button_pressed(channel):
    print("🟦 RIGHT BUTTON PRESSED → Playing RIGHT video")
    GPIO.output(RIGHT_LED, GPIO.HIGH)
    play_video(RIGHT_VIDEO)
    time.sleep(0.3)
    GPIO.output(RIGHT_LED, GPIO.LOW)

# ==============================
# EVENT DETECTION
# ==============================
GPIO.add_event_detect(
    LEFT_BUTTON,
    GPIO.FALLING,
    callback=left_button_pressed,
    bouncetime=600
)

GPIO.add_event_detect(
    RIGHT_BUTTON,
    GPIO.FALLING,
    callback=right_button_pressed,
    bouncetime=600
)

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("\n🛑 Program stopped")

finally:
    GPIO.cleanup()