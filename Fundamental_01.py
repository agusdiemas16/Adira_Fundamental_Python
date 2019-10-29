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

customer2_nama = 'Diemas'
customer2_jenis_kelamin = WANITA
customer2_gaji = 6000000
customer2_existing = False
customer2_occupation = NON_FIX

customer3_nama = 'Prayoga'
customer3_jenis_kelamin = PRIA
customer3_gaji = 9000000
customer3_existing = True
customer3_occupation = FIX

#f for format print {}
print(f'{nama_program} versi {versi} oleh {author}')

if customer1_existing:
    print(f'{customer1_nama} sudah pernah memiliki pinjaman')

if customer2_existing:
    print(f'{customer2_nama} sudah pernah memiliki pinjaman')
else: print(f'{customer2_nama} belum pernah memiliki pinjaman')

if customer3_existing:
    print(f'{customer3_nama} sudah pernah memiliki pinjaman')





