import os

class Acara:
    def __init__(self):
        self.acara_peserta = []

    def clear(self):
        input('Press Enter to continue')
        os.system('cls')

    def daftar_peserta(self, nama_peserta, nama_acara):
        self.acara_peserta.append(nama_peserta, nama_acara)
        print(f"{nama_peserta} berhasil mendaftar untuk {self.nama_acara}.")
        self.clear()

    def cari_peserta(self, nama_peserta):
        peserta_terdaftar = [(acara, peserta) for acara, peserta in self.acara_peserta if peserta == nama_peserta]
        if peserta_terdaftar:
            for acara, peserta in peserta_terdaftar:
                print(f"{peserta} terdaftar untuk {acara}.")
        else:
            print(f"{nama_peserta} tidak terdaftar untuk acara apapun.")
        self.clear()
    
    def tampilkan_daftar_peserta(self):
        for i, (acara, peserta) in enumerate (self.acara_peserta, start=1):
            print(f'{i}.{peserta}. {acara}')
        self.clear()

    def batalkan_pendaftaran(self,nama_peserta):
        ketemu = False
        for acara_peserta in self.acara_peserta[:]:
            if acara_peserta[1] == nama_peserta:
                self.acara_peserta.remove(acara_peserta)
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
                nama_acara, nama_peserta = peserta.strip().split(", ")
                acara.acara_peserta.append((nama_acara, nama_peserta))
    except FileNotFoundError:
        pass
    return acara
