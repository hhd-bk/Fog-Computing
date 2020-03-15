import requests
import cv2
import time
import numpy as np

def get_img(ip_address):
    url = "http://"+ ip_address + ":8080/shot.jpg"
    response = requests.get(url)
    # Decode to get image from byte value
    img = np.array(bytearray(response.content), dtype=np.uint8)
    img = cv2.imdecode(img, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Resize to feed to the network
    img = cv2.resize(img, (50, 50))
    # Save image
    local_time = time.asctime(time.localtime(time.time()))
    cv2.imwrite("images\\%s.jpg" %local_time, img)
    # Reshape for input the model
    img = np.array([img])
    return img