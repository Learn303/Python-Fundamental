daftar_buku = ['Seven Habit', 'how to influence poeple', 'first thing first']
print('tampilkan semua daftar buku')
print(daftar_buku)

print('\nproses semua dengan In')
for buku in daftar_buku:
    print(buku)

print('\ndaftar buku pada urutan tertentu')
print(daftar_buku[1])
print(daftar_buku[2])


for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])


daftar_buku =[23, 'aadc', -303, 'roc', 10.1]
print('\nTampilkan dengan for i range, dimana tipe data setiap element berbeda')
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])


print('\nKembaikan awal nilai daftar buku')
daftar_buku = ['seven habbit', 'how to influence people', 'thing first thing', 'aadc']
print('\ntambakan beberapa buku baru')
daftar_buku.append ('holla')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])



print('\nClear list')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku)


print('\nKembaikan awal nilai daftar buku dan ganti judul beberapa buku')
daftar_buku = ['seven habbit', 'how to influence people', 'thing first thing', 'aadc']
daftar_buku[0]='bad habbit'
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])


print('\nAmbil beberapa element dari list dengan pop')
daftar_buku.pop(2)
for i in range(0, len(daftar_buku)):
    print(daftar_buku)

print('\nMengambil element dengan pop element terakhir')
daftar_buku = ['seven habbit', 'how to influence people', 'thing first thing', 'aadc']
daftar_buku.pop(-1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])