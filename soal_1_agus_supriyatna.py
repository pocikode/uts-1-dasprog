#!/usr/bin/env python3

import sys

def usd_to_idr(usd):
    # kurs dollar
    EXCHANGE_RATE = 14591

    # validasi apakah tipe inputan numeric
    if input_usd.isnumeric() == False:
        sys.exit('Input dollar harus tipe numeric')

    return int(usd) * EXCHANGE_RATE

# ambil input jumlah dollar
input_usd = input('Masukan jumlah dollar: ')

result = usd_to_idr(input_usd)

# format rupiah
idr_format = 'Rp{:,}'.format(result).replace(',', '.')

print('Hasil penukaran ${} adalah {}'.format(input_usd, idr_format))