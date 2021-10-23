#!/usr/bin/env python3

import sys

print("Soal 4 - Agus Supriyatna")
print("Program Perhitungan Gaji Mingguan Karyawan\n")

# upah per jam berdasarkan golongan
# golongan: upah perjam
FEE_PER_HOURS = {
    1: 3000,
    2: 3500,
    3: 4000,
    4: 4500
}

MAX_WORKING_HOURS = 40

group = int(input('Masukkan golongan (1-4): '))
if group < 1 or group > 4:
    sys.exit('Error: golongan hanya boleh 1 - 4')
    
working_hours = int(input('Masukan total jam kerja: '))

if working_hours <= MAX_WORKING_HOURS:
    salary = working_hours * FEE_PER_HOURS[group]
else:
    overtime = working_hours - MAX_WORKING_HOURS
    salary   = (MAX_WORKING_HOURS * FEE_PER_HOURS[group]) + (overtime * FEE_PER_HOURS[group] * 1.5)

print()
print('Upah karyawan:', salary)