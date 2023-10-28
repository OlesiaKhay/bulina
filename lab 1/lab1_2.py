# TODO Найдите количество книг, которое можно разместить на дискете

disk = 1.44*1024*1024 #переводим в байты
pages = 100
rows = 50
symbols = 25
one_s = 4

quantity = disk/(pages*rows*symbols*one_s)

print("Количество книг, помещающихся на дискету:", int(quantity))
