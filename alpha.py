from __future__ import print_function
from pygarl.base import CallbackManager
from pygarl.classifiers import SVMClassifier
from pygarl.mocks import VerboseMiddleware
from pygarl.data_readers import SerialDataReader
from pygarl.predictors import ClassifierPredictor
from pygarl.sample_managers import DiscreteSampleManager
import pyautogui
from string import ascii_lowercase

MODEL_PATH="/home/reshu/Desktop/Minors/alphabet/model.svm"

PORT="/dev/ttyACM0"
#PORT="/dev/rfcomm2"

def receive_character(ascii_lowercase):
    #print(number)
    # pyautogui.click(29,116)
      #pyautogui.click(155,69)
      pyautogui.doubleClick(155,69)
      #pyautogui.mouseDown()
      #pyautogui.moveTo(125,166)
      #pyautogui.click(125,166)
     

     
      pyautogui.typewrite(ascii_lowercase)



#def receive_character(character):
    #if character != "D":
        #pyautogui.typewrite(character)
    #else:
        #pyautogui.keyDown('backspace')
        #pyautogui.keyUp('backspace')
         #pyautogui.typewrite(character)






# Create the SerialDataReader
sdr = SerialDataReader(PORT, expected_axis=6, verbose=False)

# Create the SampleManager
manager = DiscreteSampleManager()

# Attach the manager
sdr.attach_manager(manager)

# Create a classifier
classifier = SVMClassifier(model_path=MODEL_PATH)

# Load the model
classifier.load()

# Print classifier info
classifier.print_info()

# Create a ClassifierPredictor
predictor = ClassifierPredictor(classifier)

# Attach the classifier predictor
manager.attach_receiver(predictor)

# Create a CallbackManager
callback_mg = CallbackManager(verbose=True)

# Attach the callback manager
predictor.attach_callback_manager(callback_mg)


# Cycle through all characters to bind them
for c in ascii_lowercase:
    callback_mg.attach_callback(c, receive_character)


# Attach also space and delete characters
    #callback_mg.attach_callback(" ", receive_character)
#callback_mg.attach_callback("D", receive_character)



# Open the serial connection
sdr.open()
print("Opened!")

# Start the main loop
sdr.mainloop()






