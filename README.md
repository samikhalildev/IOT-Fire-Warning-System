# IOT-Fire-Warning-System
This project is part of a group assignment where we had to design and implement a smart fire detection system using Internet of Things technologies. The hardware components consists of a Raspberry Pi Zero W and Enviro pHAT. This system is able to detect and monitor environmental parameters such as temperature/humidity changes, as well as generate alarms/alerts when these parameters go above a predetermined threshold.

## Setup
1. Ensure Raspberry PI is connected to the same network
2. Ping raspberrypi to find the IP address
  ```sh
     ping raspberrypi.local
  ```
3. Connect to the PI via SSH
```sh
   ssh pi@address
```
4. Once connected succesfully, clone the project
```sh
   git clone https://github.com/samikhalildev/IOT-Fire-Warning-System.git
   cd IOT-Fire-Warning-System
```

5. Ensure that you have Node JS, node-red, sqlite3 and git installed on the PI

6. Run Node red
```sh
   node-red
```
6. Open the browser and go to "ip_address:1880" (Note the ip address is the one returned in step 2)
7. Import FDW_flow.json into Node red to view the project flow
8. Click deploy and go to "ip_address/ui" to view the dashboard in the browser
