#!/usr/bin/env python3

import sys

def work_hours(clock_in, clock_out):
    # asumsi menggunakan format waktu 12 jam (am/pm)
    # berarti jika jam keluar lebih kecil dari jam masuk,
    # maka jam keluar ditambah 12 supaya berubah menjadi format 24 jam
    if clock_out < clock_in:
        clock_out += 12

    return clock_out - clock_in


def validate_hour(val):
    if val < 1 or val > 12:
        sys.exit('Error: Jam hanya boleh berupa angka 1-12')


# Execute the program
print("Soal 2 - Agus Supriyatna")
print("Program perhitungan berapa lama pegawai bekerja\n")

clock_in  = int(input('Jam Masuk (1-12): '))
validate_hour(clock_in)

clock_out = int(input('Jam Keluar (1-12): '))
validate_hour(clock_out)

print('Lama bekerja', work_hours(clock_in, clock_out), 'jam')