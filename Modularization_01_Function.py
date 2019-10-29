"""
Modularisasi ada 3:
- Function
- Class
- Package
"""

versi = '0.15'
nama_program = 'Customer Advisor Management System'
author = 'Agus Diemas Prayoga'

# Tipe data Enumerasi, Konstanta umumnya huruf besar(bukan hal wajib)
PRIA, WANITA = range(2)
NON_FIX, FIX = range(2)

customer1_nama = 'Agus'
customer1_jenis_kelamin = PRIA
customer1_gaji = 3000000
customer1_existing = True
customer1_occupation = FIX
customer1_alamat = {
    'Line 1': 'Cluster Edison Summarecon Serpong',
    'Kelurahan': 'Tanggerang Selatan',
    'City': 'Gading Serpong',
    'Province': 'Banten',
    'Zipcode': '15310',
    'Country': 'Indonesia'
}

customer2_nama = 'Diemas'
customer2_jenis_kelamin = WANITA
customer2_gaji = 6000000
customer2_existing = False
customer2_occupation = NON_FIX
customer2_alamat = {
    'Line 1': 'Jalan Kenanga Atas',
    'Kelurahan': 'Koba',
    'City': 'Koba',
    'Province': 'Bangka Belitung',
    'Zipcode': '33181',
    'Country': 'Indonesia'
}

customer3_nama = 'Prayoga'
customer3_jenis_kelamin = PRIA
customer3_gaji = 9000000
customer3_existing = True
customer3_occupation = FIX
customer3_alamat = {
    'Line 1': 'Buana gardenia',
    'Kelurahan': 'Pinang',
    'City': 'Tanggerang',
    'Province': 'Banten',
    'Zipcode': '15310',
    'Country': 'Indonesia'
}

# f for format print {}
print(f'{nama_program} versi {versi} oleh {author}')

print('')

# Make Function Check Existing
def check_status_peminjaman(nama, is_existing):
    if is_existing:
        print(f'{nama} sudah pernah memiliki pinjaman')
    else:
        print(f'{nama} belum pernah memiliki pinjaman')

check_status_peminjaman(customer1_nama, customer1_existing)
check_status_peminjaman(customer2_nama, customer2_existing)
check_status_peminjaman(customer3_nama, customer3_existing)

print('')

# Make Function Check Range Gaji
"""
def check_gaji(nama, gaji):
    if gaji < 3000000:
        print(f'Gaji {nama} lebih kecil dari 3 Juta, yaitu sebesar {gaji}')
    elif gaji >= 3000000 and gaji < 6000000:
        print(f'Gaji {nama} Kelas Menengah, yaitu sebesar {gaji}')
    elif gaji >= 6000000 and gaji < 9000000:
        print(f'Gaji {nama} Kelas Atas, yaitu sebesar {gaji}')
    else : print(f'Gaji {nama} Kelas Dewa, yaitu sebesar {gaji}')
"""

def check_gaji(nama, gaji):
    if gaji < 3000000:
        status = 'lebih kecil dari 3 Juta'
    elif gaji >= 3000000 and gaji < 6000000:
        status = 'Kelas Menengah'
    elif gaji >= 6000000 and gaji < 9000000:
        status = 'Kelas Atas'
    else : status = 'Kelas Dewa'
    print(f'Gaji {nama} {status}, yaitu sebesar {gaji}')

check_gaji(customer1_nama, customer1_gaji)
check_gaji(customer2_nama, customer2_gaji)
check_gaji(customer3_nama, customer3_gaji)

print('')
