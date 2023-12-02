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
