#!/usr/bin/env python3

import sys

def usd_to_idr(amount):
    # kurs dollar
    EXCHANGE_RATE = 14591

    return amount * EXCHANGE_RATE

# ambil input jumlah dollar
input_usd = int(input('Masukan jumlah dollar: '))

result = usd_to_idr(input_usd)

# format rupiah
idr_format = 'Rp{:,}'.format(result).replace(',', '.')

print('Hasil penukaran ${} adalah {}'.format(input_usd, idr_format))