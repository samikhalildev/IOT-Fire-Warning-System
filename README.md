# IOT-Fire-Warning-System

## Setup
1. Ensure Raspberry PI is connected to the same network
2. Ping raspberrypi to find the IP address
```
ping raspberrypi.local
```
3. Connect to the PI via SSH
```
ssh pi@address
```
4. Once connected succesfully, clone the project
```
git clone https://github.com/samikhalildev/IOT-Fire-Warning-System.git
cd IOT-Fire-Warning-System
```
5. Run Node red 
```
node-red
```
6. Open the browser and go to ip_address:1880 (Note the ip address is the one returned in step 2)
7. Import FDW.json into Node red to view the project flow
8. Click deploy and go to ip_address/ui to view the dashboard in the browser
