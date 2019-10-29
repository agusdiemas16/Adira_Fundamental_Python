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

    def cari_motor_yang_sesuai(self):
        if self.gaji < 3000000:
            recomendation = 'BEAT'
        elif self.gaji >= 3000000 and self.gaji < 6000000:
            recomendation = 'VARIO'
        elif self.gaji >= 6000000 and self.gaji < 9000000:
            recomendation = 'N-MAX'
        else:
            recomendation = 'ADV'
        print(f'Motor yang cocok untuk {self.nama} untuk penghasilan sebesar {self.gaji} adalah motor {recomendation}')