# Sequential
print('ibu berkata "pergi ke toko".')
print('budi menjawab , "baik apa yang harus saya lakukan di toko?"')
print('ibu menjawab, "Beli 1 botol susu, dan jika ada telor beli 6"')
print("maka budi berangkat ke toko")
print("dan mulai berbelanja")

# Percabangan
milk_bottle_stock = 200
egg_stock = 2000
print(f"\negg_stock {egg_stock} pcs")
print(f"milk_bottle_stock {milk_bottle_stock} bottle")

if milk_bottle_stock > 0:
    print("\nbudi check his money and enough")
    if egg_stock == 6:
        print("budi buying 1 bottle of milk")
    else:
        print("budi buying 6 pcs of egg")
else:
    print("budi not buying 1 bottle of milk")

print("\nbudi go to home")
print("told to mom the result ")