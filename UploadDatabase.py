import pyrebase

#config Firebase
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
db.child("Data Rumah Sakit")

gambiran = {
    'nama_rumah_sakit' : 'Rumah Sakit Gambiran 2 Kediri',
    'alamat' : "Jl. Kapten Tendean No.16, Pakunden, Pesantren",
    'nomer_telepon' : "628980341546"
}

bhayangkara = {
    'nama_rumah_sakit' : 'Rumah Sakit Bhayangkara Kediri',
    'alamat' : "Jl. Kombes Pol Duryat No.17, Dandangan, Kediri",
    'nomer_telepon' : "6285608845319"
}

baptis = {
    'nama_rumah_sakit' : 'Rumah Sakit Baptis Kediri',
    'alamat' : "Jl. Bridgjend Pol. IBH Pranoto No.1-7, Bangsal, Pesantren",
    'nomer_telepon' : "6282131949778"
}

# db.push(gambiran)
# db.push(bhayangkara)
db.push(baptis)

