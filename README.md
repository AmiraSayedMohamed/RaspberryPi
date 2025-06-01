# RaspberryPi
This Repositery With Contain EveryThing Related to the raspberryPi
# Step By Step install Ultralytics on Raspberry Pi 4
- sudo apt update && sudo apt upgrade -y
- sudo apt install python3-pip -y
- pip3 install --upgrade pip setuptools
- sudo apt install libopenblas-dev libopencv-dev python3-opencv -y
- cd into your directory of the project
- sudo apt install python3-venv -y
- python3 -m venv yolovenv
- source yolovenv/bin/activate
- pip install ultralytics
  ### if he doesn't detect ultralytics although it was installes
  - go in the global path and write this command :
    ``` bash
pip install ultralytics --break-system-packages
``` 

