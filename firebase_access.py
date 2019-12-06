import pyrebase
import slider
import threading

firebaseConfig = {
    "apiKey": "AIzaSyDR4MYczuwRwAq0gmAyNHl_kURK3UmWlYs",
    "authDomain": "questio-a802f.firebaseapp.com",
    "databaseURL": "https://questio-a802f.firebaseio.com",
    "projectId": "questio-a802f",
    "storageBucket": "questio-a802f.appspot.com",
    "messagingSenderId": "57510774469",
    "appId": "1:57510774469:web:ab847710cf70c19026d2ac",
    "measurementId": "G-02H2ZTQ7HW"
  }

firebase = pyrebase.initialize_app(firebaseConfig)

# Get a reference to the database service
db = firebase.database()

def checkFirebaseValue(childName):
    user = db.child("Hardware_Interface").child(childName).get()
    return user.val()

def setFirebaseValue():
  db.child("Hardware_Interface").update({state:value})

class asyncSetFirebaseSliderValue():
    def __init__(self):
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()
    def run(self):
        db.child("Hardware_Interface").update({"Current_Slider_Value", slider.getLevel()})