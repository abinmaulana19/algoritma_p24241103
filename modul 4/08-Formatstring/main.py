# format string

"""
string : kumpulan dari karakter
cara membuat string :
1. dengan single qoute '...'
2. dengan double qoute "..."
    
"""

# membuat string dengan single qoute
nama = 'nama saya doo'
print(nama)

# membuat string dengan double qoute
nama = "nama saya diar"
print(nama)

# jika mau tanda single qoute
# pakai \
print('g\day')
print('what\sUp!')

# contoh gunakan slashh \
print('C:\\user\\abin')

nama = "abin"
print("selamat datang", nama)

# format string 'f' dan '{}
format_str = f'selamat datang = {nama}'
print(format_str)

# format string angka
angka = 2005.5
format_str = f'angka = {angka}'
print(format_str)

# format string angka ribuan
angka = 20000
format_str = f'jutaan = {angka}'
print(format_str)

# bilangan desimal 
angka = 2005.54321
format_str = f'desimal = {angka}'
print(format_str)

# persen 
angka = 0.55 # 0.55 * 100 = 55%
format_str = f'persen = {angka:.1%}'
print(format_str)

# opoerasi aritmatika dengan format string
harga = 57250
jumlah = 3

print(f'total bayar : {harga*jumlah:,}')