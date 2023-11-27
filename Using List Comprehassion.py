print('\nPerintah del dengan list comprehanssion')
daftar_buku = ['seven habbit', 'how to influence people', 'thing first thing', 'aadc']
del daftar_buku[0:2]#menghapus mulai dari 0 sejumlah 2 element
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])



print('\nPerintah del dengan list comprehassion menggunakan "start" ')
daftar_buku = ['seven habbit', 'how to influence people', 'thing first thing', 'aadc']
del daftar_buku[0::2]#menghapus menggunakan start, end & step. dimulai dari 1 loncat 2 step
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])   