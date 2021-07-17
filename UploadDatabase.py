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
# db.push(gambiran)

bhayangkara = {
    'nama_rumah_sakit' : 'Rumah Sakit Bhayangkara Kediri',
    'alamat' : "Jl. Kombes Pol Duryat No.17, Dandangan, Kediri",
    'nomer_telepon' : "6285608845319"
}
# db.push(bhayangkara)

baptis = {
    'nama_rumah_sakit' : 'Rumah Sakit Baptis Kediri',
    'alamat' : "Jl. Bridgjend Pol. IBH Pranoto No.1-7, Bangsal, Pesantren",
    'nomer_telepon' : "6282131949778"
}
# db.push(baptis)

slg = {
    'nama_rumah_sakit' : 'RSUD Simpang Lima Gumul',
    'alamat' : "Jl. Galuh Candrakirana, Tugurejo, Kec. Ngasem, Kediri",
    'nomer_telepon' : "628980341546"
}
# db.push(slg)

ratih = {
    'nama_rumah_sakit' : 'Rumah Sakit Umum Ratih',
    'alamat' : "Jl. Penanggungan, Bandar Lor, Kec. Mojoroto, Kota Kediri",
    'nomer_telepon' : "6282131949778"
}
# db.push(ratih)

AuraShifa = {
    'nama_rumah_sakit' : 'Rumah Sakit Aura Shifa',
    'alamat' : "Jl. Joyoboyo Dlopo No.42, Karangrejo, Kec. Ngasem, Kediri",
    'nomer_telepon' : "6285608845319"
}
# db.push(AuraShifa)

dkt = {
    'nama_rumah_sakit' : 'Rumah Sakit DKT Kediri',
    'alamat' : "Jl. Mayjend Sungkono No.44, Semampir, Kec. Kota Kediri",
    'nomer_telepon' : "628980341546"
}
# db.push(dkt)

dina = {
    'nama_rumah_sakit' : 'Rumah Sakit Dina. L',
    'alamat' : "Jl. Hayam Wuruk No.90, Dandangan, Kec. Kota Kediri",
    'nomer_telepon' : "6282131949778"
}
# db.push(dina)

citra = {
    'nama_rumah_sakit' : 'Rumah Sakit Citra Keluarga',
    'alamat' : "Jl. Urip Sumoharjo No.189, Ngronggo, Kec. Kota Kediri",
    'nomer_telepon' : "6285608845319"
}
# db.push(citra)

muh = {
    'nama_rumah_sakit' : 'Rumah Sakit Muhammadiyah Ahmad Dahlan',
    'alamat' : "Jl. Gatot Subroto No.84, Mrican, Kec. Mojoroto, Kediri",
    'nomer_telepon' : "6285608845319"
}
db.push(muh)
