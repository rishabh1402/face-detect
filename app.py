import os
from flask import Flask, render_template, redirect, url_for, Response, request, session,send_file
import cv2

app = Flask(__name__,template_folder='templates')
BASE_PATH = os.getcwd()
UPLOAD_PATH = os.path.join(BASE_PATH,'static/upload/')

def get_frame(path,filename):
    # face detector initialized   
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        # get/read the image
        img = cv2.imread(path)
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

        text = cv2.putText(img, "Total Faces Detected : " + str(count), (45, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        return text
         
    

@app.route('/')
def home():
        return render_template("index.html")
    
@app.route('/success' , methods = ['GET' , 'POST'])
def success():
  if request.method == 'POST':
    upload_file = request.files['file']
    filename = upload_file.filename
    path_save = os.path.join(UPLOAD_PATH,filename)
    upload_file.save(path_save)
    text = get_frame(path_save,filename)

    return render_template('success.html',img=filename,text_h=text)
  return render_template('index.html',upload=False)

if __name__ == "__main__":
    app.run(debug=True)
