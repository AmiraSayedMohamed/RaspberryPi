# Is code is to open your Raspberry Pi camera
# Run this code into your Geany IDE , run Using the icon send or
# Or using this command in the terminal :  python3 test.py , where test is the name of the file
# Or you can also run the camera automatically from the terminal using libcamera library
# To open Camera Using libCameraLibrary First install the library using this command : 
# ( sudo apt install -y libcamera-apps ) , Then open Camera Using this command:( libcamera-hello )
# ---------------------------------------------------
# Here it's also some command also you need for depugging the camera:
# sudo apt update
# sudo apt full-upgrade -y
# sudo rpi-update
# sudo reboot
# libcamera-hello --list-cameras
# dmesg | grep camera


from picamera2 import Picamera2
import cv2

# Initialize Picamera2
picam2 = Picamera2()
picam2.preview_configuration.main.size = (1280, 720)
picam2.preview_configuration.main.format = "RGB888"
picam2.configure("preview")

picam2.start()

while True:
    frame = picam2.capture_array()

    # Show the live feed
    cv2.imshow("Raspberry Pi Camera - Live Feed", frame)

    # Press 'q' to exit the live feed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cv2.destroyAllWindows()
picam2.stop()
