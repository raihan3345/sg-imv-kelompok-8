import json

class Acara:
    def __init__(self):
        self.nama_acara = "Acara Tralalala"
        self.peserta = []

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
    with open("data_pendaftaran.json", "w") as file:
        data = {acara.nama_acara: acara.peserta}
        json.dump(data, file)

def baca_data():
    try:
        with open("data_pendaftaran.json", "r") as file:
            data = json.load(file)
            acara = Acara()
            acara.peserta = data.get(acara.nama_acara, [])
            return acara
    except FileNotFoundError:
        return Acara()


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
