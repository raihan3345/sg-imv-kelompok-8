import os
import time


def daftar(peserta):
    os.system('cls')
    print('\t==== PENDAFTARAN EVENT FAREWELL PARTY ====\n')
    nama = input('Masukkan Nama Anda: ')
    peserta[nama] = True
    with open('data.txt', 'w') as f:
        for i in peserta:
            f.write(i + '\n')
    print(f'{nama} Berhasil Terdaftar.')
    input('Press Enter to continue...')
    time.sleep(2)
    os.system('cls')
