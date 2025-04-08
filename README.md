# Traffic-Penalty-System [![Deployed](https://img.shields.io/badge/Hosted_on-Azure-blue?logo=windows)](https://trafficpenaltysystemsk17.azurewebsites.net/)  ![Status completed](https://img.shields.io/badge/Status-finished-2eb3c1.svg) ![Django 5.2](https://img.shields.io/badge/Django-5.2-green.svg) ![Python 3.10.2](https://img.shields.io/badge/Python-3.10.2-blue.svg)
----------------------------
ABOUT THE PROJECT
----------------------------

This project provides the features of a traffic penalty system.
The traffic police can use a MFRC522 sensor used with Raspberry Pi 3B and 
add the details of the challan on the spot which will be sent to the 
website which has the driver's details like username, rfid, etc. 
along with the status of the challan.

🚀 **Hosted at:** [https://trafficpenaltysystemsk17.azurewebsites.net/](https://trafficpenaltysystemsk17.azurewebsites.net/)

----------------------------
TECHNOLOGIES USED
----------------------------

For traffic police to enter challan details on spot:
- Raspberry Pi 3B
- MFRC522 Sensor
- RFID tags

For traffic police and user to see the status of all challans/users on website:
- Python 3.10.2
- Django 5.2
- SQLLite
- Bootstrap ( HTML / CSS / Javascript )

----------------------------
INSTRUCTIONS TO RUN THE PROJECT
----------------------------

Type the following commands in sequential order:

              python3 -m venv venv      (To create virtual environment)
              source env/bin/activate      (To activate virtual environment)
              pip install -r requirements.txt
              python3 manage.py migrate
              python3 manage.py runserver  

To deactivate the virtual environment:

              deactivate               

----------------------------
# Traffic Penalty System
----------------------------

This folder contains the configuration information of the project.

----------------------------
# Penalty Manager
----------------------------

This folder contains the website application. This website
has APIs which Raspberry Pi 3B + MFRC522 Sensor can 
communicate with and store the user challan details. User
can login to the website and see the status of all challans.

----------------------------
# Raspi RFID System
----------------------------

This folder contains the hardware related application. 
MFRC522 Sensor + Raspberry Pi 3B can identify the user 
RFID tags and then the traffic police can enter 
appropriate details of challan and see the status of 
user challans as well in the display.

----------------------------
