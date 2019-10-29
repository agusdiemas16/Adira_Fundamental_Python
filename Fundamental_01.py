"""
Author : Agus Diemas Prayoga
Purpose : Fundamental of Python

Green -> File yang belum di GitHub
Blue -> File yang ada di GitHub dan telah diedit di IDE
Black -> File yang ada di Github dan belum diedit
"""
print('Fundamental Python')

"""
Fundamental ada 3 :
- Sequential
- Branching -> Condition
- Loop / Perulangan
- Tipe Data Penting: List(Array) dan Dictionary (/json)
- Modularization :
    - Dengan Fungsi
    - Dengan Class
    - Dengan Package
    
Kasus : Advis jenis motor bagi customer tertentu

Nama Program:
Customer Advisor Management System -> CAMS


"""

versi = '0.1'
nama_program = 'Customer Advisor Management System'
author = 'Agus Diemas Prayoga'

#Tipe data Enumerasi, Konstanta umumnya huruf besar(bukan hal wajib)
PRIA, WANITA = range(2)
NON_FIX, FIX = range(2)

customer1_nama = 'Agus'
customer1_jenis_kelamin = PRIA
customer1_gaji = 3000000
customer1_existing = True
customer1_occupation = FIX
customer1_alamat = {
    'Line 1': 'Cluster Edison Summarecon Serpong',
    'Kelurahan' : 'Tanggerang Selatan',
    'City' : 'Gading Serpong',
    'Province' : 'Banten',
    'Zipcode' : '15310',
    'Country' : 'Indonesia'
}

customer2_nama = 'Diemas'
customer2_jenis_kelamin = WANITA
customer2_gaji = 6000000
customer2_existing = False
customer2_occupation = NON_FIX
customer2_alamat = {
    'Line 1': 'Jalan Kenanga Atas',
    'Kelurahan' : 'Koba',
    'City' : 'Koba',
    'Province' : 'Bangka Belitung',
    'Zipcode' : '33181',
    'Country' : 'Indonesia'
}

customer3_nama = 'Prayoga'
customer3_jenis_kelamin = PRIA
customer3_gaji = 9000000
customer3_existing = True
customer3_occupation = FIX
customer3_alamat = {
    'Line 1': 'Buana gardenia',
    'Kelurahan' : 'Pinang',
    'City' : 'Tanggerang',
    'Province' : 'Banten',
    'Zipcode' : '15310',
    'Country' : 'Indonesia'
}

#f for format print {}
print(f'{nama_program} versi {versi} oleh {author}')

print('')

#Pengecekan Existing atau tidak
if customer1_existing:
    print(f'{customer1_nama} sudah pernah memiliki pinjaman')
else: print(f'{customer1_nama} belum pernah memiliki pinjaman')

if customer2_existing:
    print(f'{customer2_nama} sudah pernah memiliki pinjaman')
else: print(f'{customer2_nama} belum pernah memiliki pinjaman')

if customer3_existing:
    print(f'{customer3_nama} sudah pernah memiliki pinjaman')
else: print(f'{customer3_nama} belum pernah memiliki pinjaman')

print('')

#Condition / Segment Buat Gaji
if customer1_gaji < 3000000:
    print(f'Gaji {customer1_nama} lebih kecil dari 3 Juta')
elif customer1_gaji >= 3000000 and customer1_gaji < 6000000:
    print(f'Gaji {customer1_nama} Kelas Menengah')
elif customer1_gaji >= 6000000 and customer1_gaji < 9000000:
    print(f'Gaji {customer1_nama} Kelas Atas')
else : print(f'Gaji {customer1_nama} Kelas Dewa')

if customer2_gaji < 3000000:
    print(f'Gaji {customer2_nama} lebih kecil dari 3 Juta')
elif customer2_gaji >= 3000000 and customer2_gaji < 6000000:
    print(f'Gaji {customer1_nama} Kelas Menengah')
elif customer2_gaji >= 6000000 and customer2_gaji < 9000000:
    print(f'Gaji {customer2_nama} Kelas Atas')
else : print(f'Gaji {customer2_nama} Kelas Dewa')

if customer3_gaji < 3000000:
    print(f'Gaji {customer3_nama} lebih kecil dari 3 Juta')
elif customer3_gaji >= 3000000 and customer3_gaji < 6000000:
    print(f'Gaji {customer3_nama} Kelas Menengah')
elif customer3_gaji >= 6000000 and customer3_gaji < 9000000:
    print(f'Gaji {customer3_nama} Kelas Atas')
else : print(f'Gaji {customer3_nama} Kelas Dewa')

print('')

#Menampilkan All Nama Customer
List_Nama = [customer1_nama, customer2_nama, customer3_nama]
print('Daftar Nama Customer : ')
for i in range (0, len(List_Nama)):
    print(f'{i+1}. {List_Nama[i]}')

print('')

#Print Alamat
print(f'Alamat dari {customer1_nama} adalah di : ')
print(customer1_alamat['Line 1'])
print(customer1_alamat['Kelurahan'])
print(customer1_alamat['City'])
print(customer1_alamat['Province'])
print(customer1_alamat['Zipcode'])
print(customer1_alamat['Country'])

