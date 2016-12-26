#!/usr/bin/env python
from flask import Flask, render_template, Response

import cv2


cam = cv2.VideoCapture(0)
cam.set(3, 320)
cam.set(4, 240)

app = Flask(__name__)

def get_frame(camera):
	frame = camera.read()[1]
	jpeg = cv2.imencode('.jpg', frame)[1]
	frame = jpeg.tobytes()
	return frame

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:        
        frame = get_frame(camera)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(cam), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host="localhost", port = 8000, threaded=True)
