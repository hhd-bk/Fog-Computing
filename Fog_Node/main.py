# Import everything we need
# This run on fog node

import time

from get_img_from_cam import get_img
from find_ip_from_mac import find_ip
from tensorflow import keras

# Initialize
# MAC address of camera -> List of all devices in edge layer
cam_address = "50:8f:4c:58:71:ff"
# Load model for detecting fire
model = keras.models.load_model('model_1.h5')
# Run predicting or not
predict_flag = False

try:
    ip_cam = find_ip(cam_address)
    predict_flag = True
except:
    predict_flag = False
    print("Can't find camera ip address")
    print("Stop the program")

while(predict_flag):
    t1 = time.time()
    try:
        img = get_img(ip_cam)
    except:
        print("Can't get image from camera")
        break
    # Check if there is fire in the picture
    result = model.predict(img)
    t2 = time.time()
    print("Predicted value: ", result)
    print("Estiamted time:", t2-t1)
    # Write log file
    # Delay for 5 seconds
    # 5 second is enough for predicting fire
    time.sleep(5)


