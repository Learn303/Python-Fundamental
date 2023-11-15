#pengulangan dengan while
jumlah_buku = 10
print ('ibu berkata, "baca bukumu!"')
total_jumlah_baca = 0

jumlah_buku_yang_dibaca_dan_dipahami = 0
print(f'jumlah buku yang sudah dibaca dan dipahami= {jumlah_buku_yang_dibaca_dan_dipahami}')

while total_jumlah_baca < jumlah_buku * 2 :
    total_jumlah_baca = total_jumlah_baca + 1
    if jumlah_buku_yang_dibaca_dan_dipahami == 9:
      print(f"buku ke {jumlah_buku_yang_dibaca_dan_dipahami + 1} belum paham")
    else:
        jumlah_buku_yang_dibaca_dan_dipahami =jumlah_buku_yang_dibaca_dan_dipahami + 1
        print(f"buku ke {jumlah_buku_yang_dibaca_dan_dipahami} sudah dibaca dan dipahami")

if jumlah_buku_yang_dibaca_dan_dipahami == jumlah_buku:
    print('"bu semua buku sudah dibaca"')
else:
    print(f'"bu tidak semua buku dapat dipahami"')

print(f"jumlah buku yang dibaca dan dipahami = {jumlah_buku_yang_dibaca_dan_dipahami} buku bu")