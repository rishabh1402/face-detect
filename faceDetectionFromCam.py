import cv2

# faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

class Video(object):
    def get_frame(self):
         # face detector initialized   
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        # get/read the image
        img = cv2.imread('faces.jpg', 1)
        # print(img)  # check if image read successfully

        # detect face by decreasing the scaleFactor by 1.05
        faces = faceCascade.detectMultiScale(img, scaleFactor=1.05, minNeighbors=5)

        # initial no. of faces = 0
        count = 0
        # draw a rectangle around the detected face
        for (x, y, w, h) in faces:
            # draw rectangle around face
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # increment face count upon detection
            count += 1
            # print text on screen (Face No. : )
            cv2.putText(img, "Face No." + str(count), (x-10, y-10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2) # color format : BGR

        cv2.putText(img, "Total Faces Detected : " + str(count), (45, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # open window for showing the o/p
        cv2.imshow('pic', img)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
