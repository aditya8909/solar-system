import cv2 
import numpy
img = cv2.imread("ss.jpg")

cv2.putText(img,
            "sun",
            (110,190),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,180)
            

           )
cv2.putText(img,
            "mercury",
            (150,90),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,0)
            

           )
cv2.putText(img,
            "venus",
            (200,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,0)
            

           )
cv2.putText(img,
            "earth",
            (230,90),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,0)
            

           )
cv2.putText(img,
            "mars",
            (255,230),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,0)
            

           )
cv2.putText(img,
            "jupiter",
            (330,90),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,0)
            

           )
cv2.putText(img,
            "saturn",
            (370,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,0)
            

           )
cv2.putText(img,
            "uranus",
            (430,90),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,0)
            

           )
cv2.putText(img,
            "neptune",
            (470,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,0)
            

           )
cv2.imshow("output",img)
cv2.waitKey(0)