# AirStylus

*Hand gesture monitored gadget*

The general idea is that a user would just press the button and hold it down while dragging the pointer across the
letters in the desired word before releasing the button to complete the word. 
This can be implemented on touch devices simply as touch tracer.
The stylus should be able to determine which word was swiped by the path of the input and possibly other variables such as speed and change of
direction.


- wireless, low power, no need of screen in front
- Machine Learning, GUI


Sensor Used:
- MPU6050(Accelerometer+Gyroscope)

    
Dependencies Used:
- Python 2.7
  - Pyautogui
  - TKinter
  - DLib

Model is first trained using a classifier and stored.
Then predicts the movement of sensor data movement on test data.



