import os

class Acara:
    def __init__(self):
        self.acara_peserta = []

    def clear(self):
        input('Press Enter to continue')
        os.system('cls')

    def daftar_peserta(self, nama_peserta, nama_acara):
        self.acara_peserta.append((nama_peserta, nama_acara))
        print(f"{nama_peserta} berhasil mendaftar untuk {nama_acara}.")
        self.clear()

    def cari_peserta(self, nama_peserta):
        peserta_terdaftar = [(peserta, acara) for peserta, acara in self.acara_peserta if peserta == nama_peserta]
        if peserta_terdaftar:
            for peserta, acara in peserta_terdaftar:
                print(f"{peserta} terdaftar untuk {acara}.")
        else:
            print(f"{nama_peserta} tidak terdaftar untuk acara apapun.")
        self.clear()
    
    def tampilkan_daftar_peserta(self):
        for i, (peserta, acara) in enumerate (self.acara_peserta, start=1):
            print(f'{i}. {peserta} - {acara}')
        self.clear()

    def batalkan_pendaftaran(self,nama_peserta):
        ketemu = False
        for nama in self.acara_peserta[:]:
            if nama[0] == nama_peserta:
                self.acara_peserta.remove(nama)
                print(f"{nama_peserta} berhasil membatalkan pendaftaran.")
                ketemu = True
            if not ketemu:
                print(f"{nama_peserta} tidak terdaftar untuk acara apapun.")
        self.clear()

def simpan_data(acara):
    with open("data_pendaftaran.txt", "w") as file:
        for acara_peserta in acara.acara_peserta:
            file.write(f"{acara_peserta[0]}, {acara_peserta[1]}\n")

def baca_data():
    acara = Acara()
    try:
        with open("data_pendaftaran.txt", "r") as file:
            baca_file = file.readlines()
            for peserta in baca_file:
                nama_peserta, nama_acara = peserta.strip().split(", ")
                acara.acara_peserta.append((nama_peserta, nama_acara))
    except FileNotFoundError:
        pass
    return acara

acara = baca_data()
while True:
    print('\n' + '='*30)
    print('    🎉 PENDAFTARAN EVENT 🎉')
    print('='*30 + '\n')
    print("1. 📝 Daftar Peserta")
    print("2. 🔍 Cari Peserta")
    print("3. ❌ Batalkan Pendaftaran")
    print("4. 📋 Tampilkan Daftar Peserta")
    print("0. 🚪 Keluar\n")

    pilihan = input("👉 Masukkan pilihan Anda: ")

    if pilihan == "1":
        os.system('cls')
        print('\n' + '='*30)
        print('\tPENDAFTARAN EVENT')
        print('='*30)
        nama_peserta = input('\n👤 Masukkan Nama Anda: ')
        print('🎯 Pilih Acara yang Ingin Anda Ikuti:')
        print('1. Study Group IMV')
        print('2. Workshop Deep Learning')
        print('3. Workshop Image Detection')
        print('4. Workshop Image Optimization')
        pilihan = input('Masukkan nomor pilihan Anda: ')
        if pilihan == '1':
            nama_acara = 'Study Group IMV'
        elif pilihan == '2':
            nama_acara = 'Workshop Deep Learning'
        elif pilihan == '3':
            nama_acara = 'Workshop Image Detection'
        elif pilihan == '4':
            nama_acara = 'Workshop Image Optimization'
        else:
            print('Pilihan tidak ada.')
            continue
        acara.daftar_peserta(nama_peserta, nama_acara)

    elif pilihan == "2":
        os.system('cls')
        print('\n' + '='*30)
        print('      🔍 CARI PESERTA 🔍')
        print('='*30)
        nama_peserta = input("\n👤 Masukkan Nama Peserta: ")
        acara.cari_peserta(nama_peserta)

    elif pilihan == "3":
        os.system('cls')
        print('\n' + '='*30)
        print(' ❌ PEMBATALAN PENDAFTARAN ❌')
        print('='*30)
        nama_peserta = input("\n👤 Masukkan Nama Peserta: ")
        acara.batalkan_pendaftaran(nama_peserta)

    elif pilihan == "4":
        os.system('cls')
        print('\n' + '='*30)
        print('\tLIST PESERTA')
        print('='*30)
        acara.tampilkan_daftar_peserta()

    elif pilihan == "0":
        simpan_data(acara)
        print("Terima kasih, Telah Mendaftar!!")
        break

    else:
        print("Pilihan Tidak Valid. (masukkan antara 0 - 1)")
        input('Press Enter to continue...')
