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
