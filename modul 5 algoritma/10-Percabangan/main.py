# percabangan 
# menggunakan statment if

# struktur 
"""
   1. if-nya
   2. ada kondisi (bernilai TRUE/FALSE)
   3. ada aksi -> proses lanjutan 
"""

nama = input("Masukan Nama Anda = ")

# IF Statement dalam bentuk inline (satu baris)
if nama == "mayzy": print (f"selamat datang{nama}")
print("terimah kasih")

# if statement dalam bentuk indentasi
if nama == 'mayzy':
    print(f'selamat datang {nama}') 
print("terimah kasih")

# iF-ELSE Statement 
if nama == 'mayzy':
   # aksi 1
   print(f'selamat datang {nama}')
else:
    # aksi 2
    print(f'kamu{nama}')
print('terimah kasih')
