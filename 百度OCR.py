import cv2
import sys
from aip import AipOcr

APP_ID = '16992070'
API_KEY = 'mHZB3i5dkSFuVsdlALE5KiE6'
SECRET_KEY = 'CPKgzFBVCZPnXNdrb6pMHO4ic9dSpUEF'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

fname = sys.path[0] + "/Test.png"

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content(fname)

results = client.general(image)["words_result"]

# img = cv2.imread(fname)
for result in results:
    text = result["words"]
    location = result["location"]
    print(text)
    # cv2.rectangle(img, (location["left"],location["top"]), (location["left"]+location["width"],location["top"]+location["height"]), (0,255,0), 2)
# cv2.imwrite(fname[:-4]+"_result.jpg", img)