# Stepper-Motor
Controlling​ ​Stepper​ ​Motor​ ​Direction​ ​and​ ​Speed With Raspberry Pi

This project was done for PC/CP320 Class at WLU. 

## Project Description

This project was set to test our understanding of converting output from a sensor to a voltage which falls within a specified range, and accordingly, we control an actuator from an input signal conditioned based on the instructions we write in our software. We used an ADC to convert the analog signals we receive from Hall effect sensor and Infrared distance measuring sensor to digital signals and then pass it to the Raspberry pi. Hall-effect sensor is used to
switch the stepper motor direction based on a change of a magnetic flux of a permanent magnet, and then we display a character “R” or “L” - Right or Left- on a 7-Segment. We also used an Infrared distance measuring sensor to control the speed of the stepper motor based on the measured distance.

## Hardware 

### Inputs
#### 1- Hall-effect sensor (Analog Output)

UGN3503U

4.5 V to 6 V

The sensor tracks extremely small changes in magnetic flux density, we use a permanent magnet to change the reading of the sensor, then according to this change whether it’s the south or the north side of the magnet, we switch the motor direction.

<img width="130" alt="Screen Shot 2021-07-11 at 3 07 52 AM" src="https://user-images.githubusercontent.com/47288950/125185913-b13b7d80-e227-11eb-8ac9-a08733fe672b.png">

#### 2- Infrared distance measuring sensor (Analog Output)

GP2Y0A21YK

4.5 V to 5.5 V

This sensor sends an IR rays to hit an object and then receives it back to measure the distance. We are using this feature to control the speed of the motor based on the measured distance.

<img width="185" alt="Screen Shot 2021-07-11 at 3 07 56 AM" src="https://user-images.githubusercontent.com/47288950/125185934-bf899980-e227-11eb-8186-ff8a3adf5e62.png">


### Outputs

#### 1- Stepper Motor (PWM Input)

28BYJ-48

5V

Stepper motor moves in accurate, fixed angle increments known as steps. The motor has 4 coils of wire that are powered in a sequence to make the magnetic motor shaft spin.

<img width="196" alt="Screen Shot 2021-07-11 at 3 08 02 AM" src="https://user-images.githubusercontent.com/47288950/125185940-c4e6e400-e227-11eb-8469-776f4d980ec2.png">


#### 2- 7-Segment Display (Digital Input)

NES-5011

2.1 V to 2.5 V

7-segment numeral device provide seven corresponding outputs, so we can create number by combining those outputs together.

<img width="166" alt="Screen Shot 2021-07-11 at 3 08 06 AM" src="https://user-images.githubusercontent.com/47288950/125185944-c9ab9800-e227-11eb-9bbc-d187abddaaf3.png">


#### 3- Analog to Digital converter (Analog input -> Digital Output)

MCP3008

2.7V - 5.5V

SPI serial interface

<img width="161" alt="Screen Shot 2021-07-11 at 3 08 10 AM" src="https://user-images.githubusercontent.com/47288950/125185949-cdd7b580-e227-11eb-81eb-f8cbd0d0314a.png">

