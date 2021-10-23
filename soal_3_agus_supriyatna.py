#!/usr/bin/env python3

print("Soal 3 - Agus Supriyatna")
print("Program perhitungan data nilai\n")

MAX_INPUT = 3

value_lists = []
value_sum   = 0

for i in range(1, MAX_INPUT + 1):
    dummy_input = int(input('Masukkan nilai ke-{:d}: '.format(i)))

    value_lists.append(dummy_input)
    value_sum += dummy_input

print()
print('Nilai yang diinput adalah', ', '.join(map(str, value_lists)))
print('Total nilai yang diinput adalah', value_sum)
print('Rata-rata nilai yang diinput adalah', value_sum / MAX_INPUT)
