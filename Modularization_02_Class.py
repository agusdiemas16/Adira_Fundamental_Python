"""
OOP = Object Oriented Programming
OOP :
    - Enkapsulation -> Membuat Class yang terdiri dari variable dan fungsi
    - Inheritance -> encapsulation dari class yang sudah ada
    - Polymorphism -> Bentuk yang sama, akan beraksi berbeda tergantung class anaknya(inheritance)
"""

#Encapsulation
PRIA, WANITA = range(2)
NON_FIX, FIX = range(2)

#Customer Class
class Customer:
    def __init__(self, nama, jenis_kelamin, gaji, existing, occupation, alamat): #Constructor
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.gaji = gaji
        self.existing = existing
        self.occupation = occupation
        self.alamat = alamat

    def __str__(self):
        return f'{self.nama} bergaji {self.gaji}'

    def __repr__(self): #dibutuhkan tipe data string unicode
        return f'{self.nama} bergaji {self.gaji}'

    def check_status_peminjaman(self):
        if self.existing:
            print(f'{self.nama} sudah pernah memiliki pinjaman')
        else:
            print(f'{self.nama} belum pernah memiliki pinjaman')

    def check_gaji(self):
        if self.gaji < 3000000:
            status = 'lebih kecil dari 3 Juta'
        elif self.gaji >= 3000000 and self.gaji < 6000000:
            status = 'Kelas Menengah'
        elif self.gaji >= 6000000 and self.gaji < 9000000:
            status = 'Kelas Atas'
        else:
            status = 'Kelas Dewa'
        print(f'Gaji {self.nama} {status}, yaitu sebesar {self.gaji}')

#Make Object From Class Customer
customer1 = Customer('Agus', PRIA, 3000000, True, FIX, {
    'Line 1': 'Cluster Edison Summarecon Serpong',
    'Kelurahan': 'Tanggerang Selatan',
    'City': 'Gading Serpong',
    'Province': 'Banten',
    'Zipcode': '15310',
    'Country': 'Indonesia'
})

customer2 = Customer('Diemas', WANITA, 6000000, False, NON_FIX, {
    'Line 1': 'Jalan Kenanga Atas',
    'Kelurahan': 'Koba',
    'City': 'Koba',
    'Province': 'Bangka Belitung',
    'Zipcode': '33181',
    'Country': 'Indonesia'
})

customer3 = Customer('Prayoga', PRIA, 9000000, True, FIX, {
    'Line 1': 'Buana gardenia',
    'Kelurahan': 'Pinang',
    'City': 'Tanggerang',
    'Province': 'Banten',
    'Zipcode': '15310',
    'Country': 'Indonesia'
})

print(customer1)
print(customer2)
print(customer3)

print('')

#print(customer1.nama)
#print(customer1.alamat['Line 1'])

customer1.check_status_peminjaman()
customer1.check_gaji()

print('')

#Inheritance & Polymorphism
class CustomerBandel(Customer):
    def __str__(self):
        return f'{self.nama} adalah customer bandel ( {Customer.__str__(self)} )'

    def __repr__(self):  # dibutuhkan tipe data string unicode
        return f'{self.nama} adalah customer bandel ( {Customer.__repr__(self)} )'

customerX = CustomerBandel('XXX', WANITA, 1000, False, NON_FIX, {})

print(customerX)