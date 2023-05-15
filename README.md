# Ultrasonic sensor code
##### Why is it created?: 
    This code has written to determine a robot's movement by an ultrasonic sensor. 

_In this code to get input from user is preferred instead of ultrasonic sensor. So the user acts like sensor._
* First the program asks to user the data of ultrasonic sensor. 
* Then the data is added a list and this list is provided to be 20 data buy removing the oldest one. 
* After that average of 20 data is calculated. If result is less than 10 cm the robot stops to move. If it is not robot continues to move.
