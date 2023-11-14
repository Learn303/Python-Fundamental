#pengulangan dengan while
jumlah_buku = 10
print ('ibu berkata, "baca bukumu!"')

jumlah_buku_yang_dibaca = 0
print(f'jumlah buku yang sudah dibaca = {jumlah_buku_yang_dibaca}')

while jumlah_buku_yang_dibaca < jumlah_buku:
    jumlah_buku_yang_dibaca = jumlah_buku_yang_dibaca + 1
    print(f'buku ke {jumlah_buku_yang_dibaca} sudah dibaca')


print(f'jumlah_buku_yang_dibaca = {jumlah_buku_yang_dibaca}')