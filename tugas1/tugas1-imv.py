import os

class Acara:
    def __init__(self):
        self.acara_peserta = []

    def daftar_peserta(self, nama_peserta):
        self.peserta.append(nama_peserta)
        print(f"{nama_peserta} berhasil mendaftar untuk {self.nama_acara}.")

    def cari_peserta(self, nama_peserta):
        if nama_peserta in self.peserta:
            print(f"{nama_peserta} terdaftar untuk {self.nama_acara}.")
        else:
            print(f"{nama_peserta} tidak terdaftar untuk {self.nama_acara}.")

    def batalkan_pendaftaran(self, nama_peserta):
        if nama_peserta in self.peserta:
            self.peserta.remove(nama_peserta)
            print(f"{nama_peserta} berhasil membatalkan pendaftaran untuk {self.nama_acara}.")
        else:
            print(f"{nama_peserta} tidak terdaftar untuk {self.nama_acara}.")

    def tampilkan_daftar_peserta(self):
        print(f"Daftar Peserta untuk {self.nama_acara}:")
        for peserta in self.peserta:
            print(f"- {peserta}")
        


def simpan_data(acara):
    with open("data_pendaftaran.txt", "w") as file:
        for acara_peserta in acara.acara_peserta:
            file.write(f"{acara_peserta[0]}, {acara_peserta[1]}\n")


def baca_data():
    acara = Acara()
    try:
        with open("data_pendaftaran.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                nama_acara, nama_peserta = line.strip().split(", ")
                acara.acara_peserta.append((nama_acara, nama_peserta))
    except FileNotFoundError:
        pass
    return acara


acara = baca_data()
while True:
    print("\n----- Pendaftaran Acara -----")
    print("1. Daftar Peserta")
    print("2. Cari Peserta")
    print("3. Batalkan Pendaftaran")
    print("4. Tampilkan Daftar Peserta")
    print("0. Keluar")

    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == "1":
        nama_peserta = input("Masukkan nama peserta: ")
        acara.daftar_peserta(nama_peserta)

    elif pilihan == "2":
        nama_peserta = input("Masukkan nama peserta: ")
        acara.cari_peserta(nama_peserta)

    elif pilihan == "3":
        nama_peserta = input("Masukkan nama peserta: ")
        acara.batalkan_pendaftaran(nama_peserta)

    elif pilihan == "4":
        acara.tampilkan_daftar_peserta()

    elif pilihan == "0":
        simpan_data(acara)
        print("Terima kasih! Selesaiiiiiiiiiiiiiii")
        break

    else:
        print("Pilihan tidak valid.")
