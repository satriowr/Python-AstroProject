import pyrebase
from datetime import datetime

now = datetime.now() 
tanggal = now.strftime("%Y-%m-%d")
jam = now.strftime("%H:%M")

config = {
    "apiKey" : "AIzaSyDkFn3LdpjPly4w31eL6CAQIktzSclaMg0",
    "authDomain" : "astroapp-cbf26.firebaseapp.com",
    "databaseURL" : "https://astroapp-cbf26-default-rtdb.firebaseio.com",
    "projectId" : "astroapp-cbf26",
    "storageBucket" : "astroapp-cbf26.appspot.com",
    "serviceAccount" : "D:\satrio\Python-SignLangDetection\serviceAccAstro.json"
}

firebaseConnect = pyrebase.initialize_app(config)
db = firebaseConnect.database()
db.child("Status Pasien")

dataDummy1 = {
    "kondisi" : "Aman",
    "tanggal" : tanggal,
    "jam" : jam
}
# db.push(dataDummy1)

dataDummy2 = {
    "kondisi" : "Jatuh Depan",
    "tanggal" : tanggal,
    "jam" : jam
}
# db.push(dataDummy2)

dataDummy3 = {
    "kondisi" : "Jatuh Belakang",
    "tanggal" : tanggal,
    "jam" : jam
}
# db.push(dataDummy3)

