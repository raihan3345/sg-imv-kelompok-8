def simpan_data(acara):
    with open("data_pendaftaran.txt", "w") as file:
        for acara_peserta in acara.acara_peserta:
            file.write(f"{acara_peserta[0]}, {acara_peserta[1]}\n")

def tampilkan_daftar_peserta(self):
    for i, (acara, peserta) in enumerate (self.acara_peserta, start=1):
        print(f'{i}.{peserta}. {acara}')
    input("Press any key to continue..")
    os.system("cls")

def batalkan_pendaftaran(self,nama_peserta):
    ketemu = False
    for acara_peserta in self.acara_peserta[:]:
        if acara_peserta[1] == nama_peserta:
            self.acara_peserta.remove(acara_peserta)
            print(f"{nama_peserta} berhasil membatalkan pendaftaran.")
            ketemu = True
        if not ketemu:
            print(f"{nama_peserta} tidak terdaftar untuk acara apapun.")
        input('Press Enter to continue...')
        os.system('cls')


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
